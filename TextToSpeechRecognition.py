#Text To Speecg Recognition

# Import the gTTS module for text to speech conversion
from gtts import gTTS
import os
FileName = input('Enter the name of saving file: ')
file = open(r'.\DetailsForTextToSpeech.txt','r') # The text that you we want to convert to audio
mytext = file.read()
languageCode = 'en' # Language in which to convert
Convert = gTTS(text=mytext, lang=languageCode, slow=False) # Passing the text and language to the engine, here we have marked slow=False. Which tells the module that the converted audio should have a high speed
# Saving the converted audio in a mp3 file
Convert.save(str(FileName)+'.mp3')
print('I am done bye')
