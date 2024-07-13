import pygame
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
            for i in range(8):
                for s in range(8):
                    self.screen.blit(pygame.image.load("./images/bk.png"), (i * 100, s * 100))

            # self.screen.blit(pygame.image.load("./images/bb.png"), (100, 100))
            # self.screen.blit(pygame.image.load("./images/bk.png"), (90, 90))
            # self.screen.blit(pygame.image.load("./images/bn.png"), (80, 80))
            # self.screen.blit(pygame.image.load("./images/bp.png"), (70, 70))
            # self.screen.blit(pygame.image.load("./images/bq.png"), (60, 60))
            # self.screen.blit(pygame.image.load("./images/br.png"), (50, 50))
            # self.screen.blit(pygame.image.load("./images/wb.png"), (40, 40))
            # self.screen.blit(pygame.image.load("./images/wk.png"), (30, 30))
            # self.screen.blit(pygame.image.load("./images/wn.png"), (20, 20))
            # self.screen.blit(pygame.image.load("./images/wp.png"), (110, 110))
            # self.screen.blit(pygame.image.load("./images/wq.png"), (10, 10))
            # self.screen.blit(pygame.image.load("./images/wr.png"), (0, 0))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break




