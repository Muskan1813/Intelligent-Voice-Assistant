import os
import webbrowser
import subprocess
import time
import speech_recognition

def open_chrome(speaker):
    try:
        subprocess.Popen(
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        )
        speaker.say("Opening Google Chrome")
    except:
        speaker.say("Chrome not found")
    speaker.runAndWait()



def open_vscode(speaker):
    try:
        subprocess.Popen("code", shell=True)
        speaker.say("Opening Visual Studio Code")
    except Exception as e:
        print("VS Code error:", e)
        speaker.say("Could not open Visual Studio Code")
    speaker.runAndWait()



def open_youtube(speaker):
    webbrowser.open("https://www.youtube.com")
    speaker.say("Opening YouTube")
    speaker.runAndWait()

def open_word(speaker):
    try:
        subprocess.Popen("start winword", shell=True)
        speaker.say("Opening Microsoft Word")
    except Exception as e:
        print("Word error:", e)
        speaker.say("Could not open Microsoft Word")
    speaker.runAndWait()


def open_spotify(speaker):
    try:
        subprocess.Popen("spotify")
        speaker.say("Opening Spotify")
    except:
        speaker.say("Spotify is not installed")
    speaker.runAndWait()

def open_notepad(speaker):
    try:
        subprocess.Popen("notepad")
        speaker.say("Opening Notepad")
    except:
        speaker.say("Could not open Notepad")
    speaker.runAndWait()
    
def open_jupyter(speaker):
    try:
        subprocess.Popen([
            r"C:\Users\Er. Muskan\anaconda3\python.exe",
            "-m",
            "notebook"
        ])
        speaker.say("Opening Jupyter Notebook")
    except Exception as e:
        print("Jupyter error:", e)
        speaker.say("Could not open Jupyter Notebook")
    speaker.runAndWait()


def open_colab(speaker):
    webbrowser.open("https://colab.research.google.com")
    speaker.say("Opening Google Colab")
    speaker.runAndWait()

def open_chatgpt(speaker):
    webbrowser.open("https://chat.openai.com")
    speaker.say("Opening ChatGPT")
    speaker.runAndWait()


def shutdown_system(speaker, recognizer):
    speaker.say("Are you sure you want to shut down the system? Say yes shutdown or no cancel.")
    speaker.runAndWait()

    try:
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            audio = recognizer.listen(source, timeout=5)
            confirmation = recognizer.recognize_google(audio).lower()
            
        os.system("shutdown /s /t 1")
        if "yes" or "Yes" or "shutdown" in confirmation:
            speaker.say("Shutting down the system")
            speaker.runAndWait()
            time.sleep(1)
            os.system("shutdown /s /t 1")
        else:
            speaker.say("Shutdown cancelled")
            speaker.runAndWait()

    except:
        speaker.say("Shutdown cancelled as no confirmation received")
        speaker.runAndWait()


def restart_system(speaker, recognizer):
    speaker.say("Are you sure you want to restart the system? Say yes restart or no cancel.")
    speaker.runAndWait()

    try:
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            audio = recognizer.listen(source, timeout=5)
            confirmation = recognizer.recognize_google(audio).lower()

        if "yes" or "Yes" or "restart" in confirmation:
            speaker.say("Restarting the system")
            speaker.runAndWait()
            time.sleep(1)
            os.system("shutdown /r /t 1")
        else:
            speaker.say("Restart cancelled")
            speaker.runAndWait()

    except:
        speaker.say("Restart cancelled as no confirmation received")
        speaker.runAndWait()
