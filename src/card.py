# Kevin Ying, Charles Madsen, Daniel Luo

import pygame

class Card:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value
    self.front = pygame.image.load("CardFront.png")
    self.front = pygame.transform.scale(self.front, (150,150))
    self.back = pygame.image.load("CardBack.png")
    self.back = pygame.transform.scale(self.back, (150,150))
    self.font = pygame.font.SysFont('Arial', 20)

  def displayFront(self, x, y, screen):
    num = self.value
    suit = self.suit
    text = "txt"
    if num >= 2 and num <= 10:
      text = str(num)
    elif num == 11:
      text = "J"
    elif num == 12:
      text = "Q"
    elif num == 13:
      text = "K"
    elif num == 1:
      text = "A"
    if suit == 1:
      suit = "♠"
    elif suit == 2:
      suit = "♣"
    elif suit == 3:
      suit = "♥" #red
    elif suit == 4:
      suit = "♦" #red
    text = text + suit
    if suit == "♥" or suit == "♦":
      text = self.font.render(text, True, (255, 0, 0))
    else:
      text = self.font.render(text, True, (0, 0, 0))
    
    textRect = text.get_rect()
    textRect.center = (x, y)

    screen.blit(self.front, (x - 60, y - 40))
    screen.blit(text, textRect)
    textRect.center = (x + 33, y + 60)
    screen.blit(text, textRect)

  def displayBack(self, x, y, screen):
    screen.blit(self.back, (x - 60, y - 40))
