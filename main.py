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
    engine.setProperty('voice', voices[1].id)
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
        pystarks_speak("My name is PyStarks")
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
        stories = ["When I was little, I would go on Nickelodeon.com all the time and they had this game similar to Club Penguin, except it was called Nicktropolis. And if you forgot your password, a security question you could choose was “What is your eye color?” and if you got it right it’d tell you your password. So I would go to popular locations in Nicktropolis and write down random usernames who were also in those areas, and then I would log out and type in the username as if it were my own and see which of these usernames had a security question set to “What is your eye color?” (Which was most of them, since it was easy and we were all kids). I would then try either brown, blue, or green, and always get in, then I would go to their house and send all of their furniture and decorations to my own accounts. And if I didn’t want it, I could sell it for money.",

        "So a couple years I moved out of state with a boyfriend. Was super excited about it but with reason had anxiety about being so far from friends and family. One of the ways my anxiety was coming out was with nightmares and night terrors. I’d wake up violently sitting up in a cold sweat, gasping and whatnot. On one particular night I had woken up the sound of our doorbell ringing. Which at 4 in the morning is fucking nerve wracking. So I shook my boyfriend fully awake and told him I heard the doorbell and to go check it because I was scared. He quickly jumps up. Puts on clothes and grabs a bat. Goes all the way to the front door and opens it. I, scared shitless, am peeking around the corner watching it all go down. I see him step outside and I nervously await the verdict of the situation when I hear him call out to me. “Babe?” And I respond real shaky, “Yes?” He stands in the doorway with a real frustrated tired look in his eyes and says, 'We don’t have a fucking doorbell.'"]
        pystarks_speak(f"Okay. {random.choice(stories)} Thank you for listening.")
    if "play me a song" in voice_data:
        pystarks_speak("Okay, sit back, relax, enjoy, and let me select a song for you")
        names = []
        for song in os.listdir('C:\\Users\Aser\\Music\\'):
            splitted = song.split('.')
            if splitted[-1] == "mp3":
                names.append(song)
        os.system(f"start C:\\Users\\Aser\\Music\\{random.choice(names)}")
        exit()

    if 'search something' in voice_data:
        search_google = record_audio("What do you want to search for?")
        url = "https://google.com/search?q=" + search_google
        webbrowser.get().open(url)
        pystarks_speak("Here is what I found for "+search_google)
    if 'video' in voice_data:
        search_youtube = record_audio("I can only get videos for you on Youtube. So what video do you want to watch on Youtube?")
        url = "https://www.youtube.com/results?search_query=" + search_youtube
        webbrowser.get().open(url)
        pystarks_speak("Here are the videos I found for "+search_youtube)
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
while True:
    voice_data = record_audio()
    respond(voice_data)