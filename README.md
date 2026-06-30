# Medical Insurance Charges Prediction

A Flask web application that predicts medical insurance charges based on user inputs using a Linear Regression model. The app includes user authentication with JWT and stores prediction data in MongoDB.

## Features

- User registration and login with JWT authentication
- Predicts medical insurance charges based on age, gender, BMI, number of children, smoking status, and region
- Stores prediction results in MongoDB
- Simple web UI with HTML templates

## Tech Stack

- Python
- Flask, Flask-JWT-Extended
- Scikit-learn (Linear Regression)
- MongoDB (pymongo)
- Pandas, NumPy

## Project Structure

```
medical_insurence_charges_prediction/
├── artifacts/
│   ├── linear_reg_med_ins.pkl   # Trained ML model
│   └── med_ins_col_data.json    # Column metadata for encoding
├── src/
│   ├── utils.py                 # ML prediction logic
│   └── database.py              # MongoDB connection
├── templates/                   # HTML templates
├── config.py                    # App configuration
├── main.py                      # Flask app entry point
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository
```bash
git clone <repo-url>
cd medical_insurence_charges_prediction
```

2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Update `config.py` with your MongoDB connection details

5. Run the app
```bash
python main.py
```

The app will start at `http://localhost:5003`

## API Endpoints

| Method | Endpoint    | Description               |
|--------|-------------|---------------------------|
| GET    | `/`         | Home page                 |
| GET    | `/register` | Registration page         |
| POST   | `/register` | Register a new user       |
| GET    | `/login`    | Login page                |
| POST   | `/login`    | Login and get JWT token   |
| GET    | `/predict`  | Prediction page           |
| POST   | `/predict`  | Predict insurance charges (JWT required) |

## Input Fields for Prediction

| Field    | Type   | Example        |
|----------|--------|----------------|
| age      | int    | 25             |
| gender   | string | male / female  |
| bmi      | float  | 27.5           |
| children | int    | 2              |
| smoker   | string | yes / no       |
| region   | string | northeast / southwest / southeast / northwest |
