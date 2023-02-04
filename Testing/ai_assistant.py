import os
import random
import datetime
import pyttsx3
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Class for the AI assistant
# This class contains all the functions for the AI assistant
# The functions are called from the main program
# The functions are:
#   - speak
#   - listen
#   - get_time
#   - get_date
#   - get_day
#   - get_weather
#   - get_news
#   - get_wikipedia
#   - get_google
#   - get_youtube
#   - get_facebook
#   - get_twitter
#   - get_instagram
#   - get_reddit
#   - get_gmail
#   - get_outlook
#   - get_yahoo
#   - get_aol

class rick_atsley:
    # Initialise the AI assistant
    # This function is called when the AI assistant is created
    # It sets the name, version, built date and creator of the AI assistant
    # It also sets the voice of the AI assistant
    # The voice is set to the voice of Rick Astley
    # The voice is set using the pyttsx3 library
    # The pyttsx3 library is used to convert text to speech

    

    def __init__(self):
        self.name = "Rick Astley"
        self.version = "1.0.0"
        self.built = "February 2023"
        self.creator = "Royal Holloway University of London"

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)



    def speak(audio):
        engine.say(process(audio))
        engine.runAndWait()
  
    def listen():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            speak("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            speak(f"You said: {query}\n")
        except Exception as e:
            speak("Say that again please...")
            return "None"
        return query
    def process(audio):
        # listen to the input from the user
        # then return a rick atsley lyric if the input starts with a word in his songs
        # otherwise return the input
        if audio.startswith("Never"):
            return "Gonna give you up."
        if audio.startswith("Gonna"):
            # randomly choose one of the lyrics
            # return the lyric
            lyrics = ["Gonna let you down", "Gonna run around and desert you", "Gonna make you cry", "Gonna say goodbye", "Gonna tell a lie and hurt you"]
            return random.choice(lyrics)


        elif audio.startswith("What"):
            return "Inside, we both know what's been going on (going on)"
        if audio.startsWith("Inside"):
            return "Inside, we both know what's been going on (going on)"

        elif audio.startswith("You"):
            return "You know what the rules are."
        elif audio.startswith("I"):
            return "I just wanna tell you how I'm feeling."
        elif audio.startswith("A"):
            return "A full commitment that's what I'm thinking of"
    
    def get_time():
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is")
        speak(time)
    def get_date():
        date = datetime.datetime.now().strftime("%B %d, %Y")
        speak("The current date is")
        speak(date)

    def get_day():
        day = datetime.datetime.now().strftime("%A")
        speak("The current day is")
        speak(day)

    def get_weather():
        speak('What city do you want the weather for?')
        city = listen()
        url_address = f'https://www.google.com/search?q=weather+in+{city}'
        driver.get(url_address)
        search = driver.find_element_by_xpath('//*[@id="wob_tm"]')
        speak(f'The current temperature in {city} is {search.text} degrees celsius')

    def get_news():
        speak('What news topic do you want?')
        topic = listen()
        url_address = f'https://www.google.com/search?q={topic}+news'
        driver.get(url_address)
        search = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div[1]/a/h3')
        speak(search.text)
        search.click()
        speak('Here are some news articles about that topic')
    def get_app():
        speak("What app do you want to open?")
        app = listen()
        url_address = f"https://www.google.com/search?q={app}"
        driver.get(url_address)
        search = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div[1]/a/h3')
        speak(search.text)
        search.click()
        speak(f"Opening {app}")

