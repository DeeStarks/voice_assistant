import speech_recognition as sr
import webbrowser
import datetime
import time
import playsound
import os
import random
from gtts import gTTS
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
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 10000000)
    audio_file = 'audio'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if "how are you" in voice_data:
        pystarks_speak("I'm fine thank you. How are you too?")
    if "i am fine thank you" in voice_data:
        pystarks_speak("That's okay")
    if "what is your name" in voice_data:
        pystarks_speak("My name is Starks")
    if 'what time is it' in voice_data:
        pystarks_speak(f"The time is {now.hour}, {now.minute}")
    if "what is today's date" in voice_data:
        date = time.strftime("%a, %d %b %Y")
        pystarks_speak(f"Today's date is {date}")
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
    if "exit" in voice_data:
        pystarks_speak("Goodbye Daniel")
        exit()


time.sleep(1)
pystarks_speak("Hello Daniel, how can I help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)