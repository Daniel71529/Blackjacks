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

def compare(p, d):
  global run
  global start
  global pHand
  global dHand
  c = True
  while c:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        quit()
    if sumpoints(d) < 17:
      d.append(deal())
    winner = ""
    if sumpoints(p) > sumpoints(d) and sumpoints(p) <= 21 or sumpoints(d) > 21 and sumpoints(p) <= 21:
      winner = "You Win!"
    elif sumpoints(p) < sumpoints(d) or over(p):
      winner = "Womp Womp"
    else:
      winner = "It's a draw!"
    screen.fill(background_color)
    for i in range(len(p)):
      pHand[i].displayFront(x + 44 * i, y, screen)
    for i in range(len(d)):
      dHand[i].displayFront(x + 44 * i, y - 400, screen)
    if pygame.mouse.get_pressed()[0]:
      pygame.time.delay(200)
      print("clicked")
      c = False
      run = True
      start = True
      pHand = []
      dHand = []
    winDisplay = winFont.render(winner, True, (0, 0, 0))
    winRect = winDisplay.get_rect()
    winRect.center = (400, 300)
    screen.blit(winDisplay, winRect)
    clickText = "Click to play again"
    clickText = font.render(clickText, True, (0, 0, 0))
    clickRect = clickText.get_rect()
    clickRect.center = (400, 400)
    screen.blit(clickText, clickRect)
    pygame.display.flip()

def startScreen(screen):
  global s
  t = True
  while t:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit()
    if pygame.mouse.get_pressed()[0]:
      pygame.time.delay(200)
      print("clicked")
      s = False
      t = False
    screen.fill(background_color)
    text = "Welcome to Blackjack!"
    text = font.render(text, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (400, 300)
    screen.blit(text, textRect)
    clickText = "Click to play"
    clickText = font.render(clickText, True, (0, 0, 0))
    clickRect = clickText.get_rect()
    clickRect.center = (400, 400)
    screen.blit(clickText, clickRect)
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
  if start:
    pHand.append(deal())
    pHand.append(deal())
    dHand.append(deal())
    dHand.append(deal())
    start = False
  if over(pHand):
    run = False
    compare(pHand, dHand)
  point = str(sumpoints(pHand))
  screen.fill(background_color)
  mx, my = pygame.mouse.get_pos()
  s1.display(screen, mx, my)
  h1.display(screen, mx, my)
  if s1.function(mx, my):
    print("stand")
    pygame.time.delay(100)
    run = False
    compare(pHand, dHand)
  if h1.function(mx, my):
    print("hit")
    pHand.append(deal())
    pygame.time.delay(100)
  if start:
    pHand.append(deal())
    pHand.append(deal())
    dHand.append(deal())
    dHand.append(deal())
    start = False
  for i in range(len(pHand)):
    pHand[i].displayFront(x + 44 * i, y, screen)
  dHand[0].displayBack(144, y - 400, screen)
  dHand[1].displayFront(x + 88, y - 400, screen)
  pointDisplay = font.render("Hand: "+ point, True, (0, 0, 0))
  pointRect = pointDisplay.get_rect()
  pointRect.center = (200, 300)
  screen.blit(pointDisplay, pointRect)    
  pygame.display.update()

