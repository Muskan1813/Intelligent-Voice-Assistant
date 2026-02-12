import speech_recognition
import screen_brightness_control as sbc


def set_brightness(speaker, recognizer):
    speaker.say("Tell me the brightness level between zero and one hundred")
    speaker.runAndWait()

    try:
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            audio = recognizer.listen(source, timeout=5)
            level_text = recognizer.recognize_google(audio, language="en-IN").lower()

        # 🔹 Handle keywords
        if "maximum" in level_text or "full" in level_text:
            level = 100

        elif "minimum" in level_text or "lowest" in level_text:
            level = 0

        else:
            # 🔹 Try extracting digits first
            digits = "".join(filter(str.isdigit, level_text))

            if digits != "":
                level = int(digits)

            else:
                # 🔹 Word to number conversion
                units = {
                    "zero": 0, "one": 1, "two": 2, "three": 3,
                    "four": 4, "five": 5, "six": 6,
                    "seven": 7, "eight": 8, "nine": 9
                }

                teens = {
                    "ten": 10, "eleven": 11, "twelve": 12,
                    "thirteen": 13, "fourteen": 14,
                    "fifteen": 15, "sixteen": 16,
                    "seventeen": 17, "eighteen": 18,
                    "nineteen": 19
                }

                tens = {
                    "twenty": 20, "thirty": 30,
                    "forty": 40, "fifty": 50,
                    "sixty": 60, "seventy": 70,
                    "eighty": 80, "ninety": 90
                }

                words = level_text.split()
                level = 0

                for word in words:
                    if word in units:
                        level += units[word]
                    elif word in teens:
                        level += teens[word]
                    elif word in tens:
                        level += tens[word]
                    elif word == "hundred":
                        level = 100

                if level == 0 and "zero" not in level_text:
                    speaker.say("I could not understand the brightness level")
                    speaker.runAndWait()
                    return

        level = max(0, min(level, 100))
        sbc.set_brightness(level)

        speaker.say(f"Brightness set to {level} percent")

    except speech_recognition.UnknownValueError:
        speaker.say("I could not understand. Please try again.")

    except Exception as e:
        print("Brightness error:", e)
        speaker.say("Brightness control failed")

    speaker.runAndWait()
