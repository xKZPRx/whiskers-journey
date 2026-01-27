from core.tile import Tile
from settings import TILE_SIZE


class Level:
    def __init__(self, level_index):
        self.tiles = []
        
        self.load_level(level_index)
        

    def load_level(self, level_index):
        with open(f"levels/level{level_index}.txt", "r") as file:
            level_map = [line.strip() for line in file.readlines()]

        for y, line in enumerate(level_map):
            for x, char in enumerate(line.strip()):
                if char == "#":
                    self.tiles.append(Tile(x * TILE_SIZE, y * TILE_SIZE))


    def draw(self, screen):
        for tile in self.tiles:
            tile.draw(screen)