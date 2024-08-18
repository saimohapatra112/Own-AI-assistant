import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe() :
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good afternoon!")

    else:
        speak("Good evening!")

    speak("This is Sai's personal A.I. . Please tell me how may I help you")

def takecommand():

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio= r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    while True:
        query=takecommand().lower()

        if 'wikipedia' in query:
          speak('Searching wikipedia...')
          query = query.replace("wikipedia","")
          results= wikipedia.summary(query, sentences=100)
          speak("According to wikipedia")
          print(results)
          speak(results)

        elif 'open youtube' in query:
            print("opening youtube....")
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'google' in query:
            print("opening browser....")
            speak("opening browser")
            codePath=r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
            os.startfile(codePath)
            # webbrowser.open("google.com")
        elif 'chrome' in query:
            print("opening browser....")
            speak("opening browser")
            codePath=r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
            os.startfile(codePath)
        elif 'word' in query:
            print("opening word....")
            speak("opening word")
            codePath=r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
            os.startfile(codePath)
        elif 'store' in query:
            print("ok..\U0001F60A")
            webbrowser.open("apps.microsoft.com")
        elif 'instagram' in query:
            webbrowser.open("www.instagram.com")
        elif 'music' in query:
            webbrowser.open("https://open.spotify.com/playlist/6wl5UoqgZY5vh8upo652At?si=0e3efd9ca3c347ca")
        elif 'how are you' in query:
            print("I am good What about you?")
            speak("I am good what about you") 
        elif 'hello' in query:
            print("Hii \U0001F603!")
            speak("Hi ")
        elif 'fine' in query:
            print("That's so cool \U0001F60A!")
            speak("That's so cool")
        
        elif 'good morning' in query:
            print("Good morning, Sai \U0001F601! Hope you have a good day today!!")
            speak("Good morning Sai Hope you have a good day today")
        elif 'open code' in query:
            codePath="C:\\Users\\mohap\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'hi there what\'s up' in query:
            print("Not Much, How's your day going?")
            speak("Not Much, How's your day going")
        elif 'good evening' in query:
            print("Good evening \U0001F31C")
            speak("Good evening")
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'what about you' in query:
            print("Nothing much, Today I am glad here to help you..")
            speak("Nothing much, Today I am glad here to help you")
        elif 'how is your mood today' in query:
            print("I am feeling happy \N{grinning face}")
            speak("I am feeling happy")
        elif 'nice' in query:
            print("Thank you \U0001F60A")
            speak("Thank you")
        elif 'bye' in query:
            exit()
       
        else:
            print("Sorry, I didn't get you!")
            speak("Sorry I didn't get you")
             