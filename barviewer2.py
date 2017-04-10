
#barviewer2.py

import pygame
from barchart import BarChart
from button import Button
import fruit_model


# add to barviewer2.py -- right after the imports
class DataChangeButton(Button):

        def __init__(self, text, rect, chart):
                Button.__init__(self, text, rect)
                self.chart = chart
                self.sorted = False

        def on_click(self, event):
                # we will just toggle between sorted and unsorted data
                if (self.sorted):
                        data = fruit_model.get_data()
                        self.sorted = False
                else:
                        data = fruit_model.get_sorted_data()
                        self.sorted = True
                self.chart.set_values(data)


pygame.init()

screen = pygame.display.set_mode((1000,600))

pygame.display.set_caption("Bar Chart Viewer")
pygame.display.update()

data1 = fruit_model.get_data()

screen_rect = screen.get_rect()
bc1_rect = pygame.Rect(screen_rect.x, screen_rect.y,
  screen_rect.width, screen_rect.height) # make it the full height again

bc1 = BarChart(bc1_rect, data1)


button = DataChangeButton("Change",
    pygame.Rect(10, screen_rect.height - 70, 150, 60),
    bc1)

# display loop
done = False
while not done:
        screen.fill((0,0,0))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                else:
                        button.handle_event(event)

        bc1.draw(screen)
        button.draw(screen)
        pygame.display.update()
