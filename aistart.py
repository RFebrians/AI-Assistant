import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import datetime
import os
import sys
import smtplib
from news import speak_news, getNewsUrl
from diction import translate
from helpers import *
from youtube import youtube
from sys import platform
import os
import getpass

engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('rate', rate +15)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)

# print(voices[0].id) optional [1] [2] [3] default 0 is en_us

class ButlerAI:
    def __init__(self) -> None:
        if platform == "linux" or platform == "linux2":
            self.chrome_path = '/usr/bin/google-chrome'

        elif platform == "win32":
            self.chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        else:
            print('Unsupported OS')
            exit(1)
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(self.chrome_path)
        )

    def greetings(self) -> None:
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning ")
        elif hour >= 12 and hour < 18:
            speak("Good Afternoon ")

        else:
            speak('Good Evening ')

        weather()
        speak('Voice Assistant is Ready. How can I help you ?')

    def execute_query(self, query):
        # TODO: lower voice interval or improve adapt sound
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)
        elif 'youtube download' in query:
            exec(open('youtube.py').read())

        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[1].id)
            else:
                engine.setProperty('voice', voices[0].id)
            speak("Hello Sir, I have switched my voice. How is it?")

        #conversation trait
        if 'hello' in query:
            speak("Hi, How are you  ? ")
        if 'who are you' in query:
            speak("I am your assistant , and i am still being development")
        if 'Endruw ' in query:
            speak("He is a very cool and inspired person ")
            
         
        #command
        elif 'open youtube' in query:

            webbrowser.get('chrome').open_new_tab('https://youtube.com')
            
        elif 'open amazon' in query:
            webbrowser.get('chrome').open_new_tab('https://amazon.com')

        elif 'status' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'open google' in query:
            webbrowser.get('chrome').open_new_tab('https://google.com')

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open_new_tab('https://stackoverflow.com')

        elif 'play music' in query:
            os.startfile("./assets/bgm.mp3")

        elif 'search on youtube' in query:
            speak('What you want to search on Youtube?')
            youtube(takeCommand())
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strTime}')

        elif 'search' in query:
            speak('What do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get('chrome').open_new_tab(
                url)
            speak('Based on What is Google Says' + search)

        ## location on development
        elif 'location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.com/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)

        elif 'name' in query:
            speak('I am your assistant')
        elif 'who ' in query:
            speak('I am just an artificial intelegence')
            
        elif ' live' in query:
            speak('I live in your heart ')
        elif ' program ' in query:
            if platform == "win32":
                os.startfile(
                    "C:\\Users\\zegveld\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('code .')

        ## below command are REALLY SHUTDOWN . IT'S GOOD FOR PRANK
        elif 'shutdown' in query:
            if platform == "win32":
                os.system('shutdown /p /f')
            elif platform == "linux" or platform == "linux2" :
                os.system('poweroff')

        ## exit program
        elif 'exit' in query:
            sys.exit()

        elif 'status ' in query:
            cpu()
        elif 'friends ' in query:
            speak('My friends are Google assisstant alexa and siri')

        elif 'github' in query:
            webbrowser.get('chrome').open_new_tab(
                'https://github.com')

        elif 'remember ' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'something important' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'dictionary' in query:
            speak('What do you want to search in your dictionary?')
            translate(takeCommand())

        elif 'news' in query:
            speak('Ofcourse sir..')
            speak_news()
            speak('Do you want to read the full news...')
            test = takeCommand()
            if 'yes' in test:
                speak('Ok Sir, Opening browser...')
                webbrowser.open(getNewsUrl())
                speak('You can now read the full news from this website.')
            else:
                speak('No Problem Sir')

        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)
            speak("Hello Sir, I have switched my voice. How is it?")


if __name__ == '__main__':
    bot_ = ButlerAI()
    bot_.greetings()
    while True:
        query = takeCommand().lower()
        bot_.execute_query(query)
