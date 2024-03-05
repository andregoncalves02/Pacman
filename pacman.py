from typing import Any
import pygame
class Pacman:

    def __init__(self):
        self.player_img = []
        for i in range(1, 5):
            self.player_img.append(pygame.transform.scale(pygame.image.load(f'imagens/{i}.png'), (45, 45)))
        self.player_x = 450
        self.player_y = 663
        self.direction = 0
        self.turns = [False, False, False, False]
        self.player_speed = 2

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

    def check_wall(self,board, width, height):
        self.turns = [False, False, False, False]
        centerx = self.player_x + 23
        centery = self.player_y + 24
        pixelWidth = (width // 30)
        pixelHeight = ((height - 50) // 32)
        fudge = 15

        if centerx // 30 < 29:
            if self.direction == 0:
                if board[centery // pixelHeight][(centerx + fudge) // pixelWidth] < 3:
                    self.turns[0] = True
            if self.direction == 1:
                if board[centery // pixelHeight][(centerx - fudge) // pixelWidth] < 3:
                    self.turns[1] = True
            if self.direction == 2:
                if board[(centery - fudge) // pixelHeight][centerx // pixelWidth] < 3:
                    self.turns[2] = True
            if self.direction == 3:
                if board[(centery + fudge) // pixelHeight][centerx // pixelWidth] < 3:
                    self.turns[3] = True
            if self.direction == 2 or self.direction == 3:
                if 12 <= centerx % pixelWidth <= 18:
                    if board[(centery + fudge) // pixelHeight][centerx // pixelWidth] < 3:
                        self.turns[3] = True
                    if board[(centery - fudge) // pixelHeight][centerx // pixelWidth] < 3:
                        self.turns[2] = True
                if 12 <= centery % pixelHeight <= 18:
                    if board[centery // pixelHeight][(centerx - pixelWidth) // pixelWidth] < 3:
                        self.turns[1] = True
                    if board[centery // pixelHeight][(centerx + pixelWidth) // pixelWidth] < 3:
                        self.turns[0] = True
            if self.direction == 0 or self.direction == 1:
                if 12 <= centerx % pixelWidth <= 18:
                    if board[(centery + pixelHeight) // pixelHeight][centerx // pixelWidth] < 3:
                        self.turns[3] = True
                    if board[(centery - pixelHeight) // pixelHeight][centerx // pixelWidth] < 3:
                        self.turns[2] = True
                if 12 <= centery % pixelHeight <= 18:
                    if board[centery // pixelHeight][(centerx - fudge) // pixelWidth] < 3:
                        self.turns[1] = True
                    if board[centery // pixelHeight][(centerx + fudge) // pixelWidth] < 3:
                        self.turns[0] = True
        else:
            self.turns[0] = True
            self.turns[1] = True

    def move_player(self):
        if self.direction == 0 and self.turns[0]:
            self.player_x += self.player_speed
        elif self.direction == 1 and self.turns[1]:
            self.player_x -= self.player_speed
        if self.direction == 2 and self.turns[2]:
            self.player_y -= self.player_speed
        elif self.direction == 3 and self.turns[3]:
            self.player_y += self.player_speed

        if self.player_x > 900:
            self.player_x = -47
        elif self.player_x < -50:
            self.player_x = 897