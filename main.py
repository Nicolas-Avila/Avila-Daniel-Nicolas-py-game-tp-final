import pygame
from constantes import *

# Inicializar Pygame
pygame.init()


pygame.display.set_caption("El bebe viejo (no es benjamin button)")
icono = pygame.image.load("images/caracters/players/stay/0.png")
pygame.display.set_icon(icono)

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

fondo = pygame.image.load("images/locations/castle.png").convert()
fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))

level = pygame.image.load("images/gui/gui/0.png")
level = pygame.transform.scale(level, (250, 150))
level_rect = level.get_rect(center=(ANCHO_VENTANA /2, ALTO_VENTANA/2-210))

marco = pygame.image.load("images/gui/gui/23.png")
marco = pygame.transform.scale(marco, (600, 500))  # Ajusta el tamaño de la imagen según sea necesario
marco_rect = marco.get_rect(center=(ANCHO_VENTANA / 2, ALTO_VENTANA / 2))

marco_1_image = pygame.image.load("images/gui/gui/num1.png")
marco_1_image = pygame.transform.scale(marco_1_image, (150, 150))
marco_1_rect = pygame.Rect(ANCHO_VENTANA / 2 -210, ALTO_VENTANA / 2-110, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

marco_2_image = pygame.image.load("images/gui/gui/num2.png")
marco_2_image = pygame.transform.scale(marco_2_image,(150,150))
marco_2_rect = pygame.Rect(ANCHO_VENTANA / 2+70, ALTO_VENTANA / 2-110, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

marco_3_image = pygame.image.load("images/gui/gui/num3.png")
marco_3_image = pygame.transform.scale(marco_3_image, (150, 150))
marco_3_rect = pygame.Rect(ANCHO_VENTANA / 2-75, ALTO_VENTANA / 2+10, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario



def main():
    # Lógica del juego
    from level import nivel_1
    from level_2 import nivel_2
    from level_3 import nivel_3
    running = True
    current_level = 0

    pygame.mixer.music.load("images/disparo.wav")
    volumen = 0.4  # Establecer el volumen deseado (en este caso, la mitad del volumen máximo)
    pygame.mixer.music.set_volume(volumen)
    pygame.mixer.music.play(loops=-1)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if marco_1_rect.collidepoint(event.pos):
                    current_level = 1 
                elif marco_2_rect.collidepoint(event.pos):
                    current_level = 2
                elif marco_3_rect.collidepoint(event.pos):
                    current_level = 3

            if event.type == pygame.USEREVENT + 1:
                pygame.mixer.music.play(loops=-1)  # Reiniciar la reproducción en bucle


        if current_level == 1:
            nivel_1()
        elif current_level == 2:
            nivel_2()
        elif current_level == 3:
            nivel_3()
        # Añade más niveles según sea necesario
    
        screen.blit(fondo, (0, 0))
        screen.blit(marco, marco_rect)
        screen.blit(marco_1_image, marco_1_rect)
        screen.blit(marco_2_image, marco_2_rect)
        screen.blit(marco_3_image, marco_3_rect)
        screen.blit(level,level_rect)

        pygame.display.flip()  # Actualizar la pantalla en cada iteración del bucle

    pygame.quit()

if __name__ == "__main__":
    main()