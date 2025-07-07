import streamlit as st
import requests

API_KEY = "008c39a2b0c88774a68051aa442e21e3"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["cod"] == 200:
            return data
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    return None

def get_weather_emoji(weather_id):
    if 200 <= weather_id <= 232:
        return "⛈️"
    elif 300 <= weather_id <= 321:
        return "🌦️"
    elif 500 <= weather_id <= 531:
        return "🌧️"
    elif 600 <= weather_id <= 622:
        return "❄️"
    elif 700 <= weather_id <= 741:
        return "🌫️"
    elif weather_id == 762:
        return "🌋"
    elif weather_id == 771:
        return "💨"
    elif weather_id == 781:
        return "🌪️"
    elif weather_id == 800:
        return "☀️"
    elif 801 <= weather_id <= 804:
        return "☁️"
    else:
        return "❓"

# Streamlit UI
st.set_page_config(page_title="Weather App", layout="centered")
st.title("🌦️ Weather App")
st.markdown("Enter your city below to get current weather:")

city = st.text_input("City Name", "")

if st.button("Get Weather") and city:
    result = get_weather(city)
    if result and "error" not in result:
        temp_c = result["main"]["temp"]
        temp_f = (temp_c * 9/5) + 32
        weather_id = result["weather"][0]["id"]
        desc = result["weather"][0]["description"]

        st.markdown(f"### 🌡️ Temperature: `{temp_f:.0f}°F`")
        st.markdown(f"### {get_weather_emoji(weather_id)} {desc.title()}")
    elif "error" in result:
        st.error(f"Error: {result['error']}")
    else:
        st.error("Could not fetch weather data. Please check the city name.")
