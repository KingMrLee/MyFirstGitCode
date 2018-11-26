'''
第一个小项目：外星人入侵小游戏
'''

# 系统退出的时候需要用到模块sys中的方法
# 游戏中的小模块会用到pygame
# import sys
import pygame
from object_modules.settings import Settings
from object_modules.fighter_plane import FighterPlane
from comnfunc import game_functions as gf
from pygame.sprite import Group
# from alien import Alien
from object_modules.game_status import GameStatus

def run_game():
    '''
    游戏运行的主程序
    :return:None
    '''
    # 初始化游戏
    pygame.init()

    # 创建对象使用属性设置主屏幕
    game_settings = Settings()

    # 返回一个surface对象
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))

    # 调用caption模块设置游戏名称
    pygame.display.set_caption(game_settings.gamename)

    # 创建战斗机对象
    fighter_plane = FighterPlane(game_settings,screen)

    # 创建统计信息对象
    status = GameStatus(game_settings)

    '''
    # 创建外星人飞船对象
    alien = Alien(game_settings,screen)
    '''

    # 创建子弹对象，放在一个编组中
    bullets = Group()

    # 创建外星人飞船对象，放在一个编组中
    aliens = Group()

    # 创建外星人群
    gf.create_aliens_fleet(game_settings,screen,aliens,fighter_plane)

    # 游戏主程序
    while True:
        gf.check_events(game_settings,screen,fighter_plane,bullets)
        # 每次循环都需要更新移动标志
        fighter_plane.update_moving_flag()
        gf.update_bullets(game_settings,screen,bullets,aliens,fighter_plane)
        gf.update_aliens(game_settings,screen,status,fighter_plane,aliens,bullets)
        gf.update_screen(game_settings,screen,fighter_plane,aliens,bullets)

run_game()
    # pygame.quit()


