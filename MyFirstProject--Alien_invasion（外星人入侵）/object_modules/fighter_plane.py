'''
fighter-plane 战斗机类的定义
'''
import pygame


class FighterPlane():
    '''
    定义战斗机的相关属性和方法
    '''

    def __init__(self,game_settings,screen):
        self.screen = screen
        self.game_settings = game_settings

        # 加载战斗机bmp位图
        self.image = pygame.image.load("C:/Users/lei.guo/PycharmProjects/MyFirstProject--Alien_invasion（外星人入侵）/images/Fighter-plane2.bmp")
        '''
        # 获取飞机图像的外接矩形，返回一个rect实例，包含以下属性：
        #     x,y
        #     top,bottom,left,right
        #     topleft, bottomleft, topright, bottomright
        #     midtop, midleft, midbottom, midright
        #     center, centerx, centery
        #     size, width, height
        #     w,h
        '''
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将战斗机放在屏幕的底部、居中
        self.fighter_plane_to_center()

        # 定义一个center可以存储小数的移动单元
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # 定义一个移动标志，控制飞机的移动
        self.moving_right_flag = False
        self.moving_left_flag = False
        self.moving_up_flag = False
        self.moving_down_flag = False

    def update_moving_flag(self):
         '''
         更新moving_right_flag以及控制战斗机上下左右移动
         :return:
         '''

         # 向右移动飞船
         if  self.moving_right_flag and self.rect.right < self.screen_rect.right :
             self.centerx += self.game_settings.fighter_plane_factor

         # 向左移动飞船
         elif self.moving_left_flag and self.rect.left > 0:
              self.centerx -= self.game_settings.fighter_plane_factor

         # 向上移动飞船
         elif self.moving_up_flag and self.rect.top > 0:
              self.centery -= self.game_settings.fighter_plane_factor

         # 向下移动飞船
         elif self.moving_down_flag and self.rect.bottom < self.screen_rect.bottom :
              self.centery += self.game_settings.fighter_plane_factor

        # 根据self.center的位置更新rect对象
         self.rect.centerx = self.centerx
         self.rect.centery = self.centery

    # 定义方法将战斗机位图绘制到指定的位置
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def fighter_plane_to_center(self):
        '''
        定义一个将战斗机居中的方法
        :return:
        '''
        self.rect.centerx = self.screen_rect.centerx  # 战斗机外接矩形的x坐标和屏幕外接矩形的x坐标保持一致
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom  # 战斗机底部y坐标和屏幕外接矩形底部的y坐标保持一致