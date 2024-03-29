import pygame.font

class Scoreboard():
    '''显示得分的类'''

    def __init__(self,ai_settings,screen,stats):
        '''初始化显示得分涉及的属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats =stats

        #显示得分信息的字体
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont('arial',40)

        #准备初始化得分图像
        self.prep_score()

    def prep_score(self):
        '''将得分渲染成图像'''
        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        #将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        '''在屏幕上显示得分'''
        self.screen.blit(self.score_image,self.screen_rect)















