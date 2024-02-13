import pygame 

class Stand:


  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.mx = 0
    self.my = 0
    self.image = pygame.image.load("Stand.png")
    self.himage = pygame.image.load("StandButtonHover.png")
    self.w = self.image.get_width()
    self.h = self.image.get_height()

  def display(self, screen  ):
    if self.mx >= self.x and self.mx <= self.x + self.w and self.my >= self.y and self.my <= self.y + self.h:
      screen.blit(self.himage, (self.x, self.y))
    else:
      screen.blit(self.image, (self.x, self.y))

  def function(self):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
          self.mx, self.my = pygame.mouse.get_pos()
        if self.mx >= self.x and self.mx <= self.x + self.w and self.my >= self.y and self.my <= self.y + self.h and event.type == pygame.MOUSEBUTTONDOWN:
          return True
        else:
          return False