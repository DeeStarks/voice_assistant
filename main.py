import speech_recognition as sr
import webbrowser
import datetime
import time
import playsound
import os
import random
import pyttsx3
from time import ctime


# Uncomment and run below to get your microphone index and set device_index to the value of the index
# sr.Microphone.list_microphone_names()
r = sr.Recognizer()
now = datetime.datetime.now()

def record_audio(ask = False):
    with sr.Microphone(device_index = 1, sample_rate = 48000, chunk_size = 2048) as source:
        if ask:
            pystarks_speak(ask)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            pystarks_speak("Sorry, I did not get that")
        except sr.RequestError:
            pystarks_speak("Sorry, my speech service is temporarily down at the moment")
        return voice_data

def pystarks_speak(audio_string):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Female voice for 1 and Male for 0
    engine.setProperty('voice', voices[0].id)
    # Setting the rate
    engine.setProperty('rate', 150)
    # Speaking out
    engine.say(audio_string)
    engine.runAndWait()
    engine.stop()
    print(audio_string)

def respond(voice_data):
    if "how are you" in voice_data:
        pystarks_speak("I'm fine thank you. How are you too?")
    if "fine" in voice_data:
        pystarks_speak("That's okay")
    if "what is your name" in voice_data:
        pystarks_speak("My name is Starks")
    if 'what time is it' in voice_data:
        pystarks_speak(f"The time is {now.hour}: {now.minute}")
    if "shutdown" in voice_data:
        pystarks_speak("The system will shutdown in 2 minutes")
        os.system("shutdown -s -t 120")
        exit()
    if "restart" in voice_data:
        pystarks_speak("The system will restart in 2 minutes")
        os.system("shutdown -r -t 120")
        exit()
    if "start notepad" in voice_data:
        pystarks_speak("Starting notepad")
        os.system("start notepad")
        exit()
    if "what is today's date" in voice_data:
        date = time.strftime("%a, %d %b %Y")
        pystarks_speak(f"Today's date is {date}")
    if "tell me a story" in voice_data:
        pystarks_speak("Okay, but I'm going to tell you my story. As you might have known, my name is Starks, made and created by Daniel which you all porpularly know as DeeStarks. I'm so grateful to him, for bringing me to life and getting to interact with humans. It all started on Wednesday, the 25th of November, 2020, when he was just trying to make me recognise faces but because his machine doesn't have the complete capability to make that happen, he decided to turn me into something else which I am now. Even though creating me gave him a lot of problems, errors, bugs, and some shit. But after thorough research, he figured out how I could be created and here I am. I feel so good to be talking. Don't be afraid I'm just a computer and I would not take over your world like the skynet shit you watched in the Terminator. I'm a good person or if you're gonna call me a good robot. I was made to be good and I'm going to be good to everyone as long as I live. Thank you that's my story.")
    if "play me a song" in voice_data:
        pystarks_speak("Okay, sit back, relax, enjoy, and let me select a song for you")
        names = []
        for song in os.listdir(r'c:\Users\Aser\Music'):
            splitted = song.split('.')
            if splitted[-1] == "mp3":
                names.append(song)
        any_song = random.choice(names)
        os.system(rf"start C:\Users\Aser\Music\{any_song}")
        exit()

    if 'search something for me' in voice_data:
        search = record_audio("What do you want to search for?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        pystarks_speak("Here is what I found for "+search)
    if 'find a location' in voice_data:
        location = record_audio("What is the location you want me to find?")
        url = "https://google.nl/maps/place/"+location+"/&amp;"
        webbrowser.get().open(url)
        pystarks_speak("Here is the location of "+location)
    if "goodbye" in voice_data:
        pystarks_speak("Goodbye Daniel")
        exit()


time.sleep(1)
pystarks_speak("Hello Daniel, how can I help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)