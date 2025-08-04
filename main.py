from flask import Flask, render_template
import pandas as pd

# Initialize the Flask web application
app = Flask(__name__)

# Read the station metadata from a text file, skipping the first 17 lines
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
# Keep only Station ID and Station Name columns
stations = stations[["STAID", "STANAME                                 "]]

# Home route that displays the station table as an HTML page
@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

# API route: Get temperature for a specific station on a specific date
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # Format the filename using zero-padded station number
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    # Read the station's temperature data, skipping the header
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # Extract the temperature for the given date
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    # Return result as a JSON response
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }

# API route: Get all temperature data for a specific station
@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # Convert the DataFrame to a list of dictionaries
    result = df.to_dict(orient="records")
    return result

# API route: Get all temperature data for a specific station in a given year
@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    # Convert date column to string to filter by year
    df["    DATE"] = df["    DATE"].astype(str)
    # Filter records starting with the specified year
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result

# Run the Flask app in debug mode for development
if __name__ == "__main__":
    app.run(debug=True)
