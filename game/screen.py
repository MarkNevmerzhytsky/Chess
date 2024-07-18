import pygame

import game.game
from game.game import Game


class Screen:
    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_caption('Chess')
        self.screen = pygame.display.set_mode((width, height))
        self.matrix = Game().field

    def draw(self):
        while True:
            self.screen.fill((100, 100, 100))
            for row in range(8):
                for column in range(8):
                    # Check which figure
                    current_element_id = self.matrix[row][column]
                    current_element = ""


                    # Black pieces
                    if current_element_id == 1:
                        current_element = "br"
                    elif current_element_id == 2:
                        current_element = "bn"
                    elif current_element_id == 3:
                        current_element = "bb"
                    elif current_element_id == 4:
                        current_element = "bq"
                    elif current_element_id == 5:
                        current_element = "bk"
                    elif current_element_id == 7:
                        current_element = "bp"

                    # White pieces
                    if current_element_id == 11:
                        current_element = "wr"
                    elif current_element_id == 12:
                        current_element = "wn"
                    elif current_element_id == 13:
                        current_element = "wb"
                    elif current_element_id == 14:
                        current_element = "wq"
                    elif current_element_id == 15:
                        current_element = "wk"
                    elif current_element_id == 8:
                        current_element = "wp"

                    if current_element:
                        self.screen.blit(pygame.image.load(f"./images/{current_element}.png"), (column * 100, row * 100))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    x //= 100
                    y //= 100
                    clicked_figure = self.matrix[y][x]
                    print(clicked_figure)

