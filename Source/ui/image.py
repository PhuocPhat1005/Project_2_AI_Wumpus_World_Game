import pygame, sys
from pygame.locals import *
from ui.constants import *
from ui.text import *

def showGameBackground(screen, area=None):
    #https://wallpapercave.com/w/wp7326071
    #area: (pos_x, pos_y, width, height)
    background = pygame.image.load(f'ui/assets/game_background.jpg')
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
    if area == None:
        screen.blit(background, (0, 0))
    else:
        screen.blit(background, (area[0], area[1]), area)

def showMenuBackground(screen):
    #https://wallpapersafari.com/w/nLIPZf/download
    background = pygame.image.load('ui/assets/menu_background.jpg')
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.blit(background, (0, 0))

class ImageElement:
    def __init__(self, screen, cell_side=60):
        self.screen = screen
        self.cell_side = cell_side
        self.cell_size = (self.cell_side, self.cell_side)
        self.empty_img = pygame.image.load('ui/assets/empty.png')
        self.empty_img = pygame.transform.scale(self.empty_img, self.cell_size)
        self.unknown_img = pygame.image.load('ui/assets/unknown.png')
        self.unknown_img = pygame.transform.scale(self.unknown_img, self.cell_size)
        #https://www.clipartmax.com/download/m2i8A0H7b1Z5d3Z5_miner-miner-png/
        self.agent_img = pygame.image.load('ui/assets/agent.png')
        self.agent_img = pygame.transform.scale(self.agent_img, self.cell_size)
        #https://www.pngwing.com/en/free-png-nfowr/download
        self.gold_img = pygame.image.load('ui/assets/gold.png')
        self.gold_img = pygame.transform.scale(self.gold_img, self.cell_size)
        
        #https://yt3.googleusercontent.com/s_38Cu2ryXXDcK9fbfc9O-C23DZV1Lo8VgvDJbG_kRB7WctOofRD1gt-LNMGlJnx13-BaetK1w=s900-c-k-c0x00ffffff-no-rj
        self.wumpus_img = pygame.image.load('ui/assets/wumpus.png')
        self.wumpus_img = pygame.transform.scale(self.wumpus_img, self.cell_size)
        self.stench_img = pygame.image.load('ui/assets/stench.png')
        self.stench_img = pygame.transform.scale(self.stench_img, self.cell_size)
        
        #https://www.pikpng.com/pngvi/mTJTmi_ground-clipart-crack-hole-in-ground-drawing-png-download/
        self.pit_img = pygame.image.load('ui/assets/pit.png')
        self.pit_img = pygame.transform.scale(self.pit_img, self.cell_size)
        self.breeze_img = pygame.image.load('ui/assets/breeze.png')
        self.breeze_img = pygame.transform.scale(self.breeze_img, self.cell_size)

        #https://en.ac-illust.com/clip-art/22263264/poisonous-gas
        self.poisonous_gas_img = pygame.image.load('ui/assets/poisonous_gas.png')
        self.poisonous_gas_img = pygame.transform.scale(self.poisonous_gas_img, self.cell_size)
        self.whiff_img = pygame.image.load('ui/assets/whiff.png')
        self.whiff_img = pygame.transform.scale(self.whiff_img, self.cell_size)

        #https://pngtree.com/freepng/potion-mysterious-magic-potion-bottle_6838219.html
        self.healing_potion_img = pygame.image.load('ui/assets/healing_potion.png')
        self.healing_potion_img = pygame.transform.scale(self.healing_potion_img, self.cell_size)
        self.glow_img = pygame.image.load('ui/assets/glow.png')
        self.glow_img = pygame.transform.scale(self.glow_img, self.cell_size)

    
    # Show images
    def showEmpty(self, i, j, h):
        self.screen.blit(self.empty_img, (BOARD_APPEEAR_WIDTH + j*self.cell_side, BOARD_APPEEAR_HEIGHT + (h - 1 - i)*self.cell_side))
    def showUnknown(self, i, j, h):
        self.screen.blit(self.unknown_img, (BOARD_APPEEAR_WIDTH + j*self.cell_side, BOARD_APPEEAR_HEIGHT + (h - 1 - i)*self.cell_side))
    def showAgent(self, i, j, h):
        self.screen.blit(self.agent_img, (BOARD_APPEEAR_WIDTH + j*self.cell_side, BOARD_APPEEAR_HEIGHT + (h - 1 - i)*self.cell_side))
    def showGold(self, i, j, h):
        self.screen.blit(self.gold_img, (BOARD_APPEEAR_WIDTH + j*self.cell_side, BOARD_APPEEAR_HEIGHT + (h - 1 - i)*self.cell_side))
    
    def showWumpus(self, i, j, h):
        self.screen.blit(self.wumpus_img, (BOARD_APPEEAR_WIDTH + j*self.cell_side, BOARD_APPEEAR_HEIGHT + (h - 1 - i)*self.cell_side))
    def showStench(self, i, j, h):
        self.screen.blit(self.stench_img, (BOARD_APPEEAR_WIDTH + j*self.cell_side, BOARD_APPEEAR_HEIGHT + (h - 1 - i)*self.cell_side))
    
    def showPoisonousGas(self, i, j, h):
        self.screen.blit(self.poisonous_gas_img, (BOARD_APPEEAR_WIDTH + j*self.cell_side, BOARD_APPEEAR_HEIGHT + (h - 1 - i)*self.cell_side))
    def showWhiff(self, i, j, h):
        self.screen.blit(self.whiff_img, (BOARD_APPEEAR_WIDTH + j*self.cell_side, BOARD_APPEEAR_HEIGHT + (h - 1 - i)*self.cell_side))
    
    def showHealingPotion(self, i, j, h):
        self.screen.blit(self.healing_potion_img, (BOARD_APPEEAR_WIDTH + j*self.cell_side, BOARD_APPEEAR_HEIGHT + (h - 1 - i)*self.cell_side))
    def showGlow(self, i, j, h):
        self.screen.blit(self.glow_img, (BOARD_APPEEAR_WIDTH + j*self.cell_side, BOARD_APPEEAR_HEIGHT + (h - 1 - i)*self.cell_side))
    
    def showPit(self, i, j, h):
        self.screen.blit(self.pit_img, (BOARD_APPEEAR_WIDTH + j*self.cell_side, BOARD_APPEEAR_HEIGHT + (h - 1 - i)*self.cell_side))
    def showBreeze(self, i, j, h):
        self.screen.blit(self.breeze_img, (BOARD_APPEEAR_WIDTH + j*self.cell_side, BOARD_APPEEAR_HEIGHT + (h - 1 - i)*self.cell_side))
    
    def turnLeft(self):
        self.agent_img = pygame.transform.rotate(self.agent_img, 90)
    def turnRight(self):
        self.agent_img = pygame.transform.rotate(self.agent_img, -90)

