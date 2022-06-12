import sys
import pygame
import attack

def check_heros(screen,state):
    while True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:      
                music_s = pygame.mixer.Sound('sounds/click.wav')
                music_s.play()
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if screen.get_rect().collidepoint(mouse_x, mouse_y):
                    return True
                

def check_events(hero1, hero2, attack_dict, score):
    if hero1.end==True:
        return 
    for event in pygame.event.get():  # 检测键盘鼠标事件
        if event.type == pygame.QUIT:
            sys.exit()  # 退出程序
        if event.type == pygame.KEYDOWN:
            check_keydown(event, hero1, hero2, attack_dict,score)
        if event.type == pygame.KEYUP:
            check_keyup(event, hero1, hero2, attack_dict,score)


def check_keydown(event, hero1, hero2, attack_dict,score):   #按下键
    if event.key == pygame.K_d:         #按下D键
        hero1.moving_right = True 
        hero1.moving_right_image = True
    elif event.key == pygame.K_a:       #按下A键
        hero1.moving_left = True 
    elif event.key == pygame.K_w:       #按下W键
        hero1.moving_up_image = True
        music_w = pygame.mixer.Sound('sounds/jump.wav')
        music_w.play()
    elif event.key == pygame.K_s:  # 向下扫腿
        hero1.moving_down_image = True
        attack_dict["maxima_boom_down"].rect.left = hero1.rect.right+12
        attack_dict["maxima_boom_down"].rect.top = hero1.rect.top+118
        if score == 0:
            score=1
        if score == 1 and pygame.sprite.collide_mask(hero1, hero2):
            music_s = pygame.mixer.Sound('sounds/down1.wav')
            music_s.play()
            hero2.life = hero2.life-10
            print("hero2:",end=" ")
            print(hero2.life)
    elif event.key == pygame.K_q:
        hero1.attack_arm_image = True
        attack_dict["maxima_boom_arm"].rect.left = hero1.rect.right+170
        attack_dict["maxima_boom_arm"].rect.top = hero1.rect.top+23
        if score == 0:
            score = 1
        if score == 1 and pygame.sprite.collide_mask(hero1, hero2):
            music_end = pygame.mixer.Sound('sounds/arm1.wav')
            music_end.play()
            hero2.life = hero2.life-10
            print("hero2:", end=" ")
            print(hero2.life)
    elif event.key == pygame.K_e:           #发起腿击
        hero1.attack_leg_image=True
        attack_dict["maxima_boom_leg"].rect.left = hero1.rect.right+110
        attack_dict["maxima_boom_leg"].rect.top = hero1.rect.top+23
        if score == 0:
            score = 1
        if score == 1 and pygame.sprite.collide_mask(hero1, hero2):
            music_e= pygame.mixer.Sound('sounds/leg1.wav')
            music_e.play()
            hero2.life = hero2.life-10
            print("hero2:", end=" ")
            print(hero2.life)
    elif event.key == pygame.K_r:
        hero1.escape_image=True
        music_r = pygame.mixer.Sound('sounds/escape.wav')
        music_r.play()



    if event.key==pygame.K_LEFT:
        hero2.moving_left=True
        hero2.moving_left_image=True
    if event.key == pygame.K_RIGHT:
        hero2.moving_right = True
    if event.key==pygame.K_UP:
        hero2.moving_up_image=True
        attack_dict["andi_boom_up"].rect.right = hero2.rect.left
        attack_dict["andi_boom_up"].rect.top = hero2.rect.top-50
        if score == 0:
            score = 2
        if score == 2 and pygame.sprite.collide_mask(hero1, hero2):
            music_up = pygame.mixer.Sound('sounds/leg2.wav')
            music_up.play()
            hero1.life = hero1.life-10
            print("hero1:", end=" ")
            print(hero1.life)
    if event.key == pygame.K_DOWN:
        hero2.moving_down_image=True
        attack_dict["andi_boom_down"].rect.right = hero2.rect.left
        attack_dict["andi_boom_down"].rect.top = hero2.rect.top+130
        if score == 0:
            score = 2
        if score == 2 and pygame.sprite.collide_mask(hero1, hero2):
            music_down = pygame.mixer.Sound('sounds/down1.wav')
            music_down.play()
            hero1.life = hero1.life-10
            print("hero1:", end=" ")
            print(hero1.life)
    if event.key == pygame.K_RETURN:        #发起攻击光波
        hero2.attack_arm_image=True
        music_return = pygame.mixer.Sound('sounds/arm2.wav')
        music_return.play()
        attack_dict["andi_boom_arm"].rect.right = hero2.rect.left
        attack_dict["andi_boom_arm"].rect.top = hero2.rect.top+100
        if pygame.sprite.collide_mask(attack_dict["andi_boom_arm"], hero1):
            hero1.life=hero1.life-2
            print("hero1:", end=" ")
            print(hero1.life)
    if event.key == pygame.K_SPACE:              #发起肘击
        hero2.attack_leg_image=True
        attack_dict["andi_boom_leg"].rect.right = hero2.rect.left+10
        attack_dict["andi_boom_leg"].rect.top = hero2.rect.top+40
        if score == 0:
            score = 2
        if score == 2 and pygame.sprite.collide_mask(hero1, hero2):
            music_space = pygame.mixer.Sound('sounds/arm3.wav')
            music_space.play()
            hero1.life = hero1.life-10
            print("hero1:", end=" ")
            print(hero1.life)


def check_keyup(event, hero1, hero2, attack_dict,score):        #松开键
    if event.key == pygame.K_d:         #松开D键
        hero1.moving_right =False
        hero1.moving_right_image = False
    elif event.key == pygame.K_a:       #松开A键
        hero1.moving_left = False 
    elif event.key == pygame.K_w:       #松开W键
        hero1.moving_up_image = False
    elif event.key == pygame.K_s:                   #取消向下扫腿
        hero1.moving_down_image = False
        attack_dict["maxima_boom_down"].switch = False
        if score==1:
            score=0
    elif event.key==pygame.K_q:
        hero1.attack_arm_image = False
        attack_dict["maxima_boom_arm"].switch = False
        if score == 1:
            score = 0
    elif event.key == pygame.K_e:
        hero1.attack_leg_image=False
        attack_dict["maxima_boom_leg"].switch = False
        if score == 1:
            score = 0
    elif event.key == pygame.K_r:
        hero1.escape_image=False


    if event.key == pygame.K_LEFT:
        hero2.moving_left = False
        hero2.moving_left_image = False
    if event.key == pygame.K_RIGHT:
        hero2.moving_right = False
    if event.key == pygame.K_UP:
        hero2.moving_up_image = False
        attack_dict["andi_boom_up"].switch = False
        if score == 2:
            score = 0
    if event.key == pygame.K_DOWN:
        hero2.moving_down_image = False
        attack_dict["andi_boom_down"].switch = False
        if score == 2:
            score = 0
    if event.key == pygame.K_RETURN:
        hero2.attack_arm_image = False
    if event.key == pygame.K_SPACE:                 #取消肘击
        hero2.attack_leg_image = False
        attack_dict["andi_boom_leg"].switch = False
        if score == 2:
            score=0


def update_screen(screen, hero1, hero2, attack_dict,blood1,blood2):
    bg4 = pygame.image.load("image/background.jpg")
    screen.blit(bg4, (0, 0))
    hero1.blitme()  #人物1显示
    hero2.blitme()  #人物2显示
    blood1.blitme()
    blood2.blitme()
    for item in attack_dict.keys():     #特效显示  
        attack_dict[item].blitme()
    pygame.display.update()  # 使最近绘制的屏幕可见
