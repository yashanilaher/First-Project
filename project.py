#project
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import keyboard
import pyautogui
import smtplib


engine=pyttsx3.init("sapi5")   #this is used to take voices
voices=engine.getProperty("voices")
# it contains two voices one male and one female
engine.setProperty("voice,voices[0].id)
engine.setProperty("rate",150)   #rate with which jarvis speaks


def speak(audio):
    engine.say(audio)     #this audio will be said by engine for that runAndWait() function is used
    engine.runAndWait()
                   
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<12:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis. tell me how i can help you")
                   
def takecommand():
    #it takes our voice from microphone as input and return in the form of string output
    r=sr.Recognizer()
    with sr.microphone() as source:
        print("listening")
        r.pause_threshold=1   #seconds of nonspeaking audio before a phrase is considered complete
        audio=r.listen(source)
    try:
        print("recognizing")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said: {query}\n")
        speak(f"user said: {query}\n")
    except Exception as e:
        print("say that again please....")
        return "none"
    return query
def openApps():
    speak("sir wait for a while")               
    if "open youtube" in query:
        webbrowers.open('youtube.com')               
    elif "open google" in query:               
        webbrowers.open('google.com')
    elif "open spotify" in query:               
        webbrowers.open('spotify.com')
    elif "open whatsapp" in query:               
        webbrowers.open('web.whatsapp.com')           
    elif "open stackoverflow" in query:
        webbrowers.open('stackoverflow.com')
    elif "open facebook" in query:
        webbrowers.open('facebook.com')
    elif "open instagram" in query:
        webbrowers.open('instagram.com')
    elif "open googlemap" in query:
        webbrowers.open('googlemaps.com')
    elif "open flipkart" in query:
        webbrowers.open('www.flipkart.com')
    elif "open amazon" in query:
        webbrowers.open('www.amazon.in')
    elif "open netflix" in query:
        webbrowers.open('www.netflix.in')
                   
    speak("sir, your website is opened")               
 def YoutubeAuto():     #for youtube automation
     speak("sir,plz tell your command")
     command=takecommand()
     
     if "pause" in command:
         keyboard.press('space bar')
     elif "restart" in command:
         keyboard.press('0')
     elif "skip" in command:
         keyboard.press('1')
     elif "back" in command:
         keyboard.press('j')
     elif "full screen" in command:
         keyboard.press('f')
     elif "film mode" in command:
         keyboard.press('t')
     speak("your work is done sir")
                   
 def send_Email(to,subject,content):
    server=smtplib.SMTP("smtp.gmail.com",587)   #587 is a port ie (host,port)
    f1=open("email.txt","r")  #keep password if possible in textfile for security reason
    f2=open('password.txt',"r")
    sender_email=f1.read()
    password=f2.read()
    server.ehlo()
    server.starttls()
    server.login(sender_email,password)    
    message=f'subject:{subject}\n\n{content}'
    server.sendmail("yashaher481@gmail.com",to,message)
    server.close()                  
                   
                   
if __name__=="__main__":
    speak("our group consists 3 members")
    wishme()
    while True:
        query = takecommand().lower()
        #if we want to play music so os module used
        if "play music" in query:
            music_dir="music,py"
            songs=os.listdir(music_dir)
            print(songs)
            A = random.randint(0,2)
            os.startfile(os.path.join(music_dir,songs[A]))
        elif "wikipedia" in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia","") #wikipedia replaced by blank so that the remaining part is searched by jarvis
            result=wikipedia.summary(query,sentence=5) #kya search kiya,kitne sentence in info milegi  
            speak("according to Wikipedia")
            print(result)
            speak(result)
        elif "youtube search" in query: #open youtube and searching what we want
            speak("ok sir,with the following info i can help you")
            query = query.replace("jarvis","") # so we will replace jarvis and YouTube search so that they will not be in our search
            query = query.replace("youtube search","")
            web = "https://www.youtube.com/result?search_query=" +query # so if we see on youtube when we search so it comes after this string hence added query to that
            webbrower.open(web)
            speak("sir your work is done")
        #if we want to know the time
                   
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(strTime)  
                   
        # to send email   #see how to use that dic wala part
        elif "send mail" in query:
            try:   #try and except as if problem comes
                speak("what should i speak")   
                content=takecommand() 
                f=open("emailto.txt","r")
                to=f.read()
                subject=takecommand()
                send_Email(to,subject,content)
                speak('succesfully email sended')
            except Exception as e:
                print(e)  #printed error as will get to know what is error    
                speak("plz try again mail not sended")           
                   
                   
        
            
