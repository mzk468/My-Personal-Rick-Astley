import speech
import threading

def setToNothing():
  with open("status", "w+") as file:
    file.write("0 0")

def setThinking():
  with open("status", "w+") as file:
    file.write("1 0")

while (True):
  
  setToNothing()
  user = input("Talk to Rick > ").lower().split()

  setThinking()

  if ("bye" in user or "goodbye" in user or "got to go" in user or "gotta go" in user):
    speech.speak("goodbye")
    break
