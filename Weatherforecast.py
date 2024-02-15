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
window.title("Weather Forecast App")
window.geometry("400x300")
window.configure(bg="light blue")   # Set the initial window size

# Header Label
header_label = tk.Label(window, text="Weather Forecast by Yash", font=("Helvetica", 20, "bold"), fg="blue",background="light blue")
header_label.pack(pady=10)

# City Entry
label = tk.Label(window, text="Enter City:", font=("Helvetica", 15), background="light blue")
label.pack(pady=5)

entry = tk.Entry(window, font=("Helvetica", 15))
entry.pack(pady=10)

# Get Weather Button
button = tk.Button(window, text="Get Weather Report", command=get_weather_report, font=("Helvetica", 16), bg="green", fg="white")
button.pack(pady=10)

# Exit Button
exit_button = tk.Button(window, text="Exit", command=window.destroy, font=("Helvetica", 15), bg="red", fg="white")
exit_button.pack(pady=10)

window.mainloop()
