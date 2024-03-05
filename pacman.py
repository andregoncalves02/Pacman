from typing import Any
import pygame
from map import boards
class Pacman:

    def __init__(self):
        self.player_img = []
        for i in range(1, 5):
            self.player_img.append(pygame.transform.scale(pygame.image.load(f'imagens/{i}.png'), (45, 45)))
        self.player_x = 450
        self.player_y = 663
        self.direction = 0

    def setDir(self, direction):
        self.direction = direction



    def draw_player(self,counter, screen):
        # 0-r 1-l 2-u 3-d
        if self.direction == 0:
            screen.blit(self.player_img[counter // 5],(self.player_x, self.player_y))
        elif self.direction == 1:
            screen.blit(pygame.transform.flip(self.player_img[counter // 5], True, False),(self.player_x, self.player_y))
        elif self.direction == 2:
            screen.blit(pygame.transform.rotate(self.player_img[counter // 5], 90),(self.player_x, self.player_y))
        elif self.direction == 3:
            screen.blit(pygame.transform.rotate(self.player_img[counter // 5], 270),(self.player_x, self.player_y))

    def playerOri(self, event):
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT:
                self.setDir(0)
            if event.key == pygame.K_LEFT:
                self.setDir(1)
            if event.key == pygame.K_UP:
                self.setDir(2)
            if event.key == pygame.K_DOWN:
                self.setDir(3)