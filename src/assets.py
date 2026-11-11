import os 
import sys 
import pygame 

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base_path, relative_path)

def load_sprite(relative_path, size=None):
    full_path = resource_path(relative_path)
    image = pygame.image.load(full_path).convert_alpha()

    if size is not None:
        image = pygame.transform.scale(image, size)
    return image

def load_sprite_strip(relative_path, frame_w, frame_h, size=None):
    sheet = load_sprite(relative_path)
    sheet_w, _ = sheet.get_size()
    frames = []
    for x in range (0, sheet_w, frame_w):
        frame = pygame.Surface((frame_w, frame_h), pygame.SRCALPHA).convert_alpha()
        frame.blit(sheet, (0, 0), (x, 0, frame_w, frame_h))

        if size is not None: 
            frame = pygame.transform.scale(frame, size)
        frames.append(frame)
    return frames

