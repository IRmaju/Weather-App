# 🌦 Weather App 

A simple weather application built with **Streamlit**, **Python**, and the **OpenWeatherMap API**. This app allows users to enter a city name and get live weather data securely by loading the API key from an environment file (`.env`).

---

## 🎯 Features:
- **City-based Weather**: Enter a city name and get the current weather.
- **Real-time Data**: Get real-time data from OpenWeatherMap API.
- **Environment Variables**: The app securely loads the API key from a `.env` file for security and better handling.
- **Responsive Design**: The app is built using **Streamlit**, ensuring it runs in a web browser smoothly.

---

## 📦 Requirements:

Before running the app, you need to install the necessary libraries. You can do this using `pip`:

```bash
pip install streamlit requests python-dotenv

🌍 How It Works:
Enter a City Name: Type the name of a city into the input box.

Click on 'Get Weather': The app will fetch live weather data using the OpenWeatherMap API.

View Weather Details: See the temperature, weather description, humidity, and wind speed.

💬 Example Output:
Input: "New York"

Output:

Location: New York, US

Temperature: 25°C

Weather: Clear Sky

Humidity: 60%

Wind Speed: 5.2 m/s

