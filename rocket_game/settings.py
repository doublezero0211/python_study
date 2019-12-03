class Settings():
    # 存储所有设置的类
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (1, 1, 1)
        # 飞船的设置
        self.rocket_speed_factor = 1.5
