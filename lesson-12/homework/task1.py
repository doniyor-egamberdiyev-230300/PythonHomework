from bs4 import BeautifulSoup

# Open and read the file
with open("weather.html", "r", encoding="utf-8") as file:
    content = file.read()

# Parse the HTML content
soup = BeautifulSoup(content, "html.parser")

# Get all rows from the table
rows = soup.find("table").find("tbody").find_all("tr")

# List to store weather data
weather_data = []

# Extract data from each row
for row in rows:
    cols = row.find_all("td")
    day = cols[0].text.strip()
    temperature = int(cols[1].text.strip().replace("°C", ""))  # Remove "°C" and convert to int
    condition = cols[2].text.strip()

    weather_data.append({"day": day, "temperature": temperature, "condition": condition})

# 1. **Print all weather data**
print("\n5-Day Weather Forecast:")
for entry in weather_data:
    print(f"{entry['day']}: {entry['temperature']}°C, {entry['condition']}")

# 2. **Find the hottest day**
highest_temp_day = max(weather_data, key=lambda x: x['temperature'])
print(f"\n🌡️ Hottest day: {highest_temp_day['day']} ({highest_temp_day['temperature']}°C)")

# 3. **Find all "Sunny" days**
sunny_days = [entry['day'] for entry in weather_data if entry['condition'] == "Sunny"]
print(f"☀️ Sunny days: {', '.join(sunny_days)}")

# 4. **Calculate the average temperature**
average_temp = sum(entry['temperature'] for entry in weather_data) / len(weather_data)
print(f"📊 Average temperature: {average_temp:.2f}°C")
