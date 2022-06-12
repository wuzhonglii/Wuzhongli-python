import pygame
import sys
from random import randint
# 初始化pygame
pygame.init()
# 定义变量
size = width, height = 600, 400
# 加载logo图
img = pygame.image.load("钮门3.jpg")
# 获取图像的位置
position = img.get_rect()
# 创建一个主窗口
screen = pygame.display.set_mode(size)
# 标题
pygame.display.set_caption("C语言中文网")
 # 创建游戏主循环
while True:
      # 设置初始值
    site = [0, 0]
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('鼠标按下', event.pos)
            mx, my = event.pos
            pygame.draw.circle(screen, (255,255,0),(mx,my),50)
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            print('鼠标弹起')
            pass
        if event.type == pygame.MOUSEMOTION:
            print('鼠标移动')
            mx, my = event.pos
            # 随机生成 RGB 颜色值
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            pygame.draw.circle(screen, (r, g, b,), (mx, my), 50)
            # 处理完，更新显示
            pygame.display.update()
