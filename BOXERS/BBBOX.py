import sys
import pygame
import game_functionns as gf
import attack
import blood





def run_game():
    pygame.init()  # 初始化背景设置 
    pygame.mixer.init()
    pygame.mixer.music.load('sounds/background.mp3')  # 加载歌曲
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()  # 播放
    pygame.display.set_caption("拳皇")
    state=True
    bg1 = pygame.image.load("image/begin.jpg")      #设置图片
    screen.blit(bg1, (0, 0))
    pygame.display.update()
    pygame.time.wait(4000)
    bg2=pygame.image.load("image/option1.jpg")          #人物1选择
    screen.blit(bg2, (0, 0))
    pygame.display.update()
    if gf.check_heros(screen,state):
       bg3 = pygame.image.load("image/option2.jpg")     #人物2选择
       screen.blit(bg3, (0, 0))
       pygame.display.update()
    if gf.check_heros(screen, state):
        pass
    while True:
        gf.update_screen(screen, player1, player2, attack_dict,blood1,blood2)  #更新屏幕
        gf.check_events(player1, player2, attack_dict, score)           #检查点击事件
        player1.update()            #更新 
        player2.update()
        blood1.update()
        blood2.update()
        for item in attack_dict.keys():
            attack_dict[item].update()
        if player1.life<=0 or player2.life<=0:      #游戏结束
            if state:
                music_end = pygame.mixer.Sound('sounds/end.wav')
                music_end.play()
                state=False
                player1.end=True
                player2.end=True
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sys.exit()

        


class Hero(pygame.sprite.Sprite):
    def __init__(self, screen, imageload):  
        pygame.sprite.Sprite.__init__(self)
        self.life=100                   #人物的生命值
        self.screen = screen
        self.image = pygame.image.load(imageload)
        self.rect = self.image.get_rect()       
        self.screen_rect = screen.get_rect()       

        self.moving_right = False       #是否向右移动
        self.moving_left = False        #是否向左移动
        self.moving_right_image=False   #是否更换向右行走动作
        self.moving_left_image = False  #是否更换向左行走动作
        self.moving_up_image = False    #是否更换向上行走动作
        self.moving_down_image = False  #是否更换向下行走动作
        #self.start_left=False
        #self.start_right=False
        self.dead=False                 #生命值是否为0
        self.end=False

    def update(self):                           # 更新人物的行走速度
        clock = pygame.time.Clock()
        if self.moving_right and self.rect.right < self.screen_rect.right and self.end==False:
            self.rect.centerx += 10
        if self.moving_left and self.rect.left > 0 and self.end == False:
            self.rect.centerx -= 10
    def blitme(self):                          #显示人物
        self.screen.blit(self.image, (self.rect.left, self.rect.top))


class Maxima(Hero):
    def __init__(self, screen):
        super().__init__(screen, 'image/maxima/stand.png')
        self.rect.left = 150
        self.rect.top = 200
        self.attack_arm_image = False
        self.attack_leg_image=False
        self.escape_image=False

    def update(self):
        super().update()
        if self.moving_right_image:  # 向右走
            self.image = pygame.image.load('image/maxima/walk_right.png')
        elif self.moving_up_image:  # 向上跳
            self.image = pygame.image.load('image/maxima/walk_up.png')
            self.rect.top = 80
        elif self.moving_down_image:  # 向下扫腿
            self.image = pygame.image.load('image/maxima/walk_down.png')
            attack_dict["maxima_boom_down"].switch = True
            self.rect.top = 310
        elif self.attack_arm_image:   #出拳
            self.image = pygame.image.load('image/maxima/attack_arm.png')
            attack_dict["maxima_boom_arm"].switch = True
            self.rect.top = 210
        elif self.attack_leg_image:   #出腿
            self.image = pygame.image.load('image/maxima/attack_leg.png')
            attack_dict["maxima_boom_leg"].switch = True
        elif self.escape_image:  # 躲避
            self.image = pygame.image.load('image/maxima/escape.png')
            self.rect.top=180
        else:
            self.image = pygame.image.load('image/maxima/stand.png')
            self.rect.top = 200
        if self.life<=0:
            self.image = pygame.image.load('image/maxima/dead.png')

class K(Hero):
    def __init__(self, screen):
        super().__init__(screen, 'image/andi/stand.png')
        self.rect.right=850
        self.rect.top=200
        self.attack_arm_image = False
        self.attack_leg_image = False
        self.escape_image = False

    def update(self):
        super().update()
        if self.moving_left_image:     #向左走
            self.image = pygame.image.load('image/andi/walk_left.png')
        elif self.moving_up_image:     #向上跳
            self.image = pygame.image.load('image/andi/walk_up.png')
            attack_dict["andi_boom_up"].switch = True
            self.rect.top = 220
        elif self.moving_down_image:   #向下扫腿
            self.image = pygame.image.load('image/andi/walk_down.png')
            attack_dict["andi_boom_down"].switch = True
            self.rect.top = 380
        elif self.attack_arm_image:    #发出攻击光波
            self.image = pygame.image.load('image/andi/attack_arm.png')
            self.rect.top = 300
            attack_dict["andi_boom_arm"].switch = True
            attack_dict["andi_boom_arm"].moveleft = True
        elif self.attack_leg_image:
            self.image = pygame.image.load('image/andi/attack_leg.png')
            attack_dict["andi_boom_leg"].switch = True
            self.rect.top = 230
        else:
            self.image = pygame.image.load('image/andi/stand.png')
            self.rect.top = 200
        if self.life <= 0:
            self.image = pygame.image.load('image/andi/dead.png')
            self.rect.top=335


screen = pygame.display.set_mode((1000, 600))       #设置屏幕
player1 = Maxima(screen)
player2 = K(screen)
score=0
attack_dict = {}
andi_boom_arm = attack.Andi_boom_arm(screen)
maxima_boom_arm = attack.Maxima_attack(screen, 'image/maxima/boom_arm.png')     #添加特效对象
maxima_boom_leg = attack.Maxima_attack(screen, 'image/maxima/boom_leg.png')
maxima_boom_down = attack.Maxima_attack(screen, 'image/maxima/boom_down.png')
andi_boom_leg = attack.Andi_attack(screen, 'image/andi/boom_leg.png')
andi_boom_up = attack.Andi_attack(screen, 'image/andi/boom_up.png')
andi_boom_down = attack.Andi_attack(screen, 'image/andi/boom_down.png')
attack_dict["andi_boom_arm"] = andi_boom_arm            #将特效加入字典
attack_dict["maxima_boom_arm"] = maxima_boom_arm
attack_dict["maxima_boom_leg"] = maxima_boom_leg
attack_dict["maxima_boom_down"] = maxima_boom_down
attack_dict["andi_boom_leg"] = andi_boom_leg
attack_dict["andi_boom_up"] = andi_boom_up
attack_dict["andi_boom_down"] = andi_boom_down
blood1 = blood.Blood1(screen, player1)          #人物1的血量
blood2 = blood.Blood2(screen, player2)          #人物2的血量
run_game()

