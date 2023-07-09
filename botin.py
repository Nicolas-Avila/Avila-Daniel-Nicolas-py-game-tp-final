import pygame 


class Item:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.is_grabbed = False




    def draw(self, screen):
        if not self.is_grabbed:
            self.image = pygame.image.load("images/gui/set_gui_01/Pixel_Border/Elements/Element11.png")
            self.image = pygame.transform.scale(self.image,(self.width,self.height))
            
            screen.blit(self.image,(self.x,self.y))
 