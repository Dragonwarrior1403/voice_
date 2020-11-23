import speech_recognition as sr
import pyttsx3 as TTS
#import pyaudio

#word =''

phrase=''
r = sr.Recognizer()

def text_from_audio(dur=2, lang='en-US', off=0): # This is a code for taking the auio from the user and converting it to txt
    global phrase#, word

    with sr.Microphone(device_index=0, sample_rate=48000) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("\n \n \n \nGo on, Speak\n \n \n \n ")

        try:
            audio = r.record(source, duration=dur, offset=off)
            phrase = r.recognize_google(audio,language=lang)

        except sr.UnknownValueError as err:
            phrase="say again"

        except sr.RequestError as err:
            phrase ="request error"

        finally:
            return phrase

def text_to_audio(txt, gender='male', rate=200): # This is a code to convert text into a speech
    engine = TTS.init()

    voice = ''
    if gender == 'male' or gender == 'Male' or gender == 'MALE' or gender == 'boy' or gender == 'BOY' or gender == 'Boy':
        voice = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    elif gender == 'female' or gender == 'Female' or gender == 'FEMALE' or gender == 'girl' or gender == 'GIRL' or gender == 'Girl':
        voice = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    else:
        voice = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
    engine.setProperty('rate', rate)
    engine.setProperty('voice', voice)
    engine.say(txt)
    engine.runAndWait()


while True:
    text_to_audio(text_from_audio())



