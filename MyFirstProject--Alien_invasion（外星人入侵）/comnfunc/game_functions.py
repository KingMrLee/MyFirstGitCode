'''
结构化事件监控，定义函数check_events()实现；
定义函数update_screen()实现重绘屏幕和重绘飞机
'''

import sys
import pygame
from object_modules.bullet import Bullet
from object_modules.alien import Alien
from time import sleep

def check_keydown_events(event,game_settings,screen,fighter_plane,bullets):
    '''
     响应按键
    :param event:
    :param game_settings:
    :param screen:
    :param fighter_plane:
    :param bullets:
    :return:
    '''
    if event.key == pygame.K_RIGHT:
        fighter_plane.moving_right_flag = True
    elif event.key == pygame.K_LEFT:
        fighter_plane.moving_left_flag = True
    elif event.key == pygame.K_UP:
        fighter_plane.moving_up_flag = True
    elif event.key == pygame.K_DOWN:
        fighter_plane.moving_down_flag = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(game_settings, screen, fighter_plane, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,fighter_plane):
    '''
     响应松开
    :param event:
    :param fighter_plane:
    :return:
    '''
    if event.key == pygame.K_RIGHT:
        fighter_plane.moving_right_flag = False
    elif event.key == pygame.K_LEFT:
        fighter_plane.moving_left_flag = False
    elif event.key == pygame.K_UP:
        fighter_plane.moving_up_flag = False
    elif event.key == pygame.K_DOWN:
        fighter_plane.moving_down_flag = False


def check_events(game_settings,screen,fighter_plane,bullets):
    '''
    响应按键和鼠标事件
    :param game_settings:
    :param screen:
    :param fighter_plane:
    :param bullets:
    :return:
    '''
    # 监听键盘和鼠标事件,pygame.event.get是从queue（队列）中获取到event事件
    # KEYDOWN 是按键按下的时候的属性，此处代码控制监控上下左右移动的事件
    # KEYUP 是按键抬起的时候的属性，此处代码是监控上下左右移动按钮抬起的事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,game_settings,screen,fighter_plane,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,fighter_plane)

def update_screen(game_settings,screen,fighter_plane,aliens,bullets):
    '''
     实现重绘屏幕和重绘飞机
    :param game_settings:
    :param screen:
    :param fighter_plane:
    :param aliens:
    :param bullets: 子弹对象
    :return:
    '''
    # 每次循环重新绘制屏幕
    screen.fill(game_settings.bg_color)

    # 重绘屏幕的时候把战斗机绘制到屏幕上
    fighter_plane.blitme()

    '''
    # 将外星人飞船绘制到屏幕上
    alien.blitme()
    '''
    # 对编组调用 draw() 时， Pygame 自动绘制编组的每个元素，绘制位置由元素的属性 rect 决定。在这里，
    #  aliens.draw(screen) 在屏幕上绘制编组中的每个外星人。
    aliens.draw(screen)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullets()

    # 让设置屏幕可见
    pygame.display.flip()

def update_bullets(game_settings,screen,bullets,aliens,fighter_plane):
    '''
    删除已飞出屏幕外的子弹
    :param bullets:
    :return:
    '''
    bullets.update()
    # 删除已消失在屏幕外的子弹
    # 在 for 循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本。我们使用了方法 copy() 来设置 for 循环
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullets_aliens_collisions(game_settings,screen,bullets,aliens,fighter_plane)


def check_bullets_aliens_collisions(game_settings,screen,bullets,aliens,fighter_plane):
    '''
    响应子弹和外星人的碰撞
    :return:
    '''
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # 删除现有的子弹，并创建一个新的外星人群
        bullets.empty();
        create_aliens_fleet(game_settings,screen,aliens,fighter_plane)


def update_aliens(game_settings,screen,status,fighter_plane,aliens,bullets):
    '''
    检查是否有外星人位于屏幕边缘，并更新整群外星人的位置
    :param aliens:
    :return:
    '''
    check_fleet_edgs(game_settings,aliens)
    aliens.update()

    # 方法 spritecollideany() 接受两个实参：一个精灵和一个编组。它检查编组是否有成员与精灵发生了碰撞，并在找到与精灵发生了碰撞的成员后就停止遍历编组。在这里，
    # 它遍历编组 aliens ，并返回它找到的第一个与飞船发生了碰撞的外星人。如果没有发生碰撞， spritecollideany() 将返回 None ，因此❶处的 if 代码块不会执行。
    if pygame.sprite.spritecollideany(fighter_plane,aliens):
        fighter_plane_hit(game_settings,screen,status,fighter_plane,aliens,bullets)

    check_aliens_bottom(game_settings,screen,status,fighter_plane,aliens,bullets)

def fire_bullets(game_settings,screen,fighter_plane,bullets):
    '''
     发射子弹
    :param game_settings:
    :param screen:
    :param fighter_plane:
    :param bullets:
    :return:
    '''
    if len(bullets) < game_settings.bullets_allowed:
        # 按下空格的时候创建一个子弹对象
        new_bullet = Bullet(game_settings, screen, fighter_plane)
        # 将子弹对象添加到主函数中的Group编组中，后续操作
        bullets.add(new_bullet)

