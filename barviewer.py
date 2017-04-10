
#barviewer.py

import pygame
from barchart import BarChart
import fruit_model
#import gradesmodel

pygame.init()

screen = pygame.display.set_mode((1000,600))

pygame.display.set_caption("Bar Chart Viewer")
pygame.display.update()


data1 = fruit_model.get_data()
data2 = fruit_model.get_sorted_data()

screen_rect = screen.get_rect()
bc1_rect = pygame.Rect(screen_rect.x, screen_rect.y,
        screen_rect.width, screen_rect.height/2)
bc2_rect = pygame.Rect(screen_rect.x, screen_rect.y + screen_rect.height/2,
        screen_rect.width, screen_rect.height/2)

bc1 = BarChart(bc1_rect, data1)
bc2 = BarChart(bc2_rect, data2)

# display loop
done = False
while not done:
        screen.fill((0,0,0))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        bc1.draw(screen)
        bc2.draw(screen)
        pygame.display.update()
