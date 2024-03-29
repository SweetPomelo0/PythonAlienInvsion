class Settings():
    '''存储外星人入侵的所有设置的类'''

    def __init__(self):
        '''初始化游戏的设置'''

        #屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255,255,255)

        #飞船的设置
        self.ship_limit = 3

        #以什么速度加快游戏节奏
        # self.ship_speed_factor = 1.5
        self.speedup_scale = 2
        #外星人点数提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        #子弹设置
        # self.bullet_speed_factor = 2
        self.bullet_width = 1
        self.bullet_height = 15
        self.bullet_color =60,60,60
        self.bullets_allowed = 3

        #外星人设置
        # self.alien_speed_factor = 3
        self.fleet_drop_speed = 3
        #fleet_direction为1表示向左移，-1表示向右移
        # self.fleet_direction = 1
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 3
        # fleet_direction为1表示向左移，-1表示向右移
        self.fleet_direction = 1

        #计分
        self.alien_points = 10

    def increase_speed(self):
        '''提高速度设置'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

