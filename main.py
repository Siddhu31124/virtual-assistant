import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer= sr.Recognizer()
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("opened google on your request")
    

if __name__=="__main__":
    name_of_commender=input()
    speak("buji Activeted.....")
    while True:
        #listen for name buji
        # obtain audio from the microphone
        r = sr.Recognizer()
       
        print("recognizing...")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...!")
                audio = r.listen(source,timeout=2 ,phrase_time_limit=1)
            word_to_activate_bujji=r.recognize_google(audio)
            if (word_to_activate_bujji.lower()=="bujji"):
                speak(f"Yes {name_of_commender} how can i help you")
            #Listening for Command
                with sr.Microphone() as source:
                    print("Waiting for command...!")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    process_command(command)
                

        except Exception as e:
            print("Error; {0}".format(e))