def get_numbers_of_aliens_x(game_settings,alien):
    '''
    计算横轴下可以容纳多少外星人
    :param game_settings:
    :param alien:
    :return: numbers_of_aliens
    '''
    available_space_x = game_settings.screen_width - 2 * alien.rect.width
    numbers_of_aliens = int(available_space_x / (2 * alien.rect.width)) - 3
    return numbers_of_aliens

def get_numbers_of_aliens_rows(game_settings,alien,fighter_plane_height):
    '''
    计算纵轴（y:垂直方向）可以容纳多少行外星人
    :param game_settings:
    :param alien:
    :param fighter_plane_height:
    :return: numbers_of_rows
    '''
    # 可用行的空间高度为：屏幕高度-第一个外星人飞船的高度-战斗机的高度-战斗机最顶部与外星人群的距离（设定为三个外星人飞船的高度）
    available_alien_rows = game_settings.screen_height - 4 * alien.rect.height - fighter_plane_height
    numbers_of_rows = int(available_alien_rows / (2 * alien.rect.height))
    return numbers_of_rows

def creat_alien(game_settings,screen,aliens,aliens_number,rows_number):
    '''
    创建一个外星人并将其放在当前行
    :param game_settings: 游戏设置
    :param screen: 屏幕surface对象
    :param aliens: 外星人编组对象
    :param aliens_number: 本行可容纳的外星人数
    :param rows_number: 垂直方向可容纳外星人的列数
    :return:返回一个外星人对象，添加到编组aliens中
    '''
    alien = Alien(game_settings,screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    alien.x = alien_width + 2 * alien_width * aliens_number
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * alien_height * rows_number

    # 将alien添加到编组Group中
    aliens.add(alien)

def create_aliens_fleet(game_settings,screen,aliens,fighter_plane):
    '''
    创建一群外星人飞船
    :param gamesettings: 游戏设置
    :param screen: 屏幕surface对象
    :param aliens: 外星人飞船编组
    :param fighter_plane: 战斗机对象
    :return:
    '''
    # 创建一个外星人，并计算当前行可以容纳多少个外星人
    alien = Alien(game_settings,screen)
    # 计算当前行可以容纳多少个外星人
    numbers_of_aliens = get_numbers_of_aliens_x(game_settings,alien)
    # 计算当前可以容纳多少列外星人
    numbers_of_rows = get_numbers_of_aliens_rows(game_settings,alien,fighter_plane.rect.height)

    # 先生成一行，然后再当前行生成一行外星人，再生成下一行的外星人
    for alien_numbers_row in range(numbers_of_rows):
        for aliens_number in range(numbers_of_aliens):
            creat_alien(game_settings,screen,aliens,aliens_number,alien_numbers_row)

# 在飞船触碰到边缘的时候，飞船向下移动，并改变运动方向
def check_fleet_direction(game_settings,aliens):
    '''
    控制外星人移动的方向
    :param game_settings:
    :param aliens:
    :return:
    '''
    #  sprites() :返回一个list,包含Group中所有的元素
    #     list of the Sprites this Group contains
    #     sprites() -> sprite_list
    #     Return a list of all the Sprites this group contains. You can also get an iterator from the group,
    #     but you cannot iterator over a Group while modifying it.
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed

    game_settings.fleet_direction *= -1


def check_fleet_edgs(game_settings,aliens):
    '''
    检查外星人舰队是否接触到边缘，如果接触到边缘，则向下移动，改变移动方向
    :param game_settings:
    :param aliens:
    :return:
    '''
    for alien in aliens.sprites():
        if alien.check_edges():
            check_fleet_direction(game_settings,aliens)
            break  # 改变方向之后跳出循环

def fighter_plane_hit(game_settings,screen,status,fighter_plane,aliens,bullets):
    '''
    响应外星人飞船撞到战斗机时候的事件
    :return:
    '''
    # 如果外星人飞船撞到战斗机，战斗机数量-1
    if status.fighter_plane_limit > 0:
        status.fighter_plane_limit -= 1
    else:
        status.game_active = False

    # 生成之前首先清空外星人和子弹编组，防止内存消耗
    aliens.empty()
    bullets.empty()

    # 重新生成新的外星人群
    create_aliens_fleet(game_settings,screen,aliens,fighter_plane)

    # 战斗机位置重置为屏幕中央
    fighter_plane.fighter_plane_to_center()

    # sleep 0.5秒
    # sleep(0.5)

def check_aliens_bottom(game_settings,screen,status,fighter_plane,aliens,bullets):
    '''
    检测外星人是够触碰到屏幕底部
    :return:
    '''
    # 检测外星人是够触碰到屏幕底部
    screen_rect = screen.get_rect()

    # 如果触碰到底部，与触碰到飞机效果一致，飞机可用数量-1，重新生成外星人群，飞机重置位置,调用fighter_plane_hit方法
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            fighter_plane_hit(game_settings,screen,status,fighter_plane,aliens,bullets)
            # 有外星人撞到底部就调出循环
            break







    #








