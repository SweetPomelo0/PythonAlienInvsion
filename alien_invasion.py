
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from button import Button
from game_stats import GameStats
import game_functions as gf
from scoreboard import Scoreboard
from pygame.locals import *

def run_game():

    #初始化游戏并创建一个屏幕对象

    # 初始化背景设置
    pygame.init()
    ai_settings = Settings()
    # 指定游戏窗口尺寸
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #播放背景音乐
    # pygame.mixer_music.init()
    pygame.mixer_music.load("gotime.ogg")
    pygame.mixer_music.set_volume(0.2)
    pygame.mixer_music.play()

    #创建一艘飞船
    ship = Ship(ai_settings, screen)

    #创建一个用于存储子弹和外星人的编组
    bullets = Group()
    aliens =Group()

    # #创建一个外星人
    # alien = Alien(ai_settings,screen)

    #创建外星人群
    gf.create_fleet(ai_settings,screen,aliens,ship)

    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    #创建Play按钮
    play_button = Button(ai_settings,screen,"Play")

    #创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,bullets,aliens)
            gf.update_aliens(aliens,ai_settings,ship,stats,bullets,screen)
        gf.update_screen(ai_settings,screen,ship,bullets,aliens,play_button,stats,sb)


run_game()

