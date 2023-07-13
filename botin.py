import pygame 
from constantes import *


class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height,type_item=None):
        super().__init__()
        self.width = width
        self.height = height
        self.type_item = type_item
        if self.type_item == 1:
            self.image = pygame.image.load("images/item/38.png")
        elif self.type_item == 2:
            self.image = pygame.image.load("images/item/39.png")
        elif self.type_item == 3:
            self.image = pygame.image.load("images/item/51.png")
        elif self.type_item == 4:
            self.image = pygame.image.load("images/item/40.png")
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.rect)

      


    def draw(self, screen):
        
           
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
        
        screen.blit(self.image,self.rect)
 