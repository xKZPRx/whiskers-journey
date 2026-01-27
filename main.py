import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, BLACK_COLOR
from core.level import Level
from core.player import Player


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Whisker's Journey")
        
        self.clock = pygame.time.Clock()

        self.running = True
        self.level_index = 1

        self.load_resources()


    def load_resources(self):
        self.level = Level(self.level_index)
        self.player = Player(100, 100)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def update(self):
        self.dt = self.clock.tick(FPS) / 1000

        self.player.update(self.dt)


    def draw(self):
        self.screen.fill(BLACK_COLOR)
        self.level.draw(self.screen)
        self.player.draw(self.screen)

        pygame.display.flip()


    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()