import pygame
from constantes import *
from auxiliar import Auxiliar
 
def pause(screen):
    
    pause = pygame.image.load("images/gui/gui/1.png")
    pause = pygame.transform.scale(pause, (150,100))
    pause_rect = pause.get_rect(center=(ANCHO_VENTANA /2-18.9, ALTO_VENTANA/2-100))

    marco_1_image_nivel = pygame.image.load("images/gui/gui/botton_red/2.png")
    marco_1_image_nivel = pygame.transform.scale(marco_1_image_nivel, (100, 50))
    marco_1_rect_nivel = pygame.Rect(ANCHO_VENTANA / 2 -210, ALTO_VENTANA / 2-20, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

    marco_2_image_nivel = pygame.image.load("images/gui/gui/botton_red/12.png")
    marco_2_image_nivel = pygame.transform.scale(marco_2_image_nivel, (100, 50))
    marco_2_rect_nivel = pygame.Rect(ANCHO_VENTANA / 2+70, ALTO_VENTANA / 2-20, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

    
    screen.blit(pause,pause_rect)
    screen.blit(marco_1_image_nivel, marco_1_rect_nivel)
    screen.blit(marco_2_image_nivel, marco_2_rect_nivel)

    
    return marco_1_rect_nivel,marco_2_rect_nivel,pause_rect

def win (screen):

    win = pygame.image.load("images/gui/gui/win.png")
    win = pygame.transform.scale(win, (1510,200))
    win_rect = win.get_rect(center=(ANCHO_VENTANA /2+5.9, ALTO_VENTANA/2-100))


    marco_1_image_win = pygame.image.load("images/gui/gui/botton_red/2.png")
    marco_1_image_win = pygame.transform.scale(marco_1_image_win, (100, 50))
    marco_1_rect_win = pygame.Rect(ANCHO_VENTANA / 2 -210, ALTO_VENTANA / 2+110, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

    marco_2_image_win = pygame.image.load("images/gui/gui/botton_red/7.png")
    marco_2_image_win = pygame.transform.scale(marco_2_image_win, (100, 50))
    marco_2_rect_win = pygame.Rect(ANCHO_VENTANA / 2+70, ALTO_VENTANA / 2+110, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

   
    screen.blit(win,win_rect)
    screen.blit(marco_1_image_win, marco_1_rect_win)
    screen.blit(marco_2_image_win, marco_2_rect_win)
    
    return marco_1_rect_win,marco_2_rect_win,win_rect

def dead_screen(screen):

    dead = pygame.image.load("images/gui/gui/dead.jpeg")
    dead = pygame.transform.scale(dead, (1510,200))
    dead_rect = dead.get_rect(center=(ANCHO_VENTANA /2+5.9, ALTO_VENTANA/2-100))

    marco_5_image_win = pygame.image.load("images/gui/gui/botton_red/2.png")
    marco_5_image_win = pygame.transform.scale(marco_5_image_win, (100, 50))
    marco_5_rect_win = pygame.Rect(ANCHO_VENTANA / 2 -210, ALTO_VENTANA / 2+110, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

    marco_6_image_win = pygame.image.load("images/gui/gui/botton_red/12.png")
    marco_6_image_win = pygame.transform.scale(marco_6_image_win, (100, 50))
    marco_6_rect_win = pygame.Rect(ANCHO_VENTANA / 2+70, ALTO_VENTANA / 2+110, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

   
    screen.blit(dead, dead_rect)
    screen.blit(marco_5_image_win, marco_5_rect_win)
    screen.blit(marco_6_image_win, marco_6_rect_win)
    
    return marco_5_rect_win,marco_6_rect_win,dead_rect