#intelligent assistant with wake up word
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import threading
import tkinter as tk
from datetime import datetime
import screen_brightness_control as sbc
import pyautogui

# self made modules below
import system_commands as syscmd
import calculator
import notes
import volume_control as vc
import brightness_control as bc



from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import (
    AudioUtilities,
    IAudioEndpointVolume,
    EDataFlow,
    ERole
)





recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate',150)




def tell_day():
    today = datetime.now().strftime("%A")
    speaker.say(f"Today is {today}")
    speaker.runAndWait()

def tell_date():
    date = datetime.now().strftime("%d %B %Y")
    speaker.say(f"Today's date is {date}")
    speaker.runAndWait()

def tell_time():
    time = datetime.now().strftime("%I:%M %p")
    speaker.say(f"The current time is {time}")
    speaker.runAndWait()



   
   
def hello():    
    speaker.say("Hello. What can i do for you?")
    speaker.runAndWait()
    
    
def quit():
    speaker.say("Goodbye! Feel free to reach out if you need help again. Have a great day!")
    speaker.runAndWait()
    root.destroy()  # Destroy the Tkinter window
    sys.exit(0)
    
    
def create_file(self):
    with open("somefile.txt", "w") as f:
        f.write("Hello World")   


def run_assistant():
    global recognizer
    while True:
        
        try:
            with speech_recognition.Microphone() as mic:
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                print("Listening...")     #debug(remove later)
                audio = recognizer.listen(mic)
                
                message = recognizer.recognize_google(audio, language="en-IN")
                message= message.lower()
                print(f"Recognized: {message}")  # Debug info
                
                if "hello" in message:
                    label.config(fg = "red")
                    speaker.say("I am listening")
                    speaker.runAndWait()
                    
                    
                    audio = recognizer.listen(mic)
                    message = recognizer.recognize_google(audio, language="en-IN")
                    message = message.lower()
                    print(f"Command: {message}")  # Debug info
                    
                    response = assistant.request(message)
                    # print(response)
                    
                    
                    if response is not None:
                        speaker.say(response)
                        speaker.runAndWait()
                        
                    label.config(fg="black")   

            

        except speech_recognition.UnknownValueError:
            print("Could not understand the audio.")   #debug info
            
            label.config(fg="black")
            recognizer = speech_recognition.Recognizer() 
  
mappings = {
    
    "create_note": lambda: notes.create_note(speaker, recognizer),
    "delete_note": lambda: notes.delete_note(speaker, recognizer),
    "add_todo": lambda: notes.add_todo(speaker, recognizer),
    "show_todos": lambda: notes.show_todo(speaker),
    
    "tell_day": tell_day,
    "tell_date": tell_date,
    "tell_time": tell_time,
    
    "calculate": lambda: calculator.calculate(speaker, recognizer),
    
    "increase_volume": lambda: vc.increase_volume(speaker),
    "decrease_volume": lambda: vc.decrease_volume(speaker),
    "mute_volume": lambda: vc.mute_volume(speaker),
    "unmute_volume": lambda: vc.unmute_volume(speaker),
    
  
    "increase_brightness": lambda: bc.increase_brightness(speaker),
    "decrease_brightness": lambda: bc.decrease_brightness(speaker),
    "set_brightness": lambda: bc.set_brightness(speaker, recognizer),  
    
    "open_chrome": lambda: syscmd.open_chrome(speaker),
    "open_vscode": lambda: syscmd.open_vscode(speaker),
    "open_youtube": lambda: syscmd.open_youtube(speaker),
    "open_spotify": lambda: syscmd.open_spotify(speaker),
    "shutdown_system": lambda: syscmd.shutdown_system(speaker, recognizer),
    "restart_system": lambda: syscmd.restart_system(speaker, recognizer), 
    "open_word": lambda: syscmd.open_word(speaker),
    "open_notepad": lambda: syscmd.open_notepad(speaker),
    "open_jupyter": lambda: syscmd.open_jupyter(speaker),
    "open_colab": lambda: syscmd.open_colab(speaker),
    "open_chatgpt": lambda: syscmd.open_chatgpt(speaker), 
    
    "exit": quit,
    "file":create_file
}


assistant = GenericAssistant('C:/Users/Er. Muskan/OneDrive/Desktop/voice assistant/intents2.json', intent_methods=mappings)

assistant.train_model()  # Assuming train() is the updated method
# assistant.save_model() assistant.load_model()           # Assuming save() is the updated method
root = tk.Tk()
label = tk.Label(text="🤖", font=("Arial", 120, "bold"))
label.pack()
threading.Thread(target=run_assistant).start()
root.mainloop()




