import pygame

from code.Menu import Menu

class Game:

 def __init__(self):
     print('Start Setup')
     pygame.init()
     self.window = pygame.display.set_mode((800, 600))
     print('End Setup')

     print('Loop Setup')

 def run(self):
     while True:
         menu = Menu(self.window)
         menu.run()
         pass

         # Check for all events
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()  # Close window
                 quit()  # end pygame