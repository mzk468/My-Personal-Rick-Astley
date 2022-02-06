import speech_recognition as sr

def main():

  with sr.Microphone() as source:

    try:
      
      r.adjust_for_ambient_noise(source)

      print("Say som'ink")

      audio = r.listen(source)

      print("You said: " + r.recognize_google(audio))
    
    except Exception as e:
      print("Caught exception: " + str(e))

if __name__ == "__main__":
  main()
