#intelligent assistant without wake word
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys


recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate',150)

todo_list = ['Go Shopping', 'Clean Room', 'Record Video']

def create_note():
    global recognizer
    
    speaker.say("What do you want to write onto your note? ")
    speaker.runAndWait()
    
    done = False
    
    while not done:
        try:
            mic = speech_recognition.Microphone()  # Create an instance of Microphone
            with mic as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = recognizer.listen(source)


                note = recognizer.recognize_google(audio)
                note = note.lower()
                
                speaker.say("choose a filename!")
                speaker.runAndWait()
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                
                filename = recognizer.recognize_google(audio)
                filename = filename.lower()
                
            with open(filename, 'w') as f:
                f.write(note)   
                done = True
                speaker.say(f"I successfully created the note{filename}")
                speaker.runAndWait()
             
             
        except speech_recognition.UnknownValueError:
            recognizer=speech_recognition.Recognizer()
            speaker.say("I did not understand you! Please try again!")
            speaker.runAndWait()


def add_todo():
    global recognizer
    
    speaker.say("what to do you want to add?")
    speaker.runAndWait()
    
    done = False
    
    while not done:
        try:
            
            mic = speech_recognition.Microphone()  # Create an instance of Microphone
            with mic as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = recognizer.listen(source)

                
                item = recognizer.recognize_google(audio)
                item = item.lower()
                
                todo_list.append(item)
                done = True
                
                speaker.say(f"I added {item} to the to do list!")
                speaker.runAndWait()
                
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("i did not understand. Please try again!")
            speaker.runAndWait()
            
            
def show_todo():
    
    speaker.say("the items on your to do list are as follows")
    speaker.runAndWait() 
    for item in todo_list:
        speaker.say(item)
        speaker.runAndWait() 
        
    speaker.runAndWait()
    
    
def hello():    
    speaker.say("Hello. What can i do for you?")
    speaker.runAndWait()
    
    
def quit():
    speaker.say("Goodbye! Feel free to reach out if you need help again. Have a great day!")
    speaker.runAndWait()
    sys.exit(0)
    
  
mappings = {
    "greeting": hello,
    "create_note": create_note, 
    "add_todo": add_todo,
    "show_todos": show_todo,    
    "exit": quit
}


assistant = GenericAssistant('C:/Users/Er. Muskan/OneDrive/Desktop/voice assistant/intents2.json', intent_methods=mappings)

assistant.train_model()  # Assuming train() is the updated method
# assistant.save_model() assistant.load_model()           # Assuming save() is the updated method


while True:
    
    try:
        with speech_recognition.Microphone() as mic:
            
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            
            message = recognizer.recognize_google(audio)
            message= message.lower()
            
        
        response = assistant.request(message)

        print(response)

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer() 