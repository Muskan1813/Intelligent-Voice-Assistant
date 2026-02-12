import pyautogui


def increase_volume(speaker):
    for _ in range(5):   # increase step size if needed
        pyautogui.press("volumeup")

    speaker.say("Volume increased")
    speaker.runAndWait()


def decrease_volume(speaker):
    for _ in range(5):
        pyautogui.press("volumedown")

    speaker.say("Volume decreased")
    speaker.runAndWait()


def mute_volume(speaker):
    pyautogui.press("volumemute")

    speaker.say("System muted")
    speaker.runAndWait()


def unmute_volume(speaker):
    pyautogui.press("volumemute")  # mute is a toggle

    speaker.say("System unmuted")
    speaker.runAndWait()
