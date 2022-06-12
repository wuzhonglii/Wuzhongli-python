import sys
import pygame

class Attack(pygame.sprite.Sprite):                 #攻击特效
    def __init__(self, screen,imageload):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load(imageload)
        self.rect = self.image.get_rect()        
        self.screen_rect = screen.get_rect()
        self.switch=False                   #特效是否开启
        self.moveleft=False                     #特效是否移动
        self.moveright = False
    def update(self):                           
        pass
    def blitme(self): 
        if self.switch:
            self.screen.blit(self.image, (self.rect.left, self.rect.top))

class Andi_boom_arm(Attack):
    def __init__(self, screen):
        super().__init__(screen, 'image/andi/boom_arm.png')
        self.rect.right = 0
        self.rect.top = 50
    def update(self):
        super().update()
        if self.moveleft:
            self.rect.centerx -= 50
        if self.rect.centerx<0:
            self.switch = False


class Maxima_attack(Attack):
    def __init__(self, screen,imageload):
        super().__init__(screen, imageload)
        self.rect.right = 0
        self.rect.top = 50
    def update(self):
        super().update()


class Andi_attack(Attack):
    def __init__(self, screen, imageload):
        super().__init__(screen, imageload)
        self.rect.right = 0
        self.rect.top = 50
    def update(self):
        super().update()
