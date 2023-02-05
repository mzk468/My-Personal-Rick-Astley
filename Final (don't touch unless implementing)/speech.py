import pyttsx3
import playsound

engine = pyttsx3.init()
engine.setProperty('rate', 135)
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.3)
engine.setProperty('voice', engine.getProperty("voices")[15].id)  # Using voice 2 for Rick

def play(filename):
  playsound.playsound("Audio/" + filename, True)

def speak(input):
  input = input.split(".")  # Separate Strings whenever there are pauses
  for i in range(len(input)):
    input[i] = input[i].split(",")

  # Creating 1D list with everything
  processedInput = [] # 

  for a in input:
    for b in a:
      processedInput.append(b.lower())


  for processedInput in processedInput:
    processedInput = str(processedInput)
    processedInput = processedInput.split(" ")
    
    while i < len(processedInput):
    
      # Okay this part will look horrendous af
      if (len(processedInput) == 0):
        break

      if (len(processedInput) >= 1):
        if (processedInput[i] == "understand"):
          play("understand.mp3")
          i += 1
          continue

        if processedInput[i].lower == "$scream$":
          play("iii.mp3")
          i += 1
          continue
      
        if processedInput[i] == "hi":
          play("hi.mp3")
          i+=1
          continue
      
        if processedInput[i] == "goodbye":
          play("goodbye.mp3")
          i+=1
          continue

        if processedInput[i] == "feeling":
          i+=1
          play("feeling.mp3")
          continue

        if processedInput[i] == "dessert" or processedInput[i] == "desert":
          i+=1
          play("dessert.mp3")
          continue
    
        if processedInput[i] == "cry":
          i+=1
          play("cry.mp3")
          continue

      if (len(processedInput) >= 2):
        if (processedInput[i] == "other" and processedInput[i+1] == "guy"):
          i = i+2
          play("other-guy.mp3")
          continue

        if (processedInput[i] == "say" and processedInput[i+1] == "goodbye"):
          i = i+2
          play("say-goodbye.mp3")
          continue

        if (processedInput[i] == "give" and processedInput[i+1] == "up"):
          i+=2
          play("give-up.mp3")
          continue

      if len(processedInput) >=2:
        if processedInput[i] == "never" and processedInput[i+1] == "gonna":
          if len(processedInput) == 5:
            if (processedInput[i+2] == "give" and processedInput[i+3] == "you" and processedInput[i+4] == "up"):
              play("never-gonna-give-you-up.mp3")
              i = i+5
              continue
            elif (processedInput[i+2] == "let" and processedInput[i+3] == "you" and processedInput[i+4] == "down"):
              play("never-gonna-let-you-down.mp3")
              i = i+5
              continue
          if (len(processedInput) >= 4):
            if (processedInput[i+2] == "make" and processedInput[i+3] == "you"):
              if len(processedInput) == 5:
                if (processedInput[i+4] == "cry"):
                  play("never-gonna-make-you-cry.mp3")
                  i = i+5
                  continue
              play("never-gonna-make-you.mp3")
              i = i+4
              continue
            elif (processedInput[i+2] == "run" and processedInput[i+3] == "around"):
              if len(processedInput) == 7:
                if (processedInput[i+4] == "and" and processedInput[i+5] == "desert" and processedInput[i+6] == "you"):
                  i = i+7
                  play("never-gonna-run-around-and-desert-you.mp3")
                  continue
              play("never-gonna-run-around.mp3")
              i = i+4
              continue
            elif (processedInput[i+2] == "say" and processedInput[i+3] == "goodbye"):
              i = i+4
              play("never-gonna-say-goodbye.mp3")
              continue
      
      if (len(processedInput) == 4):
        if (processedInput[i] == "wouldnt" and processedInput[i+1] == "get" and processedInput[i+2] == "this" and processedInput[i+3] == "from"):
          play("wouldnt-get-this-from.mp3")
          i+=4
          continue

      if len(processedInput) >=4:
        if (processedInput[i] == "you"):
          if (processedInput[i+1] == "know" and processedInput[i+2] == "the" and processedInput[i+3] == "rules"):
            i+=4
            play("you-know-the-rules.mp3")
            continue
          if (len(processedInput) == 5):
            if (processedInput[i+1] == "wouldnt" and processedInput[i+2] == "get" and processedInput[i+3] == "this" and processedInput[i+4] == "from"):
              i+=5
              play("you-wouldnt-get-this-from.mp3")
              continue
      if (len(processedInput) == 3):
        if (processedInput[i] == "make" and processedInput[i+1] == "you" and processedInput[i+2] == "cry"):
          i+=3
          play("make-you-cry.mp3")
          continue

        if (processedInput[i] == "let" and processedInput[i+1] == "you" and processedInput[i+2] == "down"):
          i+=3
          play("let-you-down.mp3")
          continue

        if (processedInput[i] == "how" and processedInput[i+1] == "im" and processedInput[i+2] =="feeling"):
          play("how-im-feeling.mp3")
          i+=3
          continue

        if processedInput[i] == "gotta" and processedInput[i+1] == "make" and processedInput[i+2] == "you":
          play("gotta-make-you.mp3")
          i += 3
          continue

        if (processedInput[i] == "get" and processedInput[i+1] == "this" and processedInput[i+2] == "from"):
          i+=3
          play("get-this-from.mp3")
          continue

        if processedInput[i] == "any" and processedInput[i+1] == "other" and processedInput[i+2] == "guy":
          i+=3
          play("any-other-guy.mp3")
          continue

      if (len(processedInput) == 5):
        if (processedInput[i] == "is" and processedInput[i+1] == "what" and processedInput[i+2] == "im" and processedInput[i+3] == "thinking" and processedInput[i+4] == "of"):
          i+=5
          play("is-what-im-thinking-of.mp3")
          continue

      if len(processedInput) >= 2:
        if (processedInput[i] == "i" and processedInput[i+2] == "just"):
          if len(processedInput) >= 4:
            if (processedInput[i+3] == "want" and processedInput[i+4] == "to"):
              if len(processedInput) >= 6:
                if (processedInput[i+5] == "tell" and processedInput[i+6] == "you"):
                  if (len(processedInput) >= 10):
                    if (processedInput[i+7] == "how" and processedInput[i+8] == "im" and processedInput[i+9] == "feeling"):
                      play("i-just-wanna-tell-you-how-im-feeling.mp3")
                      i+= 10
                      continue
                  play("i-just-wanna-tell-you.mp3")
                  i+= 7
                  continue
              play("i-just-wanna.mp3")
              i+=5
              continue
          
          if (len(processedInput) >= 3):
            if (processedInput[i+3] == "wanna"):
              if (len(processedInput) >= 5):
                if (processedInput[i+4] == "tell" and processedInput[i+5] == "you"):
                  if (len(processedInput)) == 9:
                    if (processedInput[i+6] == "how" and processedInput[i+7] == "im" and processedInput[i+8] == "feeling"):
                      play("i-just-wanna-tell-you-how-im-feeling.mp3")
                      i+= 9
                      continue

                  # IM LOSING  MY SANINITYTYRYRIFRE*RYFIqwuifqewio9h
                  play("i-just-wanna-tell-you.mp3")
                  i+= 6
                  continue
              play("i-just-wanna.mp3")
              i+=4
              continue

      # Calling it a night here icl.

      if processedInput[i] == "gonna":
        if processedInput[i+1] == "make" and processedInput[i+2] == "you" and processedInput[i+3] == "understand":
          play("gonna-make-you-understand.mp3")
          i += 4
          continue
        if processedInput[i+1] == "let" and processedInput[i+2] == "you" and processedInput[i+3] == "down":
          play("gonna-let-you-down.mp3")
          i += 4
          continue
        if (processedInput[i + 1 ] == "give"):
          if (processedInput[i+2] == "you" and processedInput[i+3] == "up"):
            i+= 4
            play("gonna-give-you-up.mp3")
            continue
          if (processedInput[i+2] == "up"):
            i+= 3
            play("gonna-give-up.mp3")
            continue

      
      if processedInput[i] == "a" and processedInput[i+1] == "full" and processedInput[i+2] == "commitments" and processedInput[i+3] == "what" and processedInput[i+4] == "im" and processedInput[i+5] == "thinking" and processedInput[i+6] == "of":
        i+=7
        play("a-full-commitments-what-im-thinking-of.mp3")
        continue


      engine.say(processedInput[i])
      engine.runAndWait()

      i += 1

