import tkinter as tk
import pyowm

class WeatherForecastApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast")

        self.api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
        self.owm = pyowm.OWM(self.api_key)
        self.weather = None

        self.city_label = tk.Label(root, text="Enter City or Zip Code:")
        self.city_label.pack(pady=10)

        self.city_entry = tk.Entry(root, width=30)
        self.city_entry.pack(pady=5)

        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack(pady=10)

        self.weather_info_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.weather_info_label.pack(pady=20)

    def get_weather(self):
        location = self.city_entry.get()

        try:
            observation = self.owm.weather_at_place(location)
            self.weather = observation.get_weather()

            temperature = self.weather.get_temperature('celsius')['temp']
            humidity = self.weather.get_humidity()
            wind_speed = self.weather.get_wind()['speed']
            status = self.weather.get_status()

            weather_info = f"Temperature: {temperature:.1f} °C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nWeather: {status.capitalize()}"
            self.weather_info_label.config(text=weather_info)

        except pyowm.exceptions.NotFoundError:
            self.weather_info_label.config(text="Location not found.")
        except Exception as e:
            self.weather_info_label.config(text="Error fetching weather data.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherForecastApp(root)
    root.mainloop()
