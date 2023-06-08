import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib  # due to this pakage we can send email thru our email
import pywhatkit  # this module used for searchin results on google
import pyautogui  # this module needed for screen shot
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Diction

from intro import play_gif

play_gif

machine = pyttsx3.init('sapi5')  # this is used to take voices
voices = machine.getProperty('voices')
# print(voices[1].id)   #have two voices one male and one female
machine.setProperty('voice', voices[0].id)
machine.setProperty("rate", 150)  # rate with which jarvis speaks


def speak(audio):
    machine.say(audio)  # so us audio ko engine bolega
    machine.runAndWait()  # runandwait ek function hai


def wishuser():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 18:
        speak('good afternoon')
    else:
        speak('good Evening!')
    speak('i am jarvis sir,plz tell me how may i help you')


def tell():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()  # class bana diya
    with sr.Microphone() as source:  # isko source bna diya
        print("listening")
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        # r.energy_threshold = 100 ## minimum audio energy to consider for recording
        audio = r.listen(source)

    try:
        print('recognizing')
        query = r.recognize_google(audio,
                                   language='en-in')  # thus function is taking an audio and just returning it into a
        # string
        print(f'user said: {query}\n')
        # speak(f'user said: {query}\n')

    except Exception as e:
        # print(e)
        print('say that again please...')
        return "None"
    return query


def openApps():
    speak("sir ,wait for a while ")

    # if wanna open any site  so webbrowser is needed (webbrowser needed for seaching website)
    if "open youtube" in query:
        webbrowser.open('youtube.com')

    elif "open google" in query:
        webbrowser.open('google.com')

    elif "open spotify" in query:
        webbrowser.open('spotify.com')

    elif "open whatsapp" in query:
        webbrowser.open("web.whatsapp.com")

    elif "open stackoverflow" in query:
        webbrowser.open('stackoverflow.com')

    elif "open facebook" in query:
        webbrowser.open("Facebook.com")

    elif "open instagram" in query:
        webbrowser.open("instagram.com")

    elif "maps" in query:
        webbrowser.open("googlemaps.com")

    speak("sir, your website is opened")


def YoutubeAuto():  # for youtube automation

    speak("sir,plz tell your command")
    command = tell()

    if "pause" in command:
        keyboard.press('space bar')

    elif "restart" in command:
        keyboard.press('0')

    elif "skip" in command:
        keyboard.press('l')

    elif "back" in command:
        keyboard.press('j')

    elif "full screen" in command:
        keyboard.press('f')

    elif "film mode" in command:
        keyboard.press('t')

    speak("your work in done sir")


# automating chrome
def chromeauto():
    speak("sir,plz tell your command")
    command = tell()

    if "close this tab" in command:
        keyboard.press_and_release("ctrl+w")  # we have to click these simulataneously

    elif "open new tab" in command:
        keyboard.press_and_release("ctrl+t")

    elif "zoom out" in command:
        keyboard.press_and_release("ctrl+ -")

    elif "select everything on page" in command:
        keyboard.press_and_release("ctrl+ a")

    elif "download page in new tab" in command:
        keyboard.press_and_release("ctrl+j")

    elif "open browser window" in command:
        keyboard.press_and_release("ctrl+n")

    elif "refresh the page" in command:
        keyboard.press_and_release("ctrl+r")

    elif "history" in command:
        keyboard.press_and_release("ctrl+h")

    speak("your work is done sir")


