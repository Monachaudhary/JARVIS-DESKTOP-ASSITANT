from time import strftime
import pyttsx3    #pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.

import speech_recognition as sr
import datetime        # The datetime module supplies classes for manipulating dates and times.
import wikipedia
from wikipedia.wikipedia import languages

engine = pyttsx3.init('sapi5')   # object creation
voices = engine.getProperty('voices')    # getting details of current speaking rate
engine. setProperty('voice',voices[1].id)   #changing index, changes voices. 1 for female

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    print(Time) 
    speak(f"The current time is {Time}")   

def wiki():
    query =("Iphone")
    results = wikipedia.summary(query, sentences=2)
    speak("according to wikipedia") 
    print(results)   
    speak(results)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold =1
        audio = r.listen(source)
    try:
        print("Recognizing....") 
        query = r.Recognize_google(audio, languages= 'en-in')   
        print(f"you said:{query}\n")
    except Exception as e:
        print(e)
        print('say that again...')
        speak("say that again...")  
        return "None"
    return query      

# a = input("enter something to speak\n")
speak("Welcome mam")
time()
wiki()
takecommand()

