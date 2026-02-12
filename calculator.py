import math
import re
import speech_recognition


def calculate(speaker, recognizer):
    speaker.say("What calculation do you want to perform?")
    speaker.runAndWait()

    try:
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            audio = recognizer.listen(source, timeout=5)

            query = recognizer.recognize_google(audio, language="en-IN").lower()

        # 🔹 Square root
        if "square root" in query:
            number = re.findall(r'\d+', query)
            if number:
                result = math.sqrt(float(number[0]))
                speaker.say(f"The square root of {number[0]} is {result}")
            else:
                speaker.say("I could not understand the number")

        else:
            numbers = re.findall(r'\d+', query)
            if len(numbers) < 2:
                speaker.say("I could not understand the calculation")
                speaker.runAndWait()
                return

            num1, num2 = float(numbers[0]), float(numbers[1])

            # ➕ Addition
            if (
                "plus" in query
                or "add" in query
                or "sum" in query
                or "added" in query
            ):
                result = num1 + num2

            # ➖ Subtraction
            elif (
                "minus" in query
                or "subtract" in query
                or "subtracted" in query
                or "less" in query
            ):
                result = num1 - num2

            # ✖ Multiplication
            elif (
                "multiply" in query
                or "multiplied" in query
                or "times" in query
                or "time" in query
                or "x" in query
            ):
                result = num1 * num2

            # ➗ Division
            elif (
                "divide" in query
                or "divided" in query
                or "over" in query
                or "by" in query
            ):
                if num2 == 0:
                    speaker.say("Division by zero is not allowed")
                    speaker.runAndWait()
                    return
                result = num1 / num2

            else:
                speaker.say("Operation not supported")
                speaker.runAndWait()
                return

            speaker.say(f"The result is {result}")

        speaker.runAndWait()

    except speech_recognition.UnknownValueError:
        speaker.say("I could not understand the calculation")
        speaker.runAndWait()
