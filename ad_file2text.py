##########done in colab
####uplaod the audio file to coalb using the following code
from google.colab import files
uploaded =files.upload()
############## uploaded sx206.wav file
import speech_recognition as sr
r = sr.Recognizer()
ad = 'sx206.wav'
with sr.AudioFile(ad) as source:#################source is audio file
  print("say something");
  audio= r.record(source)###############the speech is recorded as it is an audio file
  print ("start")
try:
  print("text"+ r.recognize_google(audio));
except:
  pass;
