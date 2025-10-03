# fetch_weather_dashboard.py
import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_open_meteo(lat, lon, start_date, end_date, timezone="auto"):
    """Fetch hourly temperature and precipitation data from Open-Meteo API"""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": ["temperature_2m", "precipitation"],
        "timezone": timezone
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    df = pd.DataFrame(data["hourly"])
    df["time"] = pd.to_datetime(df["time"])
    return df

def create_dashboard(df):
    """Visualize temperature and rainfall trends"""
    plt.figure(figsize=(12,6))

    # Temperature plot
    plt.subplot(2, 1, 1)
    plt.plot(df["time"], df["temperature_2m"], color="red")
    plt.title("Hourly Temperature")
    plt.ylabel("°C")

    # Precipitation plot
    plt.subplot(2, 1, 2)
    plt.plot(df["time"], df["precipitation"], color="blue")
    plt.title("Hourly Precipitation")
    plt.ylabel("mm")
    plt.xlabel("Time")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example: Delhi, India (28.6N, 77.2E), last 2 days
    df = fetch_open_meteo(lat=28.6, lon=77.2,
                          start_date="2025-10-01", end_date="2025-10-03")
    create_dashboard(df)
