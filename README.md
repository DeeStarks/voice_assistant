# Speech Assistant

Python app that uses speech recognition and text-to-speech
This app initially used the Google text-to-speech API, but has been updated to use offline text-to-speech with pyttsx3

### Dependencies

```
pip install speechrecognition
pip install pyttsx3
pip install pyaudio
pip install playsound
```
```
pip install PyAudio
```
(If there is a issue in installing PyAudio use .whl file from this link [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio))  

### Voice Commands

You can add other commands, but these are the ones that exist

- How are you?
- What is your name?
- What time is it?
- What is today's date?
- Shutdown (shuts the system in 2 minutes. NB: For Windows users only. Change the shutdown command if using a different Operating System.)
- Restart (Restarts the system in 2 minutes. NB: For Windows users only. Change the restart command if using a different Operating System.)
- Start Notepad
- Play me a song (change to your music path)
- Search something for me
- Find a location
- Goodbye
