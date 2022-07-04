from time import sleep
import speech_recognition as sr

from hardware.experiment import Experiment

lister = sr.Recognizer()
experiment = Experiment()

def main():
    try:
        sleep(1)
        with sr.Microphone() as source:
            voice = lister.listen(source)
            command = lister.recognize_google(voice)
            print(command)
            if command.strip() == 'IC':
                experiment.send_message_lcd('Memuat Proses ...', 1, 2)
                experiment.send_message_lcd('AI Berhasil terhubung', 2, 2)
    except Exception as e:
        print(e)

if __name__=='__main__':
    experiment.change_state_led('blue', True) # Status Change
    experiment.send_message_lcd('Listening..')
    while True:
        experiment.send_message_lcd('Perintah Berhasil dijalankan')
        main()
