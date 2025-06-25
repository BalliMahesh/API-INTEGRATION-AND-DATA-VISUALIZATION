import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# --- Configuration ---
API_KEY = 'YOUR_API_KEY'  # 🔁 Replace with your OpenWeatherMap API key
CITY = 'Hyderabad'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# --- Fetch Weather Data ---
response = requests.get(URL)
data = response.json()

# --- Extract Date and Temperature ---
dates = []
temperatures = []

for entry in data.get('list', []):
    dt = datetime.datetime.fromtimestamp(entry['dt'])
    temp = entry['main']['temp']
    dates.append(dt)
    temperatures.append(temp)

# --- Plot with Seaborn ---
sns.set(style='whitegrid')
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temperatures, marker='o', color='blue')

plt.title(f"5-Day Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()