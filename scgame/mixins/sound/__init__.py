import pygame
from scgame.sprite.base_sprite import BaseSprite

class SoundMixin(BaseSprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sounds = {}  # Dictionary to store sound objects
        self.playing_sounds = []  # List to track playing sound channels

    def load_sound(self, name, filepath):
        """Load a sound from a file and add it to the sounds dictionary."""
        self.sounds[name] = pygame.mixer.Sound(filepath)

    def play_sound(self, sound_name, wait=False):
        """Play a sound by name. If wait is True, block until the sound finishes."""
        if sound_name in self.sounds:
            sound = self.sounds[sound_name]
            channel = sound.play()
            if wait:
                while channel.get_busy():
                    pygame.time.delay(100)  # Wait for the sound to finish
            else:
                self.playing_sounds.append(channel)

    def stop_sounds(self):
        """Stop all currently playing sounds."""
        for channel in self.playing_sounds:
            if channel.get_busy():
                channel.stop()
        self.playing_sounds.clear()