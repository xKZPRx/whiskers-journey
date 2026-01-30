import pygame
import os


BASE_PATH = "assets/sprites/"

DIRT_BLOCK_IMG = None
GRASS_BLOCK_IMG = None
KEY_IMG = None
FISH_IMG = None
GRASS_V1_IMG = None
GRASS_V2_IMG = None
GRASS_V3_IMG = None
GRASS_V4_IMG = None
FLOWERS_V1_IMG = None
FLOWERS_V2_IMG = None
ROCK_V1_IMG = None
ROCK_V2_IMG = None


def load_image(name):
    path = os.path.join(BASE_PATH, name)
    return pygame.image.load(path).convert_alpha()


def load_assets():
    global DIRT_BLOCK_IMG, GRASS_BLOCK_IMG, KEY_IMG, FISH_IMG, GRASS_V1_IMG, GRASS_V2_IMG, GRASS_V3_IMG, GRASS_V4_IMG, FLOWERS_V1_IMG, FLOWERS_V2_IMG, \
           ROCK_V1_IMG, ROCK_V2_IMG
    
    DIRT_BLOCK_IMG = load_image("dirt_block.png")
    GRASS_BLOCK_IMG = load_image("grass_block.png")
    KEY_IMG = load_image("key.png")
    FISH_IMG = load_image("fish.png")
    GRASS_V1_IMG = load_image("grass_v1.png")
    GRASS_V2_IMG = load_image("grass_v2.png")
    GRASS_V3_IMG = load_image("grass_v3.png")
    GRASS_V4_IMG = load_image("grass_v4.png")
    FLOWERS_V1_IMG = load_image("flowers_v1.png")
    FLOWERS_V2_IMG = load_image("flowers_v2.png")
    ROCK_V1_IMG = load_image("rock_v1.png")
    ROCK_V2_IMG = load_image("rock_v2.png")