from core.tile import Tile
from settings import TILE_SIZE, WHITE_COLOR, YELLOW_COLOR, BLUE_COLOR, BROWN_COLOR
from core.player import Player
import core.assets as assets


class Level:
    def __init__(self, level_index):
        self.loaded = False

        self.tiles = []
        self.fishes = []
        self.keys = []
        self.doors = []
        
        self.load_level(level_index)
        

    def load_level(self, level_index):
        try:
            with open(f"levels/level{level_index}.txt", "r") as file:
                level_map = [line.strip() for line in file.readlines()]
        except Exception as e:
            return           

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
                        self.tiles.append(Tile(x * TILE_SIZE, y * TILE_SIZE, WHITE_COLOR, True, assets.DIRT_BLOCK_IMG))
                    case "2":
                        self.tiles.append(Tile(x * TILE_SIZE, y * TILE_SIZE, WHITE_COLOR, True, assets.GRASS_BLOCK_IMG))
                    case "P":
                        self.player = Player(x * TILE_SIZE, y * TILE_SIZE)
                    case "F":
                        self.fishes.append(Tile(x * TILE_SIZE, y * TILE_SIZE, BLUE_COLOR, False))
                    case "K":
                        self.keys.append(Tile(x * TILE_SIZE, y * TILE_SIZE, YELLOW_COLOR, False))
                    case "D":
                        self.doors.append(Tile(x * TILE_SIZE, y * TILE_SIZE, BROWN_COLOR, False))
                    case ".":
                        pass
                    case _:
                        print("No char match found.")

        self.width = max_x
        self.height = max_y

        self.loaded = True


    def update(self):
        for fish in self.fishes:
            if self.player.rect.colliderect(fish.rect):
                self.player.collect_fish()
                self.fishes.remove(fish)

        for key in self.keys:
            if self.player.rect.colliderect(key.rect):
                self.player.collect_key()
                self.keys.remove(key)

        for door in self.doors:
            if self.player.rect.colliderect(door.rect) and self.player.has_key:
                self.player.has_key = False
                return True
            
        return False


    def draw(self, screen, camera):
        for tile in self.tiles:
            draw_rect = camera.apply(tile.rect)
            tile.draw(screen, draw_rect)

        for fish in self.fishes:
            draw_rect = camera.apply(fish.rect)
            fish.draw(screen, draw_rect)

        for key in self.keys:
            draw_rect = camera.apply(key.rect)
            key.draw(screen, draw_rect)

        for door in self.doors:
            draw_rect = camera.apply(door.rect)
            door.draw(screen, draw_rect)