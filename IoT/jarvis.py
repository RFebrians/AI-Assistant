from gtts import gTTS
import speech_recognition as sr
import os
import RPi.GPIO as GPIO

# led setup
satu = 2
dua = 3
tiga = 14
empat = 17
lima = 27
enam = 22
buka = 9
tutup = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(satu, GPIO.OUT)
GPIO.setup(dua, GPIO.OUT)
GPIO.setup(tiga, GPIO.OUT)
GPIO.setup(empat, GPIO.OUT)
GPIO.setup(lima, GPIO.OUT)
GPIO.setup(enam, GPIO.OUT)
GPIO.setup(buka, GPIO.OUT)
GPIO.setup(tutup, GPIO.OUT)

def setColor(satu, dua, tiga, empat, lima, enam, buka, tutup):
    GPIO.output(s, satu)
    GPIO.output(d, dua)
    GPIO.output(t, tiga)
    GPIO.output(e, empat)
    GPIO.output(l, lima)
    GPIO.output(m, enam)
    GPIO.output(b, buka)
    GPIO.output(p, tutup)

def turnOff(satu=0, dua=0, tiga=0, empat=0, lima=0, enam=0, buka=0, tutup=0):
    GPIO.output(s, satu)
    GPIO.output(d, dua)
    GPIO.output(t, tiga)
    GPIO.output(e, empat)
    GPIO.output(l, lima)
    GPIO.output(m, enam)
    GPIO.output(b, buka)
    GPIO.output(p, tutup)

# gtts 하이퍼 마라미터
language = 'en'
done = False

def speak(command):
    aicommand = gTTS(text=command, lang='en', slow=False)
    aicommand.save('aicommand.mp3')
    os.system("mpg321 aicommand.mp3")

def command(text):
    if 'satu ' in text:
        command = 'oke, ke lantai satu'
        GPIO.output(satu, True)
        turnOff()
    elif 'dua' in text:
        command = 'yes bose, ke lantai dua'
        GPIO.output(dua, True)
        turnOff()
    elif 'tiga' in text:
        command = 'yes bose, ke lantai tiga'
        GPIO.output(tiga, True)
        turnOff()
    elif 'empat' in text:
        command = 'yes bose, ke lantai empat'
        GPIO.output(empat, True)
        turnOff()
    elif 'lima' in text:
        command = 'yes bose, ke lantai lima'
        GPIO.output(lima, True)
        turnOff()
    elif 'enam' in text:
        command = 'yes bose, ke lantai enam'
        GPIO.output(enam, True)
        turnOff()
    elif 'buka' in text:
        command = 'yes bose, tutup pintu'
        GPIO.output(tutup, True)
        turnOff()
    elif 'tutup' in text:
        command = 'yes bose, buka pintu'
        GPIO.output(buka, True)
        turnOff()
    elif 'aicommand' in text:
        command = "you are welcome, sir"
    elif 'bye aicommand' in text:
        command = 'yes sir, Please call me again next time. bye'
    else:
        command = "i can't understand, what you said. please again command to me"
    return command

def aicommand(done1=False):
    rs = sr.Recognizer()
    while not done1:
        with sr.Microphone() as source:
            print("Speak Anything : ")
            audio = rs.listen(source)
            try:
                text = rs.recognize_google(audio)
                print("You said:")
                command = command(text)
                if command == 'yes sir, Please call me again next time. bye':
                    speak(command)
                speak(command)
            except:
                print("Sorry could not recognize what you said!!!")
            
r = sr.Recognizer()
while not done:
    with sr.Microphone() as source1:
        audio = r.listen(source1)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        
            # command
            if 'aicommand' in text:
                aicommand = gTTS(text="hello everyone my name is aicommand, I am an assistant to Yungyo.\
                what can i help you?", lang=language, slow=False)
                aicommand.save("aicommand.mp3")
                os.system("mpg321 aicommand.mp3")
                aicommand()
                done=True
        except:
            print("Sorry could not recognize what you said")
        

