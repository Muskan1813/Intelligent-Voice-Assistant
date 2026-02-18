import requests
import speech_recognition
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("OPENWEATHER_KEY not found in .env file")


def get_city(speaker, recognizer):
    speaker.say("Which city?")
    speaker.runAndWait()

    try:
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            audio = recognizer.listen(source, timeout=5)
            city = recognizer.recognize_google(audio, language="en-IN")

            print("[DEBUG] City:", city)
            return city

    except:
        speaker.say("I could not understand the city")
        speaker.runAndWait()
        return None


def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()
    
    print("[DEBUG] API response:", data)

    if data.get("cod") != 200:
        return None

    return data


def current_weather(speaker, recognizer):
    city = get_city(speaker, recognizer)
    if not city:
        return

    data = get_weather_data(city)
    if not data:
        speaker.say("Could not fetch weather data")
        speaker.runAndWait()
        return

    description = data["weather"][0]["description"]
    temp = data["main"]["temp"]

    speaker.say(f"The weather in {city} is {description} with temperature {temp} degrees Celsius")
    speaker.runAndWait()


def temperature(speaker, recognizer):
    city = get_city(speaker, recognizer)
    if not city:
        return

    data = get_weather_data(city)
    if not data:
        speaker.say("Could not fetch temperature")
        speaker.runAndWait()
        return

    temp = data["main"]["temp"]

    speaker.say(f"The temperature in {city} is {temp} degrees Celsius")
    speaker.runAndWait()


def humidity(speaker, recognizer):
    city = get_city(speaker, recognizer)
    if not city:
        return

    data = get_weather_data(city)
    if not data:
        speaker.say("Could not fetch humidity")
        speaker.runAndWait()
        return

    humidity = data["main"]["humidity"]

    speaker.say(f"The humidity in {city} is {humidity} percent")
    speaker.runAndWait()


def will_it_rain(speaker, recognizer):
    city = get_city(speaker, recognizer)
    if not city:
        return

    data = get_weather_data(city)
    if not data:
        speaker.say("Could not fetch forecast")
        speaker.runAndWait()
        return

    description = data["weather"][0]["description"]

    if "rain" in description.lower():
        speaker.say(f"Yes, it looks like it may rain in {city}")
    else:
        speaker.say(f"It does not look like rain in {city}")

    speaker.runAndWait()
