import pygame
import os


BASE_PATH = "assets/sprites/"

DIRT_BLOCK_IMG = None
GRASS_BLOCK_IMG = None
KEY_IMG = None
FISH_IMG = None


def load_image(name):
    path = os.path.join(BASE_PATH, name)
    return pygame.image.load(path).convert_alpha()


def load_assets():
    global DIRT_BLOCK_IMG, GRASS_BLOCK_IMG, KEY_IMG, FISH_IMG
    DIRT_BLOCK_IMG = load_image("dirt_block.png")
    GRASS_BLOCK_IMG = load_image("grass_block.png")
    KEY_IMG = load_image("key.png")
    FISH_IMG = load_image("fish.png")