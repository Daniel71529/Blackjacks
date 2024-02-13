import pygame
import random
from hit import Hit
from stand import Stand
from card import Card

# Initialize pygame
pygame.init()
# Set up the display
pygame.display.set_caption("Blackjack")
screen = pygame.display.set_mode((800, 600))
background_color = (54,89,74)
screen.fill(background_color)
pygame.display.flip()
pHand = []
dHand = []
h1 = Hit(500, 250) 
s1 = Stand(500, 250)
# Code for BlackJack
# Randomize cards

def deal():
  return Card(random.randint(1,4), random.randint(1,13))

# Main
run = True
start = True
x = 100
y = 450
while run:
  if start:
    pHand.append(deal())
    pHand.append(deal())
    dHand.append(deal())
    dHand[0].displayBack(x, y - 400, screen)
    dHand.append(deal())
    dHand[1].displayBack(x + 44, y - 400, screen)
    start = False
  if h1.function():
    pHand.append(deal())
  screen.fill(background_color)
  h1.display(screen)
  for i in range(len(pHand)):
    pHand[i].displayFront(x + 44 * i, y, screen)
  for i in range(len(dHand)):
    pHand[i].displayBack(x + 44 * i, y - 400, screen)
  pygame.display.flip()
  
# guide: https://www.linkedin.com/pulse/building-blackjack-game-python-can-arslan