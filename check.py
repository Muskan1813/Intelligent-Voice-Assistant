import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as mic:
    print("Say something...")
    audio = recognizer.listen(mic)
    print("Recognizing...")
    text = recognizer.recognize_google(audio, language="en-IN")
    print("You said:", text)
    with open("test_audio.wav", "wb") as f:
        f.write(audio.get_wav_data())

