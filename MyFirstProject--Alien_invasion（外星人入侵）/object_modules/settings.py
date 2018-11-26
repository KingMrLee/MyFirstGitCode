'''
创建一个Settings类，用于设置外星人入侵游戏相关的属性和方法，后续导入此模块即可实现代码复用
'''

class Settings():
    '''
    存储游戏中外星人、战斗机、屏幕、子弹等对象的相关固定设置
    '''
    def __init__(self):
        '''
        初始化游戏的相关设置
        '''
        # 主屏幕设置
        self.screen_width = 1600
        self.screen_height = 800
        self.bg_color = (240,240,10)
        self.gamename = 'Alien Invasion'
        # 设置飞船每次移动的单元为1.25个像素，之前默认是1像素
        self.fighter_plane_factor = 1.25
        # 子弹bullet的相关属性
        self.bullet_speed_factor = 1
        self.bullet_color = (35,35,35)
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 30
        # 外星人移动的移动单元
        self.alien_speed_factor = 1
        # fleet_direction为1表示向右移动，为-1标志向左移动，默认为-1
        self.fleet_direction = 1
        # 外星飞船向下移动的速度
        self.fleet_drop_speed = 100
        self.fighter_plane_limit = 5



