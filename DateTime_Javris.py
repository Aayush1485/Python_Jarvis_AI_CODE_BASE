import datetime
import pyttsx3

def init(audio):
    Engine=pyttsx3.init()
    Engine.setProperty('rate',150)
    Engine.say(audio)
    Engine.runAndWait()
    # return

def Time():
    Time=datetime.datetime.now()
    print(Time)
    Time=Time.strftime("%H:%M:%S")
    init(Time)
    Hour=datetime.datetime.now().strftime("%H")
    Hour=int(Hour)
    if Hour<=11:
      init("I should Wish You Good Morning Sir")
    elif Hour>=12:
      init("I should Wish You Good Afternoon Sir")
    elif Hour>=5 :
      init("I should Wish You Good Evening Sir")


    
# Time()    

def Date():
    Date=datetime.datetime.now()
    Date=Date.strftime("%m:%d:%Y")
    init(Date)

def Year():
 year = datetime.datetime.now()
 year = year.strftime("%Y")
 init(year)


def WishMe():
    init("Hello Sir, this is Jarvis your AI assistant")   
    init("the current time is")
    Time()
    init("The Current Date is")
    Date()
    init("The Current Year is")
    Year()
    init ("Let Me know How May i help you ")    


# Date()
WishMe()    