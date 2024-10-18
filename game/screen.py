import pygame

import game.game
from game.game import Game


class Screen:
    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_caption('Chess')
        self.screen = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height
        self.game = Game()
        self.legal_moves = []
        self.marked_figure = None

    def draw(self):
        while True:
            self.screen.fill((100, 100, 100))
            self.draw_field()
            for row in range(8):
                for column in range(8):
                    # Check which figure
                    current_element_id = self.game.field[row][column]
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
                        self.screen.blit(pygame.image.load(f"./images/{current_element}.png"),
                                         (column * self.width / 8, row * self.height / 8))

            for legal_move in self.legal_moves:
                self.mark_field(legal_move)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    x //= 100
                    y //= 100

                    if [x, y] in self.legal_moves:
                        self.game.move(self.marked_figure, [y, x])
                        self.legal_moves = []

                    else:
                        clicked_figure = self.game.field[y][x]
                        print(clicked_figure)
                        self.marked_figure = [y, x]
                        self.legal_moves = self.game.get_legal_moves(clicked_figure, x, y)

            pygame.display.update()

    def mark_field(self, square):
        self.screen.fill((85, 128, 95), pygame.Rect(square[0] * 100, square[1] * 100, 100, 100))

    def draw_field(self):
        for row in range(8):
            for column in range(8):
                if column % 2 == 0 and row % 2 == 0 or (column % 2 != 0 and row % 2 != 0):
                    self.screen.fill((64, 38, 4), pygame.Rect(row * 100, column * 100, 100, 100))
                else:
                    self.screen.fill((209, 125, 16), pygame.Rect(row * 100, column * 100, 100, 100))