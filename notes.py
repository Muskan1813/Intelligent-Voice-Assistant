import os
import speech_recognition

# shared todo list (same behavior as before)
todo_list = ['Go Shopping', 'Clean Room', 'Record Video']


# 📝 Create Note (same logic as your original)
def create_note(speaker, recognizer):
    speaker.say("What do you want to write onto your note?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            mic = speech_recognition.Microphone()
            with mic as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = recognizer.listen(source)

                note = recognizer.recognize_google(audio, language="en-IN").lower()

                speaker.say("Choose a filename")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = recognizer.listen(source)

                filename = recognizer.recognize_google(audio, language="en-IN").lower()

            with open(filename, "w") as f:
                f.write(note)

            speaker.say(f"I successfully created the note {filename}")
            speaker.runAndWait()
            done = True

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand you. Please try again.")
            speaker.runAndWait()


# 🗑️ Delete Note (same logic as your original)
def delete_note(speaker, recognizer):
    speaker.say("Which note do you want to delete?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            mic = speech_recognition.Microphone()
            with mic as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = recognizer.listen(source)

                filename = recognizer.recognize_google(audio, language="en-IN").lower()

            if os.path.exists(filename):
                os.remove(filename)
                speaker.say(f"I have deleted the note {filename}")
            else:
                speaker.say("Sorry, I could not find that note")

            speaker.runAndWait()
            done = True

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand. Please say the filename again.")
            speaker.runAndWait()


# ➕ Add Todo (same logic as your original)
def add_todo(speaker, recognizer):
    speaker.say("What do you want to add to the to do list?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            mic = speech_recognition.Microphone()
            with mic as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = recognizer.listen(source)

                item = recognizer.recognize_google(audio, language="en-IN").lower()

            todo_list.append(item)

            speaker.say(f"I added {item} to the to do list")
            speaker.runAndWait()
            done = True

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand. Please try again.")
            speaker.runAndWait()


# 📋 Show Todo (same logic as your original)
def show_todo(speaker):
    speaker.say("The items on your to do list are as follows")
    speaker.runAndWait()

    for item in todo_list:
        speaker.say(item)
        speaker.runAndWait()
