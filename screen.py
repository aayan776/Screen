import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((200,0,255))
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  pygame.display.flip()
pygame.quit()
