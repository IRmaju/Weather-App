import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

st.set_page_config(page_title="Weather App", page_icon="🌦")
st.title("🌦 Weather App (Secure)")

city = st.text_input("Enter city name")

if st.button("Get Weather") and city:
    if not API_KEY:
        st.error("⚠️ API key not found. Make sure .env file is set correctly.")
    else:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") == 200:
            city_name = data["name"]
            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            weather_description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            st.subheader(f"📍 Location: {city_name}, {country}")
            st.metric("🌡 Temperature", f"{temperature} °C")
            st.write(f"☁️ **Weather:** {weather_description.title()}")
            st.write(f"💧 **Humidity:** {humidity}%")
            st.write(f"💨 **Wind Speed:** {wind_speed} m/s")
        else:
            st.error("❌ City not found! Please enter a valid city name.")
