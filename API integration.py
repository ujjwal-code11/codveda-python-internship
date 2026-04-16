import requests

API_KEY = "91960e13f0a1eda86d1f941dbebf1429"
city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print("\nWeather Details:")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Condition:", data["weather"][0]["description"])
    else:
        print("Error:", data["message"])

except Exception as e:
    print("Something went wrong:", e)