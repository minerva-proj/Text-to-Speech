## Download tesseract engine from: https://osdn.net/projects/sfnet_tesseract-ocr-alt/downloads/tesseract-ocr-setup-3.02.02.exe/
## Install following libraries:
# pip install pytesseract
# pip install opencv-python
# pip install pillow
# pip install gTTS
# pip install pygame

# Import liraries
import pytesseract
from pytesseract import Output
import cv2
import numpy as np
from PIL import Image
from gtts import gTTS
import os
from pygame import mixer


#IMAGE TO TEXT
# Path to the image
imagePath = " "
imgRead = np.array(Image.open(imagePath))

# path to tesseract engine
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
getTheText = pytesseract.image_to_string(imgRead, config="--psm 6")
print(getTheText)

# TEXT TO SPEECH
language = 'en'
myobj = gTTS(text=getTheText, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
myobj.save(r" ")
  
# Playing the converted file
mixer.init()
mixer.music.load(r" ")
mixer.music.play()
