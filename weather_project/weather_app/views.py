from django.shortcuts import render
import requests
import datetime

def index(request):
    with open('Your Api key', 'r') as f:
        api_key = f.read().strip()
  
    forecast_url = 'https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}'

    if request.method == 'POST':
        city1 = request.POST['city1']
        city2 = request.POST.get('city2', None)

        weather_data1, daily_forecasts1 = fetch_weather(city1, api_key, forecast_url)

        if city2:
            weather_data2, daily_forecasts2 = fetch_weather(city2, api_key, forecast_url)
        else:
            weather_data2, daily_forecasts2 = None, None

        context = {
            "weather_data1": weather_data1,
            "daily_forecasts1": daily_forecasts1,
            "weather_data2": weather_data2,
            "daily_forecasts2": daily_forecasts2
        }

        return render(request, "weather_app/index.html", context)
    else:
        return render(request, "weather_app/index.html")


def fetch_weather(city, api_key, forecast_url):
    response = requests.get(forecast_url.format(city, api_key))
    data = response.json()

    if 'list' not in data:
        raise ValueError(f"City '{city}' not found or API error: {data}")

    weather_data = {
        "city": city,
        "temperature": round(data['list'][0]['main']['temp'] - 273.15, 2),
        "description": data['list'][0]['weather'][0]['description'],
        "icon": data['list'][0]['weather'][0]['icon']
    }

    # Prvih 5 dana (na svakih 24h)
    daily_forecasts = []
    for i in range(0, 40, 8):
        forecast = data['list'][i]
        daily_forecasts.append({
            "day": datetime.datetime.fromtimestamp(forecast['dt']).strftime("%A"),
            "min_temp": round(forecast['main']['temp_min'] - 273.15, 2),
            "max_temp": round(forecast['main']['temp_max'] - 273.15, 2),
            "description": forecast['weather'][0]['description'],
            "icon": forecast['weather'][0]['icon']
        })

    return weather_data, daily_forecasts
