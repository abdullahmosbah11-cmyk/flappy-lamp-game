import pygame
import os
import sys

def get_resource_path(relative_path):

    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class SoundManager:
    def __init__(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init()
            
        self.sounds = {}
        self.enable = True

        sound_files = {
            "flap": "assets/audio/flap.wav",
            "spark": "assets/audio/spark.wav",
            "score": "assets/audio/score.wav",
            "crash": "assets/audio/crash.wav",
            "zap": "assets/audio/zap.wav",
            "buy": "assets/audio/buy.wav"
        }

        for name, path in sound_files.items():
            full_path = get_resource_path(path)

            if os.path.exists(full_path):
                try:
                    snd = pygame.mixer.Sound(full_path)
                    snd.set_volume(0.5)
                    self.sounds[name] = snd

                except pygame.error as e:
                    print(f"Error loading {name}: {e}")
            else:
                print(f"Missing file: {full_path}")
        print("loaded sounds:", list(self.sounds.keys()))

    def play(self, name):
        if self.enable and name in self.sounds:
            self.sounds[name].play()