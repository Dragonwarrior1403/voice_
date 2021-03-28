import socket
import speech_recognition as sr
import pyttsx3 as TTS
#import pyaudio for later

phrase=''

phrase=''
r = sr.Recognizer()

def text_from_audio(dur=5, lang='en-US', off=0): # This is a code for taking the auio from the user and converting it to txt
    global phrase#, word

    with sr.Microphone(device_index=0, sample_rate=48000) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Go on, Speak")

        try:
            audio = r.record(source, duration=dur, offset=off)
            phrase = r.recognize_google(audio,language=lang)

        except sr.UnknownValueError as err:
            phrase="say again"

        except sr.RequestError as err:
            phrase ="request error"

        finally:
            return phrase

def text_to_audio(txt, gender='male', rate=150): # This is a code to convert text into a speech
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

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT = "Disconnect!"
SERVER = "192.168.0.27"
ADDR = (SERVER,PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER -len(send_length))
    client.send(send_length)
    client.send(message)

check = True
while check:
    message = input("Enter message")
    send(text_from_audio())
    if input("DO you want to disconnect (Y/N)") == "Y":
        check = False

send(DISCONNECT)


