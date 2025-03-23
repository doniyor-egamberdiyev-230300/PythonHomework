import requests

# API information
API_KEY = "0ab13374c21bd90fef2742776f7ed48e"
CITY = "Tashkent"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Sending API request
response = requests.get(URL)
data = response.json()

# Displaying results
if response.status_code == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_description = data["weather"][0]["description"]

    print(f"City: {CITY}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather description: {weather_description}")
else:
    print("An error occurred:", data.get("message", "Unknown error"))

