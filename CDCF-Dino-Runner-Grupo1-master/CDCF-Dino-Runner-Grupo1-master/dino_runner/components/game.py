from email import message
import pygame

from utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from utils import text_utils

from components.dinosuar import Dinosaur
from components.obstacles.obstacle_handler import ObstacleHandler

class Game:
    MAX_LIVES = 3
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.dinosaur = Dinosaur()
        self.obstacle_handler = ObstacleHandler()
        self.playing = False
        self.running = True
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.lives = self.MAX_LIVES

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def run(self):
        # Game loop: events - update - draw
        self.reset_attributes()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def reset_attributes(self):
        self.playing = True
        self.dinosaur = Dinosaur()
        self.obstacle_handler = ObstacleHandler()
        self.points = 0
        self.lives = self.MAX_LIVES

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        dino_event = pygame.key.get_pressed()
        self.dinosaur.update(dino_event)
        self.obstacle_handler.update(self)
        self.update_score()
        print(self.lives)

        if self.lives == 0:
            self.playing = False
            self.running = True
            self.execute()


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.dinosaur.draw(self.screen)
        self.obstacle_handler.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        message = "points: "+ str(self.points)
        points_text, points_rect = text_utils.get_text_element(message, SCREEN_WIDTH - 100, 40, 25)
        self.screen.blit(points_text, points_rect)

    def update_score(self):
        self.points += 1 
        if self.points % 100 == 0:
            self.game_speed += 1

    def show_menu(self):
        self.running = True

        black_color = (0, 0, 0)
        self.screen.fill(black_color)
        self.show_menu_options()
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                self.run()
    
    def show_menu_options(self):
        white_color = (255, 255, 255)
        if self.points > 0:
            text, text_rect = text_utils.get_text_element("Game Over", font_size=40, font_color=white_color)
        else:
            text, text_rect = text_utils.get_text_element("Press Any Key To Start", font_size=40, font_color=white_color)
        self.screen.blit(text, text_rect)



        

    
    