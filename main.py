import speech_recognition as sr
import webbrowser
import datetime
import time
import playsound
import os
import random
import pyttsx3
from time import ctime
import ctypes
from ctypes import wintypes as w
import pyautogui


# Uncomment and run below to get your microphone index and set device_index to the value of the index
# sr.Microphone.list_microphone_names()
r = sr.Recognizer()
now = datetime.datetime.now()

class Voice_Assistant():
    def __init__(self):
        self.name = ''
        self.voice_data = ''
        self.stories = ["When I was little, I would go on Nickelodeon.com all the time and they had this game similar to Club Penguin, except it was called Nicktropolis. And if you forgot your password, a security question you could choose was “What is your eye color?” and if you got it right it’d tell you your password. So I would go to popular locations in Nicktropolis and write down random usernames who were also in those areas, and then I would log out and type in the username as if it were my own and see which of these usernames had a security question set to “What is your eye color?” (Which was most of them, since it was easy and we were all kids). I would then try either brown, blue, or green, and always get in, then I would go to their house and send all of their furniture and decorations to my own accounts. And if I didn’t want it, I could sell it for money.",

        "So a couple years I moved out of state with a boyfriend. Was super excited about it but with reason had anxiety about being so far from friends and family. One of the ways my anxiety was coming out was with nightmares and night terrors. I’d wake up violently sitting up in a cold sweat, gasping and whatnot. On one particular night I had woken up the sound of our doorbell ringing. Which at 4 in the morning is fucking nerve wracking. So I shook my boyfriend fully awake and told him I heard the doorbell and to go check it because I was scared. He quickly jumps up. Puts on clothes and grabs a bat. Goes all the way to the front door and opens it. I, scared shitless, am peeking around the corner watching it all go down. I see him step outside and I nervously await the verdict of the situation when I hear him call out to me. “Babe?” And I respond real shaky, “Yes?” He stands in the doorway with a real frustrated tired look in his eyes and says, 'We don’t have a fucking doorbell.'"]

    def there_exists(self, terms):
        for term in terms:
            if term in self.voice_data:
                return True

    def record_audio(self, ask = False):
        with sr.Microphone(device_index = 1, sample_rate = 48000, chunk_size = 2048) as source:
            if ask:
                self.pystarks_speak(ask)
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                self.voice_data = r.recognize_google(audio)
            except sr.UnknownValueError:
                self.pystarks_speak(f"Sorry {self.name}, I did not get that")
            except sr.RequestError:
                self.pystarks_speak(f"Sorry {self.name}, my speech service is temporarily down at the moment. or connect to a network if you're not connected")
            except sr.TimeoutError:
                self.pystarks_speak(f"Sorry {self.name}, a connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond")

    def pystarks_speak(self, audio_string):
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

    def respond(self):
        if self.there_exists(['hey','hi','hello']):
            greetings = [f"Hey, how can I help you {self.name}?", f"Hey, what's up {self.name}?", f"I'm listening {self.name}", f"How can I help you {self.name}?", f"Hello {self.name}"]
            greet = random.choice(greetings)
            self.pystarks_speak(greet)
        if self.there_exists(["how are you"]):
            self.pystarks_speak(f"I'm very well, thanks for asking {self.name}")
        if self.there_exists(["what is your name", "what's your name", "tell me your name"]):
            if self.name:
                self.pystarks_speak("My name is PyStarks")
            else:
                self.pystarks_speak("My name is PyStarks. What's your name?")
        if self.there_exists(["my name is"]):
            person_name = self.voice_data.split("is")[-1].strip()
            self.pystarks_speak(f"Okay {person_name}, I'll make sure not to forget that")
            self.name = person_name
        if self.there_exists(['what time is it', 'what is the time', "what's the time"]):
            the_time = ctime().split(" ")[3].split(":")[0:2]
            if the_time[0] == "00":
                hours = '12'
            else:
                hours = the_time[0]
            minutes = the_time[1]
            self.pystarks_speak(f"The time is {hours}: {minutes}")
        if self.there_exists(["shutdown"]):
            self.pystarks_speak(f"Okay {self.name}, the system will shutdown in 2 minutes")
            os.system("shutdown -s -t 120")
            exit()
        if self.there_exists(["restart"]):
            self.pystarks_speak(f"Okay {self.name}, the system will restart in 2 minutes")
            os.system("shutdown -r -t 120")
            exit()
        if self.there_exists(["start notepad"]):
            pystarks_speak("Starting notepad")
            os.system("start notepad")
        if self.there_exists(["what is today's date", "what's today's date","tell me today's date"]):
            date = time.strftime("%a, %d %b %Y")
            self.pystarks_speak(f"Today's date is {date}")
        if self.there_exists(["tell me a story", "tell me another story"]):
            self.pystarks_speak(f"Okay {self.name}. {random.choice(self.stories)} Thank you for listening.")
        if self.there_exists(["play me a song"]):
            self.pystarks_speak(f"Okay {self.name}, sit back, relax, enjoy, and let me select a song for you")
            names = []
            for song in os.listdir('C:\\Users\Aser\\Music\\'):
                splitted = song.split('.')
                if splitted[-1] == "mp3":
                    names.append(str(song))
            random_song = random.choice(names)
            os.system(f'"C:\\Users\\Aser\\Music\\{random_song}"')
            exit()
        if self.there_exists(['search something', 'search google']):
            self.record_audio("What do you want to search for?")
            search_google = self.voice_data
            url = "https://google.com/search?q=" + search_google
            webbrowser.get().open(url)
            self.pystarks_speak("Here is what I found for "+search_google+" on google")
        if self.there_exists(['video', 'youtube']):
            self.record_audio("What video do you want to watch?")
            search_youtube = self.voice_data
            url = "https://www.youtube.com/results?search_query=" + search_youtube
            webbrowser.get().open(url)
            self.pystarks_speak("Here are the videos I found for "+search_youtube+" on youtube")
        if self.there_exists(['find a location', 'get a location', 'find me a place', 'find a place']):
            self.record_audio("What location do you want me to find?")
            location = self.voice_data
            url = "https://google.nl/maps/place/"+location+"/&amp;"
            webbrowser.get().open(url)
            self.pystarks_speak("Here is the location of "+location+" I found on google maps")
        if self.there_exists(["minimise"]):
            self.pystarks_speak(f"Okay {self.name}")
            user32 = ctypes.WinDLL('user32')
            user32.GetForegroundWindow.argtypes = ()
            user32.GetForegroundWindow.restype = w.HWND
            user32.ShowWindow.argtypes = w.HWND,w.BOOL
            user32.ShowWindow.restype = w.BOOL

            SW_MAXIMIZE = 3
            SW_MINIMIZE = 6

            hWnd = user32.GetForegroundWindow()
            user32.ShowWindow(hWnd, SW_MINIMIZE)
        if self.there_exists(["maximize"]):
            self.pystarks_speak(f"Okay {self.name}")
            user32 = ctypes.WinDLL('user32')
            user32.GetForegroundWindow.argtypes = ()
            user32.GetForegroundWindow.restype = w.HWND
            user32.ShowWindow.argtypes = w.HWND,w.BOOL
            user32.ShowWindow.restype = w.BOOL

            SW_MAXIMIZE = 3
            SW_MINIMIZE = 6

            hWnd = user32.GetForegroundWindow()
            user32.ShowWindow(hWnd, SW_MAXIMIZE)
        if self.there_exists(["go left"]):
            pyautogui.moveRel(-30, 0, duration=0.25)
        if self.there_exists(["go up"]):
            pyautogui.moveRel(0, -30, duration=0.25)
        if self.there_exists(["go down"]):
            pyautogui.moveRel(0, 30, duration=0.25)
        if self.there_exists(["go right"]):
            pyautogui.moveRel(30, 0, duration=0.25)
        if self.there_exists(["click"]):
            pyautogui.click()
        if self.there_exists(["screenshot"]):
            screenshot_files = []
            now = datetime.datetime.now()
            for file in os.listdir('C:\\Users\\aser\\Pictures'):
                screenshot_files.append(file)
            if "PyStarks_Screenshots" not in screenshot_files:
                os.system("mkdir C:\\Users\\aser\\Pictures\\PyStarks_Screenshots")
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(f'C:\\Users\\aser\\Pictures\\PyStarks_Screenshots\\screenshot{now.second}{now.minute}{now.hour}{now.day}{now.month}{now.year}.jpg')
            self.pystarks_speak("The screenshot has been taken")
        if self.there_exists(["write"]):
            self.voice_data = ''
            self.record_audio(f"Okay {self.name}, lets write")
            pyautogui.typewrite(self.voice_data)
        if self.there_exists(["goodbye", "quit", "exit"]):
            self.pystarks_speak(f"Goodbye {self.name}")
            exit()


va = Voice_Assistant()
va.pystarks_speak("Hello, how can I help you?")
while True:
    va.record_audio()
    va.respond()