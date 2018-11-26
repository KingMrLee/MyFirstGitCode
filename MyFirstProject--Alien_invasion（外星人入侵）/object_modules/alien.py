'''
外星飞船
'''

import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    '''
    外星人对象
    '''
    def __init__(self,game_settings,screen):
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        # 加载外星飞船的图像
        self.image = pygame.image.load("C:/Users/lei.guo/PycharmProjects/MyFirstProject--Alien_invasion（外星人入侵）/images/alien.bmp")
        # 获得外星人飞船的外接矩形
        self.rect = self.image.get_rect()

        # 将外星人飞船靠屏幕左上角存放
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # self.rect.x = self.game_settings.alien_width
        # self.rect.y = self.game_settings.alien_height

        # 将外星人飞船的位置x坐标存放在可以存储小数的变量中
        self.x = float(self.rect.x)


    def blitme(self):
        '''
        将外星人飞船绘制到屏幕上
        :return:
        '''
        self.screen.blit(self.image,self.rect)

    def update(self):
        '''
        更新移动外星人的位置
        :param gamesettings:
        :return:
        '''
        self.x += (self.game_settings.alien_speed_factor * self.game_settings.fleet_direction) # 乘方向，表示向左向右移动
        self.rect.x = self.x

    def check_edges(self):
        '''
        检查外星人是否撞到屏幕边缘
        :return:
        '''
        # 先返回一个screen的rect实例
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:  # 触到右边缘
            return True # 返回True表示接触到边界
        elif self.rect.left <= 0: # 触到左边缘
            return True





