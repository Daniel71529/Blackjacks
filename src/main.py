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
h1 = Button(500, 400, "image/HitButton.png", "image/HitButtonHover.png", 150, 100)
s1 = Button(500, 100, "image/Stand.png", "image/StandHover.png", 150, 100)
plus = Button(490, 250, "image/plus.png", "image/PlusHover.png", 75, 75)
minus = Button(590, 250, "image/Minus.png", "image/MinusHover.png", 75, 75)
confirm = Button(200, 400, "image/Confirm.png", "image/ConfirmHover.png", 150, 100)
allIn = Button(540, 400, "image/AllIn.png", "image/AllInHover.png", 75, 75)
font = pygame.font.SysFont('Arial', 20)
winFont = pygame.font.SysFont('Arial', 100)
money = 200
bet = 5
betting = True
MplusB = money + bet
MminusB = money - bet
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
  global money
  global betting
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
      money = MplusB
    elif sumpoints(p) < sumpoints(d) or over(p):
      winner = "Womp Womp"
      money = MminusB
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
      betting = True
    winDisplay = winFont.render(winner, True, (0, 0, 0))
    winRect = winDisplay.get_rect()
    winRect.center = (400, 300)
    screen.blit(winDisplay, winRect)
    clickText = "Click to play again"
    clickText = font.render(clickText, True, (0, 0, 0))
    clickRect = clickText.get_rect()
    clickRect.center = (400, 400)
    screen.blit(clickText, clickRect)
    if money <= 0:
      endScreen(screen)
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

def endScreen(screen):
  e = True
  while e:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit()
    screen.fill(background_color)
    text = "Bankrupt"
    text = winFont.render(text, True, (0, 0, 0))
    rect = text.get_rect()
    rect.center = (400, 300)
    screen.blit(text, rect)
    pygame.display.flip()

def betScreen(screen):
  global bet
  global mx
  global my
  global betting
  while betting:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit()
    screen.fill(background_color)
    text = "Choose your bet"
    text = winFont.render(text, True, (0, 0, 0))
    rect = text.get_rect()
    rect.center = (400, 100)
    screen.blit(text, rect)
    mDisplay = font.render("Money: "+ str(money), True, (0, 0, 0))
    mRect = mDisplay.get_rect()
    mRect.center = (200, 300)
    screen.blit(mDisplay, mRect)
    bDisplay = font.render("Bet: "+ str(bet), True, (0, 0, 0))
    bRect = bDisplay.get_rect()
    bRect.center = (200, 350)
    screen.blit(bDisplay, bRect)
    mx, my = pygame.mouse.get_pos()
    plus.display(screen, mx, my)
    minus.display(screen, mx, my)
    allIn.display(screen, mx, my)
    confirm.display(screen, mx, my)
    if plus.function(mx, my):
      print("plus")
      if bet + 5 <= money:
        bet += 5
      pygame.time.delay(100)
    if minus.function(mx, my):
      print("minus")
      if bet - 5 >= 5:
        bet -= 5
      pygame.time.delay(100)
    if allIn.function(mx, my):
      print("all in")
      bet = money
      pygame.time.delay(100)
    if confirm.function(mx, my):
      print("confirm")
      betting = False
      pygame.time.delay(200)
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
  if betting:
    betScreen(screen)
  if start:
    pHand.append(deal())
    pHand.append(deal())
    dHand.append(deal())
    dHand.append(deal())
    start = False
  MplusB = money + bet
  MminusB = money - bet
  screen.fill(background_color)
  for i in range(len(pHand)):
    pHand[i].displayFront(x + 44 * i, y, screen)
  dHand[0].displayBack(144, y - 400, screen)
  dHand[1].displayFront(x + 88, y - 400, screen)
  pointDisplay = font.render("Hand: "+ str(point), True, (0, 0, 0))
  pointRect = pointDisplay.get_rect()
  pointRect.center = (200, 250)
  screen.blit(pointDisplay, pointRect)
  mDisplay = font.render("Money: "+ str(money), True, (0, 0, 0))
  mRect = mDisplay.get_rect()
  mRect.center = (200, 300)
  screen.blit(mDisplay, mRect)
  bDisplay = font.render("Bet: "+ str(bet), True, (0, 0, 0))
  bRect = bDisplay.get_rect()
  bRect.center = (200, 350)
  screen.blit(bDisplay, bRect)
  if bet > money:
    bet = money
  if over(pHand):
    run = False
    compare(pHand, dHand)
  point = str(sumpoints(pHand))
  mx, my = pygame.mouse.get_pos()
  s1.display(screen, mx, my)
  h1.display(screen, mx, my)
  if s1.function(mx, my):
    print("stand")
    pygame.time.delay(200)
    run = False
    compare(pHand, dHand)
  if h1.function(mx, my):
    print("hit")
    pHand.append(deal())
    pygame.time.delay(200)
  pygame.display.update()

