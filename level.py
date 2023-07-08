import pygame
from pygame.locals import *
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from bulletbn import Bullet
from constantes import *
import sys



flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)

pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption("El bebe viejo (no es benjamin button)")
icono=pygame.image.load("images/caracters/players/stay/0.png")
pygame.display.set_icon(icono)

#Se inicializa la imagen del fondo y se escala al alto y ancho de la pantalla
imagen_fondo = pygame.image.load("images/locations/castle.png").convert()
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

def nivel_1():
    enemy = pygame.sprite.Group()
    #crea pj
    player_1 = Player(x=100,y=500,speed_walk=10,speed_run=10,gravity=10,jump_power=40,frame_rate_ms=150,move_rate_ms=60,jump_height=140,p_scale=1.2,interval_time_jump=100,enemy = enemy)

    #crea npc    
    enemy_list = []
    enemy_list.append (Enemy(x=450,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300))
    enemy_list.append (Enemy(x=900,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300))
    enemy_list.append (Enemy(x=600,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300))
    enemy.add(enemy_list)        
        
    #crea plataforma
    plataform_list = []
    plataform_list.append(Plataform(x=400,y=500,width=50,height=50,type=0))
    plataform_list.append(Plataform(x=450,y=500,width=50,height=50,type=1))
    plataform_list.append(Plataform(x=500,y=500,width=50,height=50,type=2))   
    plataform_list.append(Plataform(x=600,y=430,width=50,height=50,type=12))
    plataform_list.append(Plataform(x=650,y=430,width=50,height=50,type=14))
    plataform_list.append(Plataform(x=750,y=360,width=50,height=50,type=12))
    plataform_list.append(Plataform(x=800,y=360,width=50,height=50,type=13))
    plataform_list.append(Plataform(x=850,y=360,width=50,height=50,type=13))
    plataform_list.append(Plataform(x=900,y=360,width=50,height=50,type=14))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()


        delta_ms = clock.tick(FPS)
        screen.blit(imagen_fondo,imagen_fondo.get_rect())

        for plataforma in plataform_list:
            plataforma.draw(screen)

        for index, enemy in enumerate(enemy_list):
            enemy.update(delta_ms, plataform_list, enemy_list, index)
            enemy.draw(screen)

        player_1.events(delta_ms,keys)
        player_1.update(delta_ms,plataform_list)
        player_1.draw(screen)
        player_1.bullet.update()
        player_1.bullet.draw(screen)

        



        pygame.display.flip()



    










