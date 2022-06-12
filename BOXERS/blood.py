import pygame
import sys

class Blood:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("image/blood/blood1_1.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.top=20
    def update(self):
        pass
    def blitme(self):
        self.screen.blit(self.image, (self.rect.left, self.rect.top))

class Blood1(Blood):
    def __init__(self, screen, player):
        super().__init__(screen)
        self.rect.right = 250
        self.player=player

    def update(self):
        super().update()
        if self.player.life==100:           #根据血量值更新血量条
            self.image = pygame.image.load("image/blood/blood1_1.png")
        if self.player.life<100 and self.player.life>=80:
            self.image = pygame.image.load("image/blood/blood1_2.png")
        if self.player.life < 80 and self.player.life >= 60:
            self.image = pygame.image.load("image/blood/blood1_3.png")
        if self.player.life < 60 and self.player.life >= 40:
            self.image = pygame.image.load("image/blood/blood1_4.png")
        if self.player.life < 40 and self.player.life >= 20:
            self.image = pygame.image.load("image/blood/blood1_5.png")
        if self.player.life < 20 and self.player.life >0:
            self.image = pygame.image.load("image/blood/blood1_6.png")
        if self.player.life <= 0:
            self.image = pygame.image.load("image/blood/blood1_7.png")


class Blood2(Blood):
    def __init__(self, screen, player):
        super().__init__(screen)
        self.rect.right = 970
        self.rect.top = 18
        self.player = player

    def update(self):
        super().update()
        if self.player.life == 100:
            self.image = pygame.image.load("image/blood/blood2_1.png")
        if self.player.life < 100 and self.player.life >= 80:
            self.image = pygame.image.load("image/blood/blood2_2.png")
        if self.player.life < 80 and self.player.life >= 60:
            self.image = pygame.image.load("image/blood/blood2_3.png")
        if self.player.life < 60 and self.player.life >= 40:
            self.image = pygame.image.load("image/blood/blood2_4.png")
        if self.player.life < 40 and self.player.life >= 20:
            self.image = pygame.image.load("image/blood/blood2_5.png")
        if self.player.life < 20 and self.player.life > 0:
            self.image = pygame.image.load("image/blood/blood2_6.png")
        if self.player.life <= 0:
            self.image = pygame.image.load("image/blood/blood2_7.png")
