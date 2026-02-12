import os
import webbrowser
import subprocess
import time
import speech_recognition

def open_chrome(speaker):
    try:
        subprocess.Popen("chrome")
        speaker.say("Opening Google Chrome")
    except:
        speaker.say("Chrome is not installed")
    speaker.runAndWait()


def open_vscode(speaker):
    try:
        subprocess.Popen("code")
        speaker.say("Opening Visual Studio Code")
    except:
        speaker.say("VS Code is not installed or not in PATH")
    speaker.runAndWait()


def open_youtube(speaker):
    webbrowser.open("https://www.youtube.com")
    speaker.say("Opening YouTube")
    speaker.runAndWait()


def open_spotify(speaker):
    try:
        subprocess.Popen("spotify")
        speaker.say("Opening Spotify")
    except:
        speaker.say("Spotify is not installed")
    speaker.runAndWait()


def shutdown_system(speaker, recognizer):
    speaker.say("Are you sure you want to shut down the system? Say yes or no.")
    speaker.runAndWait()

    try:
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            audio = recognizer.listen(source, timeout=5)
            confirmation = recognizer.recognize_google(audio).lower()

        if "yes" in confirmation:
            speaker.say("Shutting down the system")
            speaker.runAndWait()
            time.sleep(1)
            os.system("shutdown /s /t 1")
        else:
            speaker.say("Shutdown cancelled")
            speaker.runAndWait()

    except:
        speaker.say("Shutdown cancelled")
        speaker.runAndWait()


def restart_system(speaker, recognizer):
    speaker.say("Are you sure you want to restart the system? Say yes or no.")
    speaker.runAndWait()

    try:
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            audio = recognizer.listen(source, timeout=5)
            confirmation = recognizer.recognize_google(audio).lower()

        if "yes" in confirmation:
            speaker.say("Restarting the system")
            speaker.runAndWait()
            time.sleep(1)
            os.system("shutdown /r /t 1")
        else:
            speaker.say("Restart cancelled")
            speaker.runAndWait()

    except:
        speaker.say("Restart cancelled")
        speaker.runAndWait()
