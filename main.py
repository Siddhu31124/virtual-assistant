import speech_recognition as sr
import webbrowser
import pyttsx3
import date_time_speak
import requests
engine=pyttsx3.init() 
newsapi="0858f100a95f4a7cbc37c9c68be5009e"
def speak(text):
    engine.say(text)
    engine.runAndWait()
def process_command(c):
    list_c=c.split()
    broswer_name=list_c[1]
    link=f"https://{broswer_name}.com"
    if "open" in c.lower():
        webbrowser.open(link)
        speak(f"opening {broswer_name} on your request")
    elif "date" in c.lower():
        speak("today date is")
        date_time_speak.speak_date()
    elif "time" in c.lower():
        speak("time is")
        date_time_speak.speak_time()
    elif "tell" in c.lower() or "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            counter=0
            speak("How many headlines do you want about")
            no_of_headlines=int(input("How many headlines in todays news"))
            speak("today date is")
            date_time_speak.speak_date()
            speak("Todays headline are ")
            if no_of_headlines>10:
                no_of_headlines=10
            for article in articles:
                speak(article['title'])
                counter+=1
                if(counter>no_of_headlines):
                    break
        else:
            speak("Sorry, I couldn't fetch the news at the moment.")

    elif "who is" in c.lower() or "what is" in c.lower():
        speak("Please enter name about what you want to search")
        searchInput=input("Enter the name :")
        a=f"https://apis.ccbp.in/wiki-search?search={searchInput}"
        info=requests.get(a)
        if info.status_code == 200:
            data=info.json()
            d=data.values()
            for i in d:
                speak(f"How many articles do you want about {searchInput}")
                no_of_articles=int(input(f"How many articles do you want about {searchInput} :"))
                counter=0
                if no_of_articles>20:
                    no_of_articles=20
                for j in i:
                    if counter<no_of_articles:
                        speak(j['description'])
                        counter=counter+1
                    else:
                        break
        else:
            speak("Data not found")
    else:
        speak("Sorry I can perform some limited commands only like opening a web browser, telling date,time and news")
    

if __name__=="__main__":
    name=input("Your Name please: ")
    speak(f"Hello {name} how are you doing")
    print("If you want to give any commands, Say Alexa to Activate it")
    print("If you want to exit the code say See you alexa")
    stop_the_loop=0
    while True:
        if stop_the_loop<10:
            r = sr.Recognizer()
            try:
                print("Listening....!")
                with sr.Microphone() as source:
                    audio = r.listen(source,timeout=2 ,phrase_time_limit=2)
                word_to_activate_alexa=r.recognize_google(audio)
                if (word_to_activate_alexa.lower()=="alexa"):
                    stop_the_loop=0
                    speak(f"alexa Activeted , Yes {name} how can i help you")
                    with sr.Microphone() as source:
                        print("Waiting for command...!")
                        audio=r.listen(source)
                        command=r.recognize_google(audio)
                        process_command(command)
                elif (word_to_activate_alexa=="see you Alexa") :
                    speak(f"Bye {name},hava a nice day")
                    break
                else:
                    speak("Invalid wake up note")
            except Exception as e:
                stop_the_loop+=1
        else:
            speak(f"Since a while,You have not given any command,So i am Signning off. have a nice day{name}")
            break
