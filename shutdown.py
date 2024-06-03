import os
import speech_recognition
import pyttsx3
r = speech_recognition.Recognizer()

def SpeakText(command):

    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-80)
    engine.say(command)
    engine.runAndWait()

def listen():
    with speech_recognition.Microphone() as source2:
        r.adjust_for_ambient_noise(source2, duration=1)
        SpeakText("say something")
        audio2 = r.listen(source2)
        try:
            MyText = r.recognize_google(audio2)
        except:
            #SpeakText("Didnt recognize voice")
            SpeakText("try again")
            listen()
            return
        MyText = MyText.lower()

    if MyText == "hi" or MyText == "Hi":
        SpeakText("Shutting down computer in 5")
        SpeakText("4")
        SpeakText("3")
        SpeakText("2")
        SpeakText("1")

        os.system('shutdown -s')

listen()