import speech_recognition as sr
import pyttsx3
import wikipedia

import datetime
# import pywhatkit
# import PyAudio
ass_Name = "alexa"


listener = sr.Recognizer()
engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("This is Adeyemi's Voice Assistant")
            print("listening....")
            print("Please speak now!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            # talk("This is Adeyemi's Voice Assistant called snow")
            talk("i do not know the time, just joking! fetching current time")
            if "snow" in command:
                # talk("This is Adeyemi's Voice Assistant called snow")
                # talk("what would you like me to do")
                command = command.replace('snow', '')
                print(command)
                return command

    except:
        pass


def run_snow():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace('play', "")
        # pywhatkit.play

        talk("playing" + song)
        # talk("playing " + song)
        print(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I: %M %p')
        talk("current time is " + time)
        print(time)

    elif "what is" in command:
        # 'wikipedia' in command or "who is" in command or
        person = command.replace("what is", '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)


    else:
        talk("did you say " + command)


run_snow()
# take_command()