def send_Email(to, subject, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port ie (host,port)
    f1 = open("email.txt", "r")  # keep password if possible in textfile for security reason
    f2 = open('password.txt', "r")
    sender_email = f1.read()
    password = f2.read()
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    message = f'subject:{subject}\n\n{content}'
    server.sendmail("yashaher481@gmail.com", to, message)
    server.close()


# dictionary
# using pydictionary will get the meaning of any word
# if we give input in form ( jarvis what is the meaning/synonym/antonym of {word})

def dict():  ##################################
    speak("activated dictionary")
    speak("tell me the problem")
    problem = tell()

    if "meaning" in problem:
        problem = problem.replace("what is the", "")
        # problem=problem.replace("jarvis","")
        problem = problem.replace("meaning of", "")
        result = Diction.meaning(problem)
        print(result)
        speak(f"THe Meaning for {problem} is {result}")

    if "synonym" in problem:  #######################
        problem = problem.replace("what is the", "")
        # problem=problem.replace("jarvis","")
        problem = problem.replace("synonym of", "")
        result = Diction.synonym(problem)
        print(result)
        speak(f"THe Meaning for {problem} is {result}")

    if "antonym" in problem:  #####################
        problem = problem.replace("what is the", "")
        # problem=problem.replace("jarvis","")
        problem = problem.replace("antonym of", "")
        result = Diction.antonym(problem)
        print(result)
        speak(f"THe Meaning for {problem} is {result}")

    speak("exited dictionary")


if __name__ == "__main__":
    speak("our group consists 3 members")
    wishuser()
    while True:
        query = tell().lower()  # as queries can be reduced
        # logic for executing task
        if "wikipedia" in query:
            speak('searching wikipedia')
            query = query.replace('wikipedia',
                                  "")  # wiki.. replaced by blank so that the remaining part is searched by jarvis
            results = wikipedia.summary(query, sentences=5)  # (kya search kiya,kitna sentence ki info milegi)
            speak('according to wikipedia')
            print(results)
            speak(results)

        # opening some of the websites
        elif "open youtube" in query:
            openApps()

        elif "open google" in query:
            openApps()

        elif "open spotify" in query:
            openApps()

        elif "open whatsapp" in query:
            openApps()

        elif "open stackoverflow" in query:
            openApps()

        elif "open facebook" in query:
            openApps()

        elif "open instagram" in query:
            openApps()

        elif "maps" in query:
            openApps()


        # opening youtube and searching what we want
        elif "youtube search" in query:
            speak("ok sir,with the following info i can help you")
            query = query.replace("jarvis",
                                  "")  # so will replace jarvis and youtube search so that they will not be in our
            # search
            query = query.replace("youtube search", "")
            web = "https://www.youtube.com/results?search_query=" + query  # so if we see on yotube when we seach so
            # it comes after this string hence added query to that
            webbrowser.open(web)
            speak('sir your work is done')

            # opening google and searching what we want
        elif "google search" in query:
            speak("hello sir , i got this for what you seached")
            query = query.replace("jarvis", "")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            speak("your work is done sir")

        # way to open a website
        elif "launch website" in query:
            speak("sir plz tell the name of website")
            name = tell()  # so jarvis will take command from user
            web = "https://www." + name + ".com"
            webbrowser.open(web)
            speak("sir, your work is done")

            # os module require to open any application available on dexstop
        elif "open code" in query:
            codepath = "C:\\Users\\SAMRUDDHI ANIL AHER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        # if wanna ply music so os module used
        elif 'play music' in query:
            music_dir = "music,py"
            songs = os.listdir(music_dir)
            print(songs)
            A = random.randint(0, 2)
            os.startfile(os.path.join(music_dir, songs[A]))  # ie 1st song will play

        # if we want to know the time
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(strTime)

        # to send email
        # see how to use that dic part
        elif "send mail" in query:
            try:  # try and except as if problem comes
                speak("what should i speak")
                content = tell()  # hamne jo khuch bhi bola hai vo hame string ke format me return krta hai take command
                f = open("emailto.txt", "r")
                to = f.read()
                subject = tell()
                send_Email(to, subject, content)
                speak('succesfully email sended')
            except Exception as e:
                print(e)  # printed error as will get to know what is error
                speak("plz try again mail not sended")

        # if want to take screenshot
        elif "screenshot" in query:
            ss = pyautogui.screenshot("screenshot.png")
            # ss.save("screenshot.txt")      #screen shot will be saved in that file  and if we do it multiple times so
            # next image ill be replaced by the older one in that file
            speak("sir screenshot taken")

        # if want to click photo
        elif "click my photo" in query:  # so due to this it will say smile and will click photo
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(2)  # will delay or sleep it for 2 sec
            speak("SMILE")
            pyautogui.press("enter")

        # for automating youtube
        elif "youtube start" in query:  # this function every time we need to call for a ny command
            YoutubeAuto()  # so if we directly also call command it will work directly as wrote below also

        if "pause" in query:
            keyboard.press('space bar')

        elif "restart" in query:
            keyboard.press('0')

        elif "skip" in query:
            keyboard.press('l')

        elif "back" in query:
            keyboard.press('j')

        elif "full screen" in query:
            keyboard.press('f')

        elif "film mode" in query:
            keyboard.press('t')

            # for automating chrome
        elif "google start" in query:  # this function every time we need to call for any command
            chromeauto()  # so if we directly also call command it will work directly as wrote below also

        elif "close this tab" in query:
            keyboard.press_and_release("ctrl+w")  # we have to click these simulataneously

        elif "open new tab" in query:
            keyboard.press_and_release("ctrl+t")

        elif "zoom out" in query:
            keyboard.press_and_release("ctrl+ -")

        elif "download page in new tab" in query:
            keyboard.press_and_release("ctrl+j")

        elif "select everything on page" in query:
            keyboard.press_and_release("ctrl+a")

        elif "open browser window" in query:
            keyboard.press_and_release("ctrl+n")

        elif "refresh the page" in query:
            keyboard.press_and_release("ctrl+r")

        elif "history" in query:
            keyboard.press_and_release("ctrl+h")

            # joke will be told by jarvis
        elif "joke" in query:
            j = pyjokes.get_joke()
            speak(j)

        # my word repetition ie it will repeat what user will say
        elif "repeat my words" in query:
            speak("sir plz do speak")
            l = tell()
            speak(f"you said:{l}")

        elif "dictionary" in query:  ###############
            dict()

        # to quit 
        elif "quit" in query:
            exit()
