import pygame

class Hit:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.mx = 0
    self.my = 0
    self.image = pygame.image.load("HitButton.png")
    self.image = pygame.transform.scale(self.image, (200,300))
    self.himage = pygame.image.load("HitButtonHover.png")
    self.himage = pygame.transform.scale(self.himage, (200,300))
    self.w = 200
    self.h = 300

  def display(self, screen):
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
        