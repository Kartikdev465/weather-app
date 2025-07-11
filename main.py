import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")   

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;               
            }
            QLabel#city_label{
                font-size: 40px;          
                font-style: italic;
            }    
            QLineEdit#city_input{
                font-size: 40px;           
            } 
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;                      
            }
            QLabel#temperature_label{
                 font-size: 75px;          
            }
            QLabel#emoji_label{
                 font-size: 100px;
                 font-family: segoe UI emoji;          
            }
            QLabel#description_label{
                 font-size: 50px;          
            }    
        """)
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_Key = "008c39a2b0c88774a68051aa442e21e3"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_Key}&units=metric"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
            status = response.status_code
            if status == 400:
                self.display_error("Bad request:\nPlease check your input")
            elif status == 401:
                self.display_error("Unauthorized:\nAPI key")
            elif status == 403:
                self.display_error("Forbidden:\nAccess is denied")
            elif status == 404:
                self.display_error("Not found:\nCity not found")
            elif status == 500:
                self.display_error("Internal Server Error:\nPlease try again later")
            elif status == 502:
                self.display_error("Bad gateway:\nInvalid response from the server")
            elif status == 503:
                self.display_error("Service Unavailable:\nServer is down")
            elif status == 504:
                self.display_error("Gateway timeout:\nNo response from server")
            else:
                self.display_error(f"HTTP error occurred:\n{http_error}") 
        except requests.exceptions.ConnectionError:
            self.display_error("Connection error:\nCheck your internet connection")               
        except requests.exceptions.Timeout:
            self.display_error("Timeout error:\nThe request timed out")               
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")               
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")


    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temperature_c = data["main"]["temp"]  # Already in Celsius due to `units=metric`
        temperature_f = (temperature_c * 9/5) + 32
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        self.temperature_label.setText(f"{temperature_f:.0f}°F")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)  # FIXED typo from setTExt

    @staticmethod    
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
            return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())