# 🌦️ Weather Forecast Web App

This is a **real-time weather forecasting web application** built using **Python** and **Streamlit**. It uses the **OpenWeatherMap API** to fetch current weather information for any city entered by the user. The app displays temperature in Fahrenheit along with a relevant weather emoji 🌤️🌧️🌩️❄️.

---

## 🚀 Live Demo

👉 [Launch Streamlit App](https://your-app-link.streamlit.app/)  
*(You can deploy it on [Streamlit Cloud](https://share.streamlit.io) in seconds)*

---

## 📁 Project Structure

```bash
WEATHER-APP/
├── app.py              # 🌐 Main Streamlit weather app
├── main.py             # 🧠 Optional helper or backup file
├── requirements.txt    # 📦 List of required Python libraries

```
---

## 📌 Features

- ✅ Real-time weather data from OpenWeatherMap API  
- ✅ Temperature displayed in Fahrenheit  
- ✅ Weather description with emojis (☀️ / 🌧️ / ❄️ etc.)  
- ✅ Streamlit-powered, fast, and interactive UI  
- ✅ Minimal design, runs in the browser instantly  

---

## 🧠 Technologies Used

- `Python 3`  
- `Streamlit`  
- `Requests`  
- `OpenWeatherMap API`

---

## 🌐 API Used

- **OpenWeatherMap API** – for fetching weather data  
🔑 You’ll need an API key from [https://openweathermap.org/api](https://openweathermap.org/api)  
Paste your key inside `app.py`:

```python
API_KEY = "your_api_key_here"

