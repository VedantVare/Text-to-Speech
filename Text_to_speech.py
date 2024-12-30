import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

while True:
    a = input("Enter a sentence(or type exit to end): ")
    if a.lower()==exit:
        break
    speak(a)