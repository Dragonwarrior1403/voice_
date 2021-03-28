import speech_recognition as sr



r = sr.Recognizer()

mic = sr.Microphone()
posmic = sr.Microphone.list_microphone_names()
for x in posmic:
    print(x)
