import requests
import json
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

## newsapi.org
def speak_news():
    
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=API_KEY'
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak('Source: Top-Headlines ')
    speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        speak(articles['title'])
        if index == len(arts)-1:
            break
        speak('Moving on the next news headline..')
    speak('These were the top headlines, Have a nice day Sir!!..')

def getNewsUrl():
    return 'https://newsapi.org/v2/top-headlines?country=us&apiKey=API_KEY'

if __name__ == '__main__':
    speak_news()
