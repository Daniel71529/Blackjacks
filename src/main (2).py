# Kevin Ying, Cormac Stone
import pygame
import random
from button import Button
from card import Card

# Initialize pygame
pygame.init()
# Set up the display
pygame.display.set_caption("Blackjack")
screen = pygame.display.set_mode((800, 600))
background_color = (54, 89, 74)
screen.fill(background_color)
pygame.display.flip()
pHand = []
dHand = []
h1 = Button(500, 400, "HitButton.png", "HitButtonHover.png")
s1 = Button(500, 100, "Stand.png", "StandHover.png")
font = pygame.font.SysFont('Arial', 20)
winFont = pygame.font.SysFont('Arial', 100)

# Randomize cards

def deal():
  return Card(random.randint(1, 4), random.randint(1, 13))

def sumpoints(hand):
  points = 0
  for card in hand:
    if card.value > 10:
      points += 10
    elif card.value == 1:
      points += 11
    else:
      points += card.value
  return points

def over(pHand):
  if sumpoints(pHand) > 21:
    return True

def compare(pHand, dHand):
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        quit()
    if sumpoints(dHand) < 17:
      dHand.append(deal())
    winner = ""
    if sumpoints(pHand) > sumpoints(dHand) and sumpoints(pHand) <= 21 or sumpoints(dHand) > 21 and sumpoints(pHand) <= 21:
      winner = "You Win!"
    elif sumpoints(pHand) < sumpoints(dHand) or over(pHand):
      winner = "Womp Womp"
    else:
      winner = "It's a draw!"
    screen.fill(background_color)
    for i in range(len(pHand)):
      pHand[i].displayFront(x + 44 * i, y, screen)
    for i in range(len(dHand)):
      dHand[i].displayFront(x + 44 * i, y - 400, screen)
    winDisplay = winFont.render(winner, True, (0, 0, 0))
    winRect = winDisplay.get_rect()
    winRect.center = (400, 300)
    screen.blit(winDisplay, winRect)
    pygame.display.flip()

def startScreen(screen):
  screen.fill(background_color)
  text = "Welcome to Blackjack!" + "\n" + "Click to start"
  text = winFont.render(text, True, (0, 0, 0))
  textRect = text.get_rect()
  textRect.center = (400, 300)
  screen.blit(text, textRect)
  pygame.display.flip()
    


# Main
run = True
start = True
s = True
x = 100
y = 450
point = 0
mx, my = 0, 0
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      quit()
  if s:
    startScreen(screen)
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        s = False
  if start:
    pHand.append(deal())
    pHand.append(deal())
    dHand.append(deal())
    dHand[0].displayBack(x, y - 400, screen)
    dHand.append(deal())
    dHand[1].displayBack(x + 44, y - 400, screen)
    start = False
  if over(pHand):
    run = False
    compare(pHand, dHand)
  point = str(sumpoints(pHand))
  screen.fill(background_color)
  for event in pygame.event.get():
    if event.type == pygame.MOUSEMOTION:
      mx, my = pygame.mouse.get_pos()
      print(mx, my)
  s1.display(screen, mx, my)
  h1.display(screen, mx, my)
  if s1.function(mx, my):
    print("stand")
    run = False
    compare(pHand, dHand)
  if h1.function(mx, my):
    print("hit")
    pHand.append(deal())
  for i in range(len(pHand)):
    pHand[i].displayFront(x + 44 * i, y, screen)
    dHand[0].displayBack(144, y - 400, screen)
    dHand[0].displayFront(x + 88, y - 400, screen)
  pointDisplay = font.render("Hand: "+ point, True, (0, 0, 0))
  pointRect = pointDisplay.get_rect()
  pointRect.center = (200, 300)
  screen.blit(pointDisplay, pointRect)    
  pygame.display.update()
