import pygame
from constantes import *
 
def pause(screen):
    marco_1_image_nivel = pygame.image.load("images/gui/gui/num1.png")
    marco_1_image_nivel = pygame.transform.scale(marco_1_image_nivel, (100, 100))
    marco_1_rect_nivel = pygame.Rect(ANCHO_VENTANA / 2 -210, ALTO_VENTANA / 2-110, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

    marco_2_image_nivel = pygame.image.load("images/gui/gui/num2.png")
    marco_2_image_nivel = pygame.transform.scale(marco_2_image_nivel, (100, 100))
    marco_2_rect_nivel = pygame.Rect(ANCHO_VENTANA / 2+70, ALTO_VENTANA / 2-110, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

    marco_3_image_nivel = pygame.image.load("images/gui/gui/num3.png")
    marco_3_image_nivel = pygame.transform.scale(marco_3_image_nivel, (100, 100))
    marco_3_rect_nivel = pygame.Rect(ANCHO_VENTANA / 2-75, ALTO_VENTANA / 2+10, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

    screen.blit(marco_1_image_nivel, marco_1_rect_nivel)
    screen.blit(marco_2_image_nivel, marco_2_rect_nivel)
    screen.blit(marco_3_image_nivel, marco_3_rect_nivel)
    return marco_1_rect_nivel,marco_2_rect_nivel,marco_3_rect_nivel