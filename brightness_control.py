import screen_brightness_control as sbc
import speech_recognition


def increase_brightness(speaker):
    current = sbc.get_brightness()[0]
    sbc.set_brightness(min(current + 10, 100))

    speaker.say("Brightness increased")
    speaker.runAndWait()


def decrease_brightness(speaker):
    current = sbc.get_brightness()[0]
    sbc.set_brightness(max(current - 10, 0))

    speaker.say("Brightness decreased")
    speaker.runAndWait()


def set_brightness(speaker, recognizer):
    speaker.say("Tell me the brightness level")
    speaker.runAndWait()

    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        audio = recognizer.listen(source)

        level_text = recognizer.recognize_google(audio, language="en-IN")

    level = int("".join(filter(str.isdigit, level_text)))
    level = max(0, min(level, 100))

    sbc.set_brightness(level)

    speaker.say(f"Brightness set to {level} percent")
    speaker.runAndWait()
