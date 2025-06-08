Weather App (Django)

This is a Django-based web application that allows users to compare the current weather and 5-day forecast for up to two cities using the OpenWeatherMap API.
🔧 Features

    Enter one or two city names to get weather data

    Displays:

        Current temperature (in °C)

        Weather description

        Weather icon

        5-day forecast (daily min/max temp and conditions)

    Fetches data from OpenWeatherMap's Forecast API

    Lightweight and beginner-friendly Django setup

📦 Requirements

    Python 3.10+

    Django 5+

    requests library

    OpenWeatherMap API key (free)

🚀 How to Run

    Clone the repo:

git clone https://github.com/yourusername/weather-app.git
cd weather-app

Create a virtual environment and activate it:

python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows

Install dependencies:

pip install -r requirements.txt

Add your API key:

    Create a file named API_KEY inside the project directory (where manage.py is)

    Paste your OpenWeatherMap API key into the file (no quotes, no spaces)

Run the app:

python manage.py runserver

Open in browser:

    http://127.0.0.1:...../

📷 Screenshot

(Optional: add a screenshot of the app here)
🧠 Note

This project uses the OpenWeatherMap Forecast API, not One Call. It works with free accounts.
