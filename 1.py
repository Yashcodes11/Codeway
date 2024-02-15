import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city):
    api_key = 'b5db501322dfa22e7f4c5d4e20330aad'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key,'units':'metric'}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_info = {
                'city': data['name'],
                'description': data['weather'][0]['description'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            return weather_info
        else:
            return None
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def get_weather_report():
    city = entry.get()
    weather_data = get_weather(city)

    if weather_data:
        report = f"Weather forecast for {weather_data['city']}:\n"\
                 f"Description: {weather_data['description']}\n"\
                 f"Temperature: {weather_data['temperature']}°C\n"\
                 f"Humidity: {weather_data['humidity']}%\n"\
                 f"Wind Speed: {weather_data['wind_speed']} m/s"
        messagebox.showinfo("Weather Report", report)
    else:
        messagebox.showerror("Error", "Error fetching weather data.")

# GUI Setup
window = tk.Tk()
window.title("Weather Forecast App by Yash")

label = tk.Label(window, text="Enter City:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=10)

button = tk.Button(window, text="Get Weather Report", command=get_weather_report)
button.pack(pady=10)

window.mainloop()
