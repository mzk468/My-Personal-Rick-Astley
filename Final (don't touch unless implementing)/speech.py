import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 105)
engine.setProperty('voice', engine.getProperty("voices")[2].id)  # Using voice 2 for Rick

def play(filename):
  #does the thing
  print("Done")

def speak(input):
  input = input.split(".")  # Separate Strings whenever there are pauses
  for i in range(len(input)):
    input[i] = input[i].split(",")

  # Creating 1D list with everything
  processedInput = [] # 

  for a in input:
    for b in a:
      processedInput.append(b)


  for zx in processedInput:
    zx = zx.split(" ")
    
    while i < len(zx):
    
      # Okay this part will look horrendous af

      if zx[i] == "never" and zx[i+1] == "gonna":
        if (zx[i+2] == "give" and zx[i+3] == "you" and zx[i+4] == "up"):
          play("never-gonna-give-you-up.mp3")
          i = i+5
          continue
        elif (zx[i+2] == "let" and zx[i+3] == "you" and zx[i+4] == "down"):
          play("never-gonna-let-you-down.mp3")
          i = i+5
          continue
        elif (zx[i+2] == "make" and zx[i+3] == "you"):
          if (zx[i+4] == "cry"):
            play("never-gonna-make-you-cry.mp3")
            i = i+5
            continue
          play("never-gonna-make-you.mp3")
          i = i+4
          continue
        elif (zx[i+2] == "run" and zx[i+3] == "around"):
          if (zx[i+4] == "and" and zx[i+5] == "desert" and zx[i+6] == "you"):
            i = i+7
            play("never-gonna-run-around-and-desert-you.mp3")
            continue
          play("never-gonna-run-around.mp3")
          i = i+4
          continue
        elif (zx[i+2] == "say" and zx[i+3] == "goodbye"):
          i = i+4
          play("never-gonna-say-goodbye.mp3")
          continue
    
      if (zx[i] == "other" and zx[i+1] == "guy"):
        i = i+2
        play("other-guy.mp3")
        continue
      
      if (zx[i] == "say" and zx[i+1] == "goodbye"):
        i = i+2
        play("say-goodbye.mp3")
        continue

      if (zx[i] == "understand"):
        play("understand.mp3")
        i += 1
        continue

      if (zx[i] == "wouldnt" and zx[i+1] == "get" and zx[i+2] == "this" and zx[i+3] == "from"):
        play("wouldnt-get-this-from.mp3")
        i+=4
        continue

      if (zx[i] == "you"):
        if (zx[i+1] == "know" and zx[i+2] == "the" and zx[i+3] == "rules"):
          i+=4
          play("you-know-the-rules.mp3")
          continue
        if (zx[i+1] == "wouldnt" and zx[i+2] == "get" and zx[i+3] == "this" and zx[i+4] == "from"):
          i+=5
          play("you-wouldnt-get-this-from.mp3")
          continue
      
      if (zx[i] == "make" and zx[i+1] == "you" and zx[i+2] == "cry"):
        i+=3
        play("make-you-cry.mp3")
        continue

      if (zx[i] == "let" and zx[i+1] == "you" and zx[i+2] == "down"):
        i+=3
        play("let-you-down.mp3")
        continue

      if (zx[i] == "is" and zx[i+1] == "what" and zx[i+2] == "im" and zx[i+3] == "thinking" and zx[i+4] == "of"):
        i+=5
        play("is-what-im-thinking-of.mp3")
        continue

      if zx[i].lower == "$scream$":
        play("iii.mp3")
        i += 1
        continue

      if (zx[i] == "i" and zx[i+2] == "just"):
        if (zx[i+3] == "want" and zx[i+4] == "to"):
          if (zx[i+5] == "tell" and zx[i+6] == "you"):
            if (zx[i+7] == "how" and zx[i+8] == "im" and zx[i+9] == "feeling"):
              play("i-just-wanna-tell-you-how-im-feeling.mp3")
              i+= 10
              continue
            play("i-just-wanna-tell-you.mp3")
            i+= 7
            continue
          play("i-just-wanna.mp3")
          i+=5
          continue
        elif (zx[i+3] == "wanna"):
          if (zx[i+4] == "tell" and zx[i+5] == "you"):
            if (zx[i+6] == "how" and zx[i+7] == "im" and zx[i+8] == "feeling"):
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

      if (zx[i] == "how" and zx[i+1] == "im" and zx[i+2] =="feeling"):
        play("how-im-feeling.mp3")
        i+=3
        continue

      if zx[i] == "hi":
        play("hi.mp3")
        i+=1
        continue

      if zx[i] == "gotta" and zx[i+1] == "make" and zx[i+2] == "you":
        play("gotta-make-you.mp3")
        i += 3
        continue

      if zx[i] == "goodbye":
        play("goodbye.mp3")
        i+=1
        continue

      # Calling it a night here icl.

      if zx[i] == "gonna":
        if zx[i+1] == "make" and zx[i+2] == "you" and zx[i+3] == "understand":
          play("gonna-make-you-understand.mp3")
          i += 4
          continue
        if zx[i+1] == "let" and zx[i+2] == "you" and zx[i+3] == "down":
          play("gonna-let-you-down.mp3")
          i += 4
          continue
        if (zx[i + 1 ] == "give"):
          if (zx[i+2] == "you" and zx[i+3] == "up"):
            i+= 4
            play("gonna-give-you-up.mp3")
            continue
          if (zx[i+2] == "up"):
            i+= 3
            play("gonna-give-up.mp3")
            continue

      if (zx[i] == "give" and zx[i+1] == "up"):
        i+=2
        play("give-up.mp3")
        continue

      if (zx[i] == "get" and zx[i+1] == "this" and zx[i+2] == "from"):
        i+=3
        play("get-this-from.mp3")
        continue

      if zx[i] == "feeling":
        i+=1
        play("feeling.mp3")
        continue

      if zx[i] == "dessert" or zx[i] == "desert":
        i+=1
        play("dessert.mp3")
        continue
    
      if zx[i] == "cry":
        i+=1
        play("cry.mp3")
        continue

      if zx[i] == "any" and zx[i+1] == "other" and zx[i+2] == "guy":
        i+=3
        play("any-other-guy.mp3")
        continue

      if zx[i] == "a" and zx[i+1] == "full" and (zx[i+2] == "commitment" and zx[i+3] == "is" and zx[i+4] == "what" and zx[i+5] == "im" and zx[i+6] == "thinking" and zx[i+7] == "of") or (zx[i+2] == "commitments" and zx[i+3] == "what" and zx[i+4] == "im" and zx[i+5] == "thinking" and zx[i+6] == "of"):
        if (zx[i+2] == "commitment"):
          i+=8
        else:
          i+=7

        play("a-full-commitment-is-what-im-thinking-of.mp3")
        continue


      engine.say(zx)
      engine.runAndWait()

      i += 1
