import pygame

print('Start Setup')
pygame.init()
window = pygame.display.set_mode((800, 600))
print('End Setup')

print('Loop Setup')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close window
            quit() # end pygame
