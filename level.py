import json
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
from level_2 import nivel_2

def load_platforms_from_json(json_file):
    with open(json_file) as file:
        data = json.load(file)
    plataforma_list = []
    for platform_data in data["plataform_list"]:
        plataforma = Plataform(
            x=platform_data["x"],
            y=platform_data["y"],
            width=platform_data["width"],
            height=platform_data["height"],
            type=platform_data["type"]
        )
        plataforma_list.append(plataforma)
    return plataforma_list

def load_enemies_from_json(json_file):
    with open(json_file) as file:
        data = json.load(file)
    enemy_list = []
    for enemy_data in data["enemy_list"]:
        enemy = Enemy(
            x=enemy_data["x"],
            y=enemy_data["y"],
            speed_walk=enemy_data["speed_walk"],
            speed_run=enemy_data["speed_run"],
            gravity=enemy_data["gravity"],
            jump_power=enemy_data["jump_power"],
            frame_rate_ms=enemy_data["frame_rate_ms"],
            move_rate_ms=enemy_data["move_rate_ms"],
            jump_height=enemy_data["jump_height"],
            num_enemy=enemy_data["num_enemy"],
            life=enemy_data["life"],
            p_scale=enemy_data["p_scale"],
            interval_time_jump=enemy_data["interval_time_jump"]
        )
        enemy_list.append(enemy)
    return enemy_list

def load_items_from_json(json_file):
    with open(json_file) as file:
        data = json.load(file)
    item_list = []
    for item_data in data["item_list"]:
        item = Item(
            x=item_data["x"],
            y=item_data["y"],
            width=item_data["width"],
            height=item_data["height"],
            type_item=item_data["type_item"]
        )
        item_list.append(item)
    return item_list

def nivel_1():

    clock = pygame.time.Clock()


    imagen_fondo = pygame.image.load("images/locations/noche.png").convert()
    imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

    enemy = pygame.sprite.Group()
    item_group = pygame.sprite.Group()

    player_1 = Player(x=100, y=590, speed_walk=10, speed_run=10, gravity=10, jump_power=40, frame_rate_ms=150, move_rate_ms=60, jump_height=140, p_scale=0.9, interval_time_jump=100, enemy=enemy, item=item_group)

    enemy_list = load_enemies_from_json("nivel_1.json")
    enemy.add(enemy_list)

    item_list = load_items_from_json("nivel_1.json")
    item_group.add(item_list)

    plataforma_list = load_platforms_from_json("nivel_1.json")

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
                        main()
                    if marco_2_rect_win.collidepoint(event.pos):
                       nivel_2() 


                if marco_5_rect_win is not None and marco_6_rect_win is not None:
                    if marco_5_rect_win.collidepoint(event.pos):
                        main()
                    if marco_6_rect_win.collidepoint(event.pos):
                       nivel_1()

        keys = pygame.key.get_pressed()
        delta_ms = clock.tick(FPS)
        screen.blit(imagen_fondo, imagen_fondo.get_rect())

        # Draw platforms
        for plataforma in plataforma_list:
            plataforma.draw(screen)

        # Update and draw enemies
        for index, enemy in enumerate(enemy_list):
            enemy.update(delta_ms, plataforma_list, enemy_list, index, player_1)
            enemy.draw(screen)
            if not player_1.pause:
                enemy.bullet.update()
            enemy.bullet.draw(screen)

        # Update and draw items
        for item in item_group:
            item.update()
            item.draw(screen)

        # Update and draw player
        player_1.events(delta_ms, keys)
        player_1.update(delta_ms, plataforma_list, enemy_list, player_1)
        player_1.draw(screen)
        player_1.bullet.update()
        player_1.bullet.draw(screen)

        # Draw score and lives
        if player_1.score <= 0:
            player_1.score = 0
            
        font_score = pygame.font.SysFont("comicsans", 40, True)
        score_text = font_score.render("Score: " + str(player_1.score), True, (255, 255, 255))
        screen.blit(score_text, (600, 5))
        font = pygame.font.SysFont("arial", 40, True)
        lives_text = font.render("Lives:", True, (255, 255, 255))
        screen.blit(lives_text, (10, 5))

        # Draw pause, win, and dead screens
        marco_1_rect_nivel = None
        marco_2_rect_nivel = None
        marco_1_rect_win = None
        marco_2_rect_win = None
        marco_5_rect_win = None
        marco_6_rect_win = None

        if player_1.pause == True:
            marco_1_rect_nivel, marco_2_rect_nivel, pause_rect = pause(screen)
        if player_1.win == True:
            marco_1_rect_win, marco_2_rect_win,win_rect = win(screen)
        if player_1.is_dead == True:
            marco_5_rect_win, marco_6_rect_win, dead_rect = dead_screen(screen)

        # Update the display
        pygame.display.flip()


