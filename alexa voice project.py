import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[-1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    pass
    try:
        with sr.Microphone() as source:
            print("listening.....")
            listener.adjust_for_ambient_noise(source)
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace("alexa","")
                print(command)
            else:
                print("sorry")
    except:
        pass
    return command
def rn_alexa():
    command=take_command()
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song) 
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Zain! Current time is ' + time)
    elif 'are you single' in command:
        talk('No Zain! I am in a relationship with wifi')
    elif 'tell me about' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'ok close' in command:
        quit()
    elif 'feeling bad' in command:
        talk('Eat panadol')
    elif 'thanks' in command:
        talk('zain,no problem')
    elif 'friend' in command:
        talk('hey zain friend,how are you')
    elif 'good' in command:
        talk('ok thats good')
    elif 'brother' in command:
        talk('hey ali, how are you')
    elif 'love' in command:
        talk('Sorry! i like nawaz shareef noon league zindabad')
    elif 'imran' in command:
        talk('keep quite')
    else:
        talk('Please say the command again.')
while True:
    rn_alexa()
