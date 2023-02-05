import speech
import threading

while (True):
  user = input("Talk to Rick > ").lower().split()

  if ("bye" in user or "goodbye" in user or "got to go" in user or "gotta go" in user):
    speech.speak("goodbye")
    break