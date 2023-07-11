import pygame
from pygame.locals import *
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from bulletbn import Bullet
from constantes import *
from botin import Item
from pause import *
import sys
from main import *

#pausa

level = pygame.image.load("images/gui/gui/0.png")
level = pygame.transform.scale(level, (250, 150))
level_rect = level.get_rect(center=(ANCHO_VENTANA /2, ALTO_VENTANA/2-210))




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
    item_group = pygame.sprite.Group()
    #crea pj
    player_1 = Player(x=100,y=590,speed_walk=10,speed_run=10,gravity=10,jump_power=40,frame_rate_ms=150,move_rate_ms=60,jump_height=140,p_scale=0.9,interval_time_jump=100,enemy = enemy, item = item_group)

    #crea npc    
    enemy_list = []
    # enemy_list.append (Enemy(x=450,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300))
    enemy_list.append (Enemy(x=600,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,num_enemy = 1,p_scale=1,interval_time_jump=300))
    enemy_list.append (Enemy(x=980,y=100,speed_walk=3,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,num_enemy = 2,p_scale=0.9,interval_time_jump=300))
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
    plataform_list.append(Plataform(x=900,y=360,width=50,height=50,type=13))
    plataform_list.append(Plataform(x=950,y=360,width=50,height=50,type=13))
    plataform_list.append(Plataform(x=1000,y=360,width=50,height=50,type=13))
    plataform_list.append(Plataform(x=1050,y=360,width=50,height=50,type=14))

   
    #item
    # Crear una instancia de Item
    item_list = []
    item_list.append(Item(400, 400, 50, 50,type_item= 1))
    item_list.append(Item(200, 500, 50, 50, type_item= 2))
    item_group.add(item_list)





    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if marco_1_rect_nivel is not None and marco_2_rect_nivel is not None :
                    if marco_1_rect_nivel.collidepoint(event.pos):
                        main()
                    elif marco_2_rect_nivel.collidepoint(event.pos):
                        player_1.pause = False

                if marco_1_rect_win is not None and marco_2_rect_win is not None:
                    if marco_1_rect_win.collidepoint(event.pos):
                        print('sos bueno')
                    if marco_2_rect_win.collidepoint(event.pos):
                       main()
                

                        

        keys = pygame.key.get_pressed()


        delta_ms = clock.tick(FPS)
        screen.blit(imagen_fondo,imagen_fondo.get_rect())

        for plataforma in plataform_list:
            plataforma.draw(screen)

        for index, enemy in enumerate(enemy_list):
            enemy.update(delta_ms, plataform_list, enemy_list, index,player_1)
            enemy.draw(screen)

            if not player_1.pause:
                enemy.bullet.update()
            enemy.bullet.draw(screen)


        for item in item_group:
            item.update()
            item.draw(screen)
        player_1.events(delta_ms,keys)
        player_1.update(delta_ms,plataform_list,enemy_list,player_1)
        player_1.draw(screen)
        player_1.bullet.update()
        player_1.bullet.draw(screen)


        if player_1.score <= 0:
            player_1.score = 0

        font_score=pygame.font.SysFont("comicsans", 40, True)
        score_text = font_score.render("Score: " + str(player_1.score), True, (255, 255, 255))
        screen.blit(score_text, (600, 5))
        font=pygame.font.SysFont("arial", 40, True)
        lives_text = font.render("Lives:", True, (255, 255, 255))
        screen.blit(lives_text, (10, 5))
            


        marco_1_rect_nivel = None
        marco_2_rect_nivel = None

        marco_1_rect_win = None
        marco_2_rect_win = None


        if player_1.pause == True:
            marco_1_rect_nivel, marco_2_rect_nivel = pause(screen)
        if player_1.win == True:
            marco_1_rect_win, marco_2_rect_win = win(screen)
 

        pygame.display.flip()



    











