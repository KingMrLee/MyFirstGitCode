'''
bullet子弹类相关属性和方法
'''

import sys
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''
    子弹类相关属性和方法
    :return:
    '''
    def __init__(self,game_settings,screen,fighter_plane):
        '''
        在飞船所处的位置创建一个子弹对象
        :param alien_settings: 游戏中相关对象的属性设置
        :param screen: 屏幕对象surface
        :param fighter_plane: 战斗机对象
        '''
        # super()继承Sprite类，通过使用精灵，可将游戏中相关的元素编组，进而同时操作编组中的所有元素。
        super().__init__()
        self.screen = screen

        # 在左上角（0,0）位置创建一个子弹的外接矩形，然后再确定其位置
        self.rect = pygame.Rect(0,0,game_settings.bullet_width,game_settings.bullet_height)
        self.rect.centerx = fighter_plane.rect.centerx
        self.rect.top = fighter_plane.rect.top

        # 存储可以用小数表示的子弹的位置y坐标
        self.y = float(self.rect.y)
        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        '''
        更新子弹的位置
        :return:
        '''
        self.y -= self.speed_factor
        # 更新表示子弹的rect外接矩形的位置
        self.rect.y = self.y

    def draw_bullets(self):
        '''
        绘制子弹，调用pygame.draw.rect(Surface, color, Rect, width=0（默认）) 方法
        :return:
        '''
        pygame.draw.rect(self.screen,self.color,self.rect)





