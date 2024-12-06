import speech_recognition as sr
import webbrowser
import pyttsx3
import pocketsphinx


recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak(" i am Terminator T109, now its time to destroy this world boom")
