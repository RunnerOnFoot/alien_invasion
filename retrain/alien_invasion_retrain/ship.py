"""Creating the Ship Class"""

import pygame


class Ship:
    """A Class to manage the ship."""

    def __init__(self, ai_game) -> None:
        """Initialize the ship and set it's starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get it's rect.
        self.image = pygame.image.load(
            r'retrain\alien_invasion_retrain\images\ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at it's current location."""
        self.screen.blit(self.image, self.rect)