class Map(ImageElement):
    def __init__(self, screen, map_data, cell_side=65):
        # Read and store map data
        self.map_data = map_data.copy()
        self.h = len(map_data)
        self.w = len(map_data[0])
        cell_side = 65
        if max(self.h, self.w) <= 5:
            cell_side = 120
        elif max(self.h, self.w) <= 10:
            cell_side = 65
        else:
            cell_side = 20
        super().__init__(screen, cell_side)
    
    def returnH(self):
        return self.h
    
    def returnCellSide(self):
        return self.cell_side
    
    def deleteGold(self, y, x):
        self.map_data[y][x][0].remove('G')
    
    def deleteWumpus(self, y, x):
        self.map_data[y][x][0].remove('W')
        if y > 0:
            self.map_data[y-1][x][1] = False
            self.showPath(y-1, x)
        if y < self.h-1:
            self.map_data[y+1][x][1] = False
            self.showPath(y+1, x)
        if x > 0:
            self.map_data[y][x-1][1] = False
            self.showPath(y, x-1)
        if x < self.w-1:
            self.map_data[y][x+1][1] = False
            self.showPath(y, x+1)
    
    def deleteHealingPotion(self, y, x):
        self.map_data[y][x][0].remove('H_P')
        if y > 0:
            self.map_data[y-1][x][4] = False
            self.showPath(y-1, x)
        if y < self.h-1:
            self.map_data[y+1][x][4] = False
            self.showPath(y+1, x)
        if x > 0:
            self.map_data[y][x-1][4] = False
            self.showPath(y, x-1)
        if x < self.w-1:
            self.map_data[y][x+1][4] = False
            self.showPath(y, x+1)
    
    def showUnknownBoard(self): # Show game board
        y = 0
        x = 0
        for y in range (0, self.h):
            for x in range (0, self.w):
                self.showUnknown(y, x, self.h)
    
    def showKnownBoard(self): # Show game board
        y = 0
        x = 0
        #[element, stench, breeze, whiff, glow]
        for y in range (0, self.h):
            for x in range (0, self.w):
                self.showEmpty(y, x, self.h)
                if 'A' in self.map_data[y][x][0]:
                    self.showAgent(y, x, self.h)
                if 'G' in self.map_data[y][x][0]:
                    self.showGold(y, x, self.h)
                if 'W' in self.map_data[y][x][0]:
                    self.showWumpus(y, x, self.h)
                if 'P' in self.map_data[y][x][0]:
                    self.showPit(y, x, self.h)
                if 'P_G' in self.map_data[y][x][0]:
                    self.showPoisonousGas(y, x, self.h)
                if 'H_P' in self.map_data[y][x][0]:
                    self.showHealingPotion(y, x, self.h)
                
                if self.map_data[y][x][1]:
                    self.showStench(y, x, self.h)
                if self.map_data[y][x][2]:
                    self.showBreeze(y, x, self.h)
                if self.map_data[y][x][3]:
                    self.showWhiff(y, x, self.h)
                if self.map_data[y][x][4]:
                    self.showGlow(y, x, self.h)
    
    def showPath(self, y, x): # Show agent move
        # y = 0
        # x = 0
        # #[element, stench, breeze, whiff, glow]
        # for y in range (0, self.h):
        #     for x in range (0, self.w):
        #         self.showEmpty(y, x, self.h)
        #         if 'A' in self.map_data[y][x][0]:
        #             self.showAgent(y, x, self.h)
        #         if 'G' in self.map_data[y][x][0]:
        #             self.showGold(y, x, self.h)
        #         if 'W' in self.map_data[y][x][0]:
        #             self.showWumpus(y, x, self.h)
        #         if 'P' in self.map_data[y][x][0]:
        #             self.showPit(y, x, self.h)
        #         if 'P_G' in self.map_data[y][x][0]:
        #             self.showPoisonousGas(y, x, self.h)
        #         if 'H_P' in self.map_data[y][x][0]:
        #             self.showHealingPotion(y, x, self.h)
                
        #         if self.map_data[y][x][1]:
        #             self.showStench(y, x, self.h)
        #         if self.map_data[y][x][2]:
        #             self.showBreeze(y, x, self.h)
        #         if self.map_data[y][x][3]:
        #             self.showWhiff(y, x, self.h)
        #         if self.map_data[y][x][4]:
        #             self.showGlow(y, x, self.h)
        #[element, stench, breeze, whiff, glow]
        self.showEmpty(y, x, self.h)
        # if 'A' in self.map_data[y][x][0]:
        #     self.showAgent(y, x, self.h)
        if 'G' in self.map_data[y][x][0]:
            self.showGold(y, x, self.h)
        if 'W' in self.map_data[y][x][0]:
            self.showWumpus(y, x, self.h)
        if 'P' in self.map_data[y][x][0]:
            self.showPit(y, x, self.h)
        if 'P_G' in self.map_data[y][x][0]:
            self.showPoisonousGas(y, x, self.h)
        if 'H_P' in self.map_data[y][x][0]:
            self.showHealingPotion(y, x, self.h)
        
        if self.map_data[y][x][1]:
            self.showStench(y, x, self.h)
        if self.map_data[y][x][2]:
            self.showBreeze(y, x, self.h)
        if self.map_data[y][x][3]:
            self.showWhiff(y, x, self.h)
        if self.map_data[y][x][4]:
            self.showGlow(y, x, self.h)