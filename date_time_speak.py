import pyttsx3
from datetime import datetime
engine=pyttsx3.init()
a=datetime.now()
d=datetime.today()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def speak_date():
    b=datetime.strftime(d,"%d %B %Y")
    speak(b)
def speak_time():
    b1=datetime.strftime(a,"%I %M %p")
    speak(b1.lstrip('0')) 
