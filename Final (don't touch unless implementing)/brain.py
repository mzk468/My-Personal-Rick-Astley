import speech
import threading
import random

print("Speak to Rick Astley himself! Please don't use punctuaution. No exclamation marks, no apostrophes, nothing. Please.")

while (True):

  user = input("Talk to Rick > ").lower().split()

  if ("bye" in user or "goodbye" in user or "got to go" in user or "gotta go" in user):
    speech.speak("goodbye")
    break

  if ("sing" in user):
    speech.play("never-gonna-give-you-up.mp3")
    speech.play("never-gonna-let-you-down.mp3")
    speech.play("never-gonna-run-around-and-desert-you.mp3")

  if (("you" in user and "scared" in user) or "scream" in user):
    speech.scream()

  if user[0] == "say":
    str = ""
    i = 1
    while i < len(user):
      str+= user[i] + " "
    
    speech.speak(str)

  if "play" in user and "music" in user:
    speech.speak("are you sure")
    x = input("Are you sure? > ")
    if (x.lower == "yes" or x.lower == "y"):
      speech.speak("i will rick roll you")
      y = input("You sure you're sure? > ")
      if (y.lower == "yes" or y.lower == "y"):
        speech.speak("alright")
        speech.speak("you have to sit through this now")
        speech.play("fullsong.mp3")

  if "how" in user and "you" in user:
    resps = ["im alright", "could be better", "you wouldnt understand", "i dont wanna tell you how im feeling", "i give up", "i spilled my dessert"]

    speech.speak(resps[random.randint(0, len(resps))])

  if "you" in user and "love" in user and "me" in user:
    speech.speak("you know the rules")