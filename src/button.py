import pygame


class Button:

  def __init__(self, x, y, image, himage):
    self.x = x
    self.y = y
    self.image = pygame.image.load(image)
    self.image = pygame.transform.scale(self.image, (150, 100))
    self.himage = pygame.image.load(himage)
    self.himage = pygame.transform.scale(self.himage, (150, 100))
    self.w = 150
    self.h = 100

  def display(self, screen, mx, my):
    if mx >= self.x and mx <= self.x + self.w and my >= self.y and my <= self.y + self.h:
      screen.blit(self.himage, (self.x, self.y))
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          return True
    else:
      screen.blit(self.image, (self.x, self.y))
      return False

  def function(self, mx, my):
    for event in pygame.event.get():
      if mx >= self.x and mx <= self.x + self.w and my >= self.y and my <= self.y + self.h and event.type == pygame.MOUSEBUTTONDOWN:
        return True
      else:
        return False
