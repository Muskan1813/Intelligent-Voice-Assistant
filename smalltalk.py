import random

def who_created_you(speaker):
    responses = [
        "I was created by Musskaan, as part of her intelligent voice assistant project. She created me to help with tasks and automation."
    ]
    speaker.say(responses)
    speaker.runAndWait()


def what_can_you_do(speaker):
    speaker.say(
        "I can control your system, manage notes, do calculations for you, send WhatsApp messages, adjust brightness, mic, and volume, and much more."
    )
    speaker.runAndWait()


def how_are_you(speaker):
    responses = [
        "I am functioning perfectly. Thanks for asking!",
        "All systems are running smoothly.",
        "I am doing great and ready to help you."
    ]
    speaker.say(random.choice(responses))
    speaker.runAndWait()


def tell_joke(speaker):
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Why did the computer go to therapy? It had too many bytes of emotional baggage.",
        "I would tell you a UDP joke, but you might not get it."
    ]
    speaker.say(random.choice(jokes))
    speaker.runAndWait()


def introduce_yourself(speaker):
    speaker.say(
        "Hello, I am your intelligent voice assistant Emgee. I can help you automate tasks and answer questions."
    )
    speaker.runAndWait()
