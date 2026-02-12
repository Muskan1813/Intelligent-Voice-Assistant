import webbrowser
import pyautogui
import time
import speech_recognition
import json
import os

CONTACTS_FILE = "contacts.json"


# 🔹 Load contacts
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return {}
    with open(CONTACTS_FILE, "r") as f:
        return json.load(f)


# 🔹 Save contacts
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


# 🔹 Open chat
def open_chat(number):
    url = f"https://web.whatsapp.com/send?phone={number.replace('+', '')}&text="
    webbrowser.open(url)
    time.sleep(10)


# 🔥 SEND MESSAGE
def send_whatsapp_message(speaker, recognizer):

    contacts = load_contacts()

    speaker.say("Who should I send the message to?")
    speaker.runAndWait()

    try:
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            audio = recognizer.listen(source, timeout=5)
            name = recognizer.recognize_google(audio).lower()
            # print(f"[DEBUG] Recognized contact name: {name}")


        # If contact exists
        if name in contacts:
            number = contacts[name]

        else:
            speaker.say("I don't have this contact saved. Please say the number with country code.")
            speaker.runAndWait()

            with speech_recognition.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.3)
                audio = recognizer.listen(source, timeout=5)
                number = recognizer.recognize_google(audio).replace(" ", "")

            if not number.startswith("+"):
                speaker.say("Number must start with plus and country code.")
                speaker.runAndWait()
                return

            # Auto-save new contact
            contacts[name] = number
            save_contacts(contacts)
            speaker.say(f"Contact {name} saved successfully.")

        speaker.say("What message should I send?")
        speaker.runAndWait()

        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            audio = recognizer.listen(source, timeout=5)
            message = recognizer.recognize_google(audio)

        # open_chat(number)
        # speaker.say("Opening WhatsApp Web. Please wait.")
        # speaker.runAndWait()

        # time.sleep(10)
        # pyautogui.typewrite(message, interval=0.02)
        # time.sleep(1)
        # pyautogui.press("enter")

        # speaker.say("Message sent successfully.")
        # speaker.runAndWait()
        
        open_chat(number)

        speaker.say("Opening WhatsApp Web. Please wait.")
        speaker.runAndWait()

        time.sleep(18)  # wait for WhatsApp to fully load

        # 🔥 Force focus on message input box
        # screen_width, screen_height = pyautogui.size()
        # pyautogui.click(screen_width / 2, screen_height - 120)

        # time.sleep(1)  # allow focus to activate

        pyautogui.typewrite(message, interval=0.02)
        pyautogui.press("enter")

        speaker.say("Message sent successfully.")
        speaker.runAndWait()

    except Exception as e:
        print("WhatsApp error:", e)
        speaker.say("Could not send the message.")

    speaker.runAndWait()


# 📞 CALL CONTACT
def call_whatsapp_contact(speaker, recognizer):

    contacts = load_contacts()

    speaker.say("Who should I call?")
    speaker.runAndWait()

    try:
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            audio = recognizer.listen(source, timeout=5)
            name = recognizer.recognize_google(audio).lower()

        if name not in contacts:
            speaker.say("This contact is not saved.")
            speaker.runAndWait()
            return

        number = contacts[name]
        open_chat(number)

        speaker.say("Chat opened. Please press the call button.")
        speaker.runAndWait()

    except Exception as e:
        print("Call error:", e)
        speaker.say("Could not open WhatsApp.")

    speaker.runAndWait()
