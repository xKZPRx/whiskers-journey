from core.tile import Tile
from settings import TILE_SIZE
from core.player import Player


class Level:
    def __init__(self, level_index):
        self.tiles = []
        
        self.load_level(level_index)
        

    def load_level(self, level_index):
        with open(f"levels/level{level_index}.txt", "r") as file:
            level_map = [line.strip() for line in file.readlines()]

        for y, line in enumerate(level_map):
            for x, char in enumerate(line.strip()):
                match char:
                    case "1":
                        self.tiles.append(Tile(x * TILE_SIZE, y * TILE_SIZE))
                    case "2":
                        self.tiles.append(Tile(x * TILE_SIZE, y * TILE_SIZE))
                    case "P":
                        self.player = Player(x * TILE_SIZE, y * TILE_SIZE)
                    case "F":
                        pass
                    case "K":
                        pass
                    case "D":
                        pass
                    case ".":
                        pass
                    case _:
                        print("No char match found.")


    def draw(self, screen):
        for tile in self.tiles:
            tile.draw(screen)