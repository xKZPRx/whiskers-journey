import pygame
import os


BASE_PATH = "assets/sprites/"

DIRT_BLOCK_IMG = None
GRASS_BLOCK_IMG = None


def load_image(name):
    path = os.path.join(BASE_PATH, name)
    return pygame.image.load(path).convert_alpha()


def load_assets():
    global DIRT_BLOCK_IMG, GRASS_BLOCK_IMG
    DIRT_BLOCK_IMG = load_image("dirt_block.png")
    GRASS_BLOCK_IMG = load_image("grass_block.png")
    print("loaded", DIRT_BLOCK_IMG, GRASS_BLOCK_IMG)