import webbrowser as web
import pyttsx3
import speech_recognition as sr
import wikipedia as wk

def speak(audio):
    Engine=pyttsx3.init()
    Engine.setProperty("rate",160)
    Engine.say(audio)
    Engine.runAndWait()

def greetMe():
    String = "Hello Sir,Jarvis is at your service, how may i help you "
    speak(String)

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening ")
        querytoPrcocess=r.listen(source)
        r.pause_threshold=1
        query_result=r.recognize_google(querytoPrcocess)
        print(query_result)
        speak(query_result)
        return query_result

if __name__ == "__main__":
    greetMe()

    while True:
       query_result= TakeCommand().lower()
       if "search in chrome" in query_result:
           speak("What should i search ")
           chromePath ='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
           query_result=TakeCommand().lower()
           web.get(chromePath).open_new_tab(query_result+".com")
                    
       elif "search on wikipedia" in query_result:
           Engine=pyttsx3.init()    
           Engine.setProperty("rate",120)
           Engine.say("What should i search on wikipdeia sir")
           Engine.runAndWait()
           query_result=TakeCommand().lower()
           fetched_data =wk.summary(query_result,sentences = 5)
           print(fetched_data)
           speak(fetched_data)


       elif 'offline' in query_result:
           quit()

