import pygame


class Screen:
    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_caption('Simulation')
        self.screen = pygame.display.set_mode((width, height))

    def draw(self):
        while True:
            self.screen.fill((100, 100, 100))

            self.screen.blit(pygame.image.load("C:/Users/Artem/PycharmProjects/python/Chess/images/bb.png"), (100, 100))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break


screen = Screen(1000, 1000)
screen.draw()
