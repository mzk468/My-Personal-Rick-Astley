import speech_recognition as sr

rec = sr.Recognizer()

mic = sr.Microphone(device_index=0)


with mic as source:
  rec.adjust_for_ambient_noise(source)
  audio = rec.listen(source)


try:
  print(rec.recognize_google(audio))

  
except sr.UnknownValueError:
  print("didnt work")