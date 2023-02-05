import speech_recognition as sr

recogniser = sr.Recognizer()

micNum = "list" # Why not

def speak(string):
  # Temporarily, we use print()
  print(str(string))

while(True):
  if micNum == "list":
    for i in range(len(sr.Microphone.list_microphone_names())):
      print(str(i+1) + ". " + sr.Microphone.list_microphone_names()[i])

  micNum = input("\nEnter mic number for input > ").lower()

  if micNum.isdigit():
    micNum = int(micNum) - 1
    break; # BREAK FREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
  else:
    print("Invalid, please reenter number. Type `list` to view list again")

mic = sr.Microphone(device_index=micNum)


with mic as source:
  recogniser.adjust_for_ambient_noise(source)
  audio = recogniser.listen(source)


try:
  print(recogniser.recognize_google(audio))

  
except sr.UnknownValueError:
  speak("I'm having issues. Try restarting me, make sure your microphone is working properly")
