import pygame

pygame.init()

screen = pygame.display.set_mode((750, 750))

background = pygame.image.load("Images/background.png").convert()
background = pygame.transform.scale(background,(750,750))

rick = pygame.image.load("Images/rick.png").convert_alpha()
rick = pygame.transform.scale(rick, (750,750))

rickmouth = pygame.image.load("Images/rickmouth.png").convert_alpha()
rickmouth = pygame.transform.scale(rickmouth, (750,750))

thinking = pygame.image.load("Images/thinking.png").convert_alpha()
thinking = pygame.transform.scale(thinking, (400,300))

screen.blit(background, (0, 0))

running  = True

mouthLocation = [0,0]
direction = False # False for down

talking = False
isThinking = True

def moveMouth(direction):
  if (talking):
    if (direction):
      mouthLocation[1] -= 1
    else:
      mouthLocation[1] += 1

  while running:  
    # Load images initially
    screen.blit(background, (0,0))
    screen.blit(rick, (0,0))
    screen.blit(rickmouth, (mouthLocation[0], mouthLocation[1]))

    if (isThinking):
      screen.blit(thinking, (200,450))
    else:
      screen.blit(thinking, (6969,6969))

    moveMouth(direction)

    if (mouthLocation[1] % 50) == 0:
      direction = not direction

    for event in pygame.event.get():  
      if event.type == pygame.QUIT:  
        running = False
    pygame.display.update()