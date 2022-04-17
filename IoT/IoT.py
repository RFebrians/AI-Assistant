from gtts import gTTS
import os

mytext = 'aicommand'

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("aicommand.mp3")
os.system("mpg321 aicommand.mp3")
