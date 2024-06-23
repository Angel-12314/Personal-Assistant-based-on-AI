#from importlib.metadata import PackageNotFoundError
from unicodedata import category
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import wolframalpha

engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
     engine.say(audio)
     engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12: 
        speak("Good   morning ")   
    elif hour >=12 and hour<15:
        speak("Good   afternoon ")
    elif hour >=15 and hour<=18:
        speak("Good    evening ")  
    elif hour>=18 and hour <=24:
        speak("Good   night ")
        
    speak("i   am   jaarwiz,    how   can   i   help you?")
              
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....,")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
    
    try:
        print("Recognizing......,")
        query=r.recognize_google(audio,language='en-in')
        print("my boss said!",query)
    

    
    except Exception as e:
        print(e)
        speak("please,  say    that      again")
        query="nothing"
    return query
print("Loading your AI personal assistant ")
speak("Loading your AI personal assistant ")
wishme()

if __name__=='__main__':
     #wishme()
            
  
         while True:
            query=takecommand().lower()
            if query==0:
                continue

            if'bye'in query or'exit'in query or'quit'in query:
                speak("goodbye")
                break
            

            if "wikipedia" in query:
           
                speak("searching in wikipedia")
                query=query.replace("search in wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)



            elif 'open youtube' in query:
             speak("opening  youtube")
             webbrowser.open("youtube.com")
             
            elif'open google' in query:
             speak("opening  google  browser")
             webbrowser.open("google.co.in") 

            elif 'open stack overflow' in query:
             speak("opening  stackflow")
             webbrowser.open("stackoverflow.com")

            elif'open twitter' in query:
             speak("opening  twitter")
             webbrowser.open("https://twitter.com/?lang=en-in")

            elif'open facebook'in query:
             speak("opening  facebook")
             webbrowser.open("https://www.facebook.com/?_rdc=1&_rdr") 

            elif'open instagram'in query:
             speak("opening  instagram, have fun")
             webbrowser.open("https://www.instagram.com/")

            

            elif'open spotify' in query:
             speak("opening spotify, get chill and relax with songs")
             webbrowser.open("https://open.spotify.com/")    

            elif'play songs' in query:
                musicdir="F:\\songs"
                songs=os.listdir(musicdir)
                os.startfile(os.path.join(musicdir,songs[4]))

            elif'open movies' in query or 'play movies' in query:
                moviedir="F:\\movies"
                movie=os.listdir(moviedir)
                os.startfile(os.path.join(moviedir,movie[1]))

            elif 'ask' in query:
             speak('I can answer to computational and geographical questions  and what question do you want to ask now')
             question=takecommand().lower()
             app_id="3YW6A7-L94G8X9937"
             #app_id="JY6V5Y-KELVY6J8TR"
             #client = wolframalpha.Client('JY6V5Y-KELVY6J8TR')
             client = wolframalpha.Client('3YW6A7-L94G8X9937')
             res = client.query(question)
             answer =next(res.results).text
             speak(answer)
             print(answer)


            elif'open vs code' in query:
                codepath="C:\\Users\\Harikrishnan.R\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)

            elif 'open ac game' in query:
                path="F:\\Assassins.Creed.II.v1.01.REPACK-KaOs\\AssassinsCreedIIGame.exe"
                os.startfile(path)

            elif'open Ms word' in query:
                path1="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"    
                os.startfile(path1)

            elif'open ms powerpoint' in query:
                path2="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"""
                os.startfile(path2) 

            elif'open ms excel' in query:
                path3="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"""
                os.startfile(path3) 

            elif'open whatsapp' in query:
                path4="C:\\Users\\\Harikrishnan.R\\AppData\\Local\\WhatsApp\\WhatsApp.exe" 
                os.startfile(path4)

            elif'open chrome' in query:
                path5="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe""" 
                os.startfile(path5)       

            elif'the time' in query:
                time=datetime.datetime.now().strftime("%H:%M:%S")
                print(time)
                speak("the  time is")
                speak(time) 
                speak("good  luck ") 

            elif'the date' in query:
                date=datetime.date.today()
                print(date)
                speak("the date is ")
                speak(date)
                speak("Have     a      nice    day")

            elif'a joke' in query or 'another joke' in query or 'more jokes' in query:
                joke=pyjokes.get_joke(language='en', category='all')
                print(joke)
                speak(joke)
