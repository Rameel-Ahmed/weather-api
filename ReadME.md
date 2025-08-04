
# 🌤️ Weather API Flask App

A simple Flask application that provides weather temperature data via RESTful APIs. The data is sourced from local `.txt` files containing station-wise daily temperature logs.

---

## 📁 Project Structure

```
├── app.py
├── templates/
│   └── home.html
├── data_small/
│   ├── stations.txt
│   └── TG_STAIDxxxxxx.txt
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone or download** this repository.

2. (Optional but recommended) **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   # Activate (Windows)
   venv\Scripts\activate
   # Activate (Mac/Linux)
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install Flask pandas
   ```

4. **Run the Flask app**:

   ```bash
   python app.py
   ```

5. Open your browser and navigate to:  
   📍 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🚀 API Endpoints

### `/`
- Returns an HTML page showing a table of available stations.

---

### `/api/v1/<station>/<date>`
- **Purpose**: Get temperature of a specific station on a given date.
- **Example**: `/api/v1/10/1992-03-05`
- **Response**:
  ```json
  {
    "station": "10",
    "date": "1992-03-05",
    "temperature": 7.3
  }
  ```

---

### `/api/v1/<station>`
- **Purpose**: Get all temperature records for a specific station.
- **Example**: `/api/v1/10`
- **Response**: JSON list of temperature records.

---

### `/api/v1/yearly/<station>/<year>`
- **Purpose**: Get all records for a specific year and station.
- **Example**: `/api/v1/yearly/10/1991`
- **Response**: JSON list filtered by year.

---

## 🧠 Notes
- All temperature data is originally in tenths of degrees Celsius and is divided by 10 in the output.
- Make sure your file names follow this pattern:  
  `TG_STAID######.txt` (e.g., `TG_STAID000010.txt`)
- The stations list is read from `stations.txt` (skipping first 17 lines).

---

