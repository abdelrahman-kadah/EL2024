"""
Alexa Features:
-> Tell the current time.
-> Tell the current date.
-> Tell jokes.
-> Open applicatoins.
-> Open videos on YouTube.
-> Search for some text on Wikipedia and get summary.
-> Take a screenshot.
-> Write text in file and save it.
"""

import speech_recognition as sr # to recognize voice from microphones
import pyttsx3                  # for text to speech conversion
import pywhatkit                # for playing videos on youtube
import datetime 
import wikipedia                # to seach on wikipedia
import pyjokes                  # to get jokes
import os
import pyautogui

listener = sr.Recognizer()

engine = pyttsx3.init()
engine.setProperty('rate', 125)              # chnage the voice speed.
engine.setProperty('voice', 'english_rp+f3') # change the voice from male to female.

def speak(message):
    engine.say(message)
    engine.runAndWait()

def listenToCommand():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
            
            return command
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def runAlexa():
    command = listenToCommand()
    if command != None:
        if 'play' in command:
            song = command.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'open' in command:
            app = command.replace('open', '')
            speak("opening " + app)
            os.system(app)
        elif 'type' in command:
            text = command.replace('type', '')
            with open("notes.txt", 'w') as f:
                f.write(text)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            speak(f"Current time is {time}")
        elif 'date' in command:
            date = datetime.datetime.now().strftime("%A %d %B %Y")
            print(f"Today is {date}")
            speak(f"Today is {date}")
        elif 'joke' in command:
            speak(pyjokes.get_joke())
        elif 'tell me about' in command:
            req = command.replace('tell me about', '')
            info = wikipedia.summary(req, 1)
            print(info)
            speak(info)
        elif 'take a screenshot as' in command:
            imageName = command.replace('take a screenshot as', '')
            speak("Taking a screenshot")
            pyautogui.screenshot(f"{imageName}.png")
        else:
            speak("Please say the command again")
    else:
        speak("You didn't say any thing.")

while True:
 runAlexa()