import pyautogui
import datetime
import speech_recognition
import os


SAVE_FOLDER = "screenshots"

# Create folder if not exists
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)


def take_screenshot(speaker):
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshot_{timestamp}.png"
        path = os.path.join(SAVE_FOLDER, filename)

        image = pyautogui.screenshot()
        image.save(path)

        speaker.say("Screenshot taken successfully")

    except Exception as e:
        print("Screenshot error:", e)
        speaker.say("Could not take screenshot")

    speaker.runAndWait()


def take_screenshot_with_name(speaker, recognizer):
    speaker.say("What name should I save the screenshot as?")
    speaker.runAndWait()

    try:
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            audio = recognizer.listen(source, timeout=5)
            name = recognizer.recognize_google(audio, language="en-IN")

        name = name.replace(" ", "_")
        filename = f"{name}.png"
        path = os.path.join(SAVE_FOLDER, filename)

        image = pyautogui.screenshot()
        image.save(path)

        speaker.say(f"Screenshot saved as {name}")

    except speech_recognition.UnknownValueError:
        speaker.say("I could not understand the name")
        

    except Exception as e:
        print("Screenshot error:", e)
        speaker.say("Could not take screenshot")

    speaker.runAndWait()
