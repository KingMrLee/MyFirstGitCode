'''
游戏统计信息
'''

class GameStatus():
    '''
    游戏统计信息
    '''
    def __init__(self,game_settings):
        '''
        初始化
        '''
        self.game_settings = game_settings
        # 游戏刚开始的时候处于活动状态
        self.game_active = True
        self.reset_status()

    def reset_status(self):
        self.fighter_plane_limit = self.game_settings.fighter_plane_limit