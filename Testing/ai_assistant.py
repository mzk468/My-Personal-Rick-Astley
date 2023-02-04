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
            playsound('never_gonna_give_you_up.mp3')
            return "Gonna give you up."

        if audio.startswith("Gonna"):
            # randomly choose one of the lyrics
            # return the lyric
            lyrics = ["Gonna let you down", "Gonna run around and desert you", "Gonna make you cry", "Gonna say goodbye", "Gonna tell a lie and hurt you"]
            if random.choice[lyrics] == "Gonna let you down":
                playsound('never_gonna_let_you_down.mp3')
            elif random.choice[lyrics] == "Gonna run around and desert you":
                playsound('never_gonna_run_around_and_desert_you.mp3')
            elif random.choice[lyrics] == "Gonna make you cry":
                playsound('never_gonna_make_you_cry.mp3')
            elif random.choice[lyrics] == "Gonna say goodbye":
                playsound('never_gonna_say_goodbye.mp3')
            elif random.choice[lyrics] == "Gonna tell a lie and hurt you":
                playsound('never_gonna_tell_a_lie_and_hurt_you.mp3')
            return random.choice(lyrics)


        elif audio.startswith("What"):
            playsound('what_do_you_want_from_me.mp3')
            return "What do you want from me?"
        if audio.startsWith("Inside"):
            playsound('inside_we_both_know_what_has_been_going_on.mp3')
            return "Inside, we both know what's been going on (going on)"

        elif audio.startswith("You"):
            playsound('you_know_the_rules_and_so_do_i.mp3')
            return "You know what the rules are."
        elif audio.startswith("I"):
            playsound('i_just_wanna_tell_you_how_im_feeling.mp3')
            return "I just wanna tell you how I'm feeling."
        elif audio.startswith("A"):
            playsound('a_full_commitment_thats_what_im_thinking_of.mp3')
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

def main():
    # Create the AI assistant
    # Then run the AI assistant
    # The AI assistant will listen for input
    # If the input is a command, then the AI assistant will run the command
    # If the input is not a command, then the AI assistant will process the input
    # The AI assistant will then speak the processed input
    # The AI assistant will then listen for input again
    # This will continue until the AI assistant is terminated
    # The AI assistant is terminated by saying "goodbye"
    # The AI assistant will then say "goodbye" and terminate
    rick = rick_atsley()
    speak("Hello, I am Rick Astley. How can I help you?")
    while True:
        query = listen().lower()
        if "time" in query:
            get_time()
        elif "date" in query:
            get_date()
        elif "day" in query:
            get_day()
        elif "weather" in query:
            get_weather()
        elif "news" in query:
            get_news()
        elif "open" in query:
            get_app()
        elif "goodbye" in query:
            speak("Goodbye")
            break
        else:
            speak(process(query))

