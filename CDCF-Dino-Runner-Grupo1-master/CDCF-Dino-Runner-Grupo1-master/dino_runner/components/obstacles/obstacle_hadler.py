from dino_runner.utils.constants import SMALL_CACTUS

from dino_runner.components.obstacles.cactus import Cactus


class ObstacleHandler():
    def __init__(self):
        self.obstacles = []

    def update(self, speed):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
        for obstacle in self.obstacles:
            obstacle.update(speed)

    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.Draw(screen)

