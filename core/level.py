from core.tile import Tile
from settings import TILE_SIZE, WHITE_COLOR, YELLOW_COLOR, BLUE_COLOR, BROWN_COLOR
from core.player import Player


class Level:
    def __init__(self, level_index):
        self.tiles = []
        
        self.load_level(level_index)
        

    def load_level(self, level_index):
        with open(f"levels/level{level_index}.txt", "r") as file:
            level_map = [line.strip() for line in file.readlines()]

        max_x = 0
        max_y = 0

        for y, line in enumerate(level_map):
            for x, char in enumerate(line.strip()):
                px = x * TILE_SIZE
                py = y * TILE_SIZE

                max_x = max(max_x, px + TILE_SIZE)
                max_y = max(max_y, py + TILE_SIZE)

                match char:
                    case "1":
                        self.tiles.append(Tile(x * TILE_SIZE, y * TILE_SIZE, WHITE_COLOR, True))
                    case "2":
                        self.tiles.append(Tile(x * TILE_SIZE, y * TILE_SIZE, WHITE_COLOR, True))
                    case "P":
                        self.player = Player(x * TILE_SIZE, y * TILE_SIZE)
                    case "F":
                        self.tiles.append(Tile(x * TILE_SIZE, y * TILE_SIZE, BLUE_COLOR, False))
                    case "K":
                        self.tiles.append(Tile(x * TILE_SIZE, y * TILE_SIZE, YELLOW_COLOR, False))
                    case "D":
                        self.tiles.append(Tile(x * TILE_SIZE, y * TILE_SIZE, BROWN_COLOR, False))
                    case ".":
                        pass
                    case _:
                        print("No char match found.")

        self.width = max_x
        self.height = max_y


    def draw(self, screen, camera):
        for tile in self.tiles:
            draw_rect = camera.apply(tile.rect)
            tile.draw(screen, draw_rect)