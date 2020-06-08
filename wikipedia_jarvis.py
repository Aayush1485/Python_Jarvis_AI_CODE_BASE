import pyttsx3
import wikipedia
import speech_recognition as sr


def speak(audio):
    Engine=pyttsx3.init()
    Engine.setProperty("rate",160)
    Engine.say(audio)
    Engine.runAndWait()

def greetMe():
    string = "Hey this is Jarvis here ,Your AI assistant Let me know How may i help you "
    speak(string)

def takeCommand():
    r=sr.Recognizer()   
    with sr.Microphone() as source:
        print("Listening.....")
        query_result=r.listen(source)
        r.pause_threshold = 1
        query_result=r.recognize_google(query_result)
        speak(query_result)
        return query_result




if __name__ == "__main__":
    greetMe()
while True:
    Keyword=takeCommand().lower()
    print(Keyword)
    if 'wikipedia' in Keyword:
      speak("Searching....")
      Keyword=Keyword.replace("wikipedia"," ")#not understand for now why we replacing here wikipedia here
      query_result=wikipedia.summary(Keyword,sentences =10)
      print(query_result)
      speak(query_result)
    elif 'offline' in Keyword:
        quit()
