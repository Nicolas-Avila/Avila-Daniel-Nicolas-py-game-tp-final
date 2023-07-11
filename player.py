import pygame
from constantes import *
from auxiliar import Auxiliar
from bulletbn import *
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100,enemy=None,item=None) -> None:
        super().__init__()
        '''
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk.png",15,1,scale=p_scale)[:12]
        '''
        
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/stay/{0}.png",0,5,flip=False,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/stay/{0}.png",0,5,flip=True,scale=p_scale)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/jump/{0}.png",0,9,flip=False,scale=p_scale)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/jump/{0}.png",0,9,flip=True,scale=p_scale)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/walk/{0}.png",0,5,flip=False,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/walk/{0}.png",0,5,flip=True,scale=p_scale)

        
        self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/shoot/{0}.png",0,9,flip=False,scale=p_scale)
        self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/shoot/{0}.png",0,9,flip=True,scale=p_scale)
       # self.knife_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/mariposa/{0}.png",0,119,flip=False,scale=p_scale)
       # self.knife_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/mariposa/{0}.png",0,119,flip=True,scale=p_scale)

        self.damage_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/damage/{0}.png",1,3,flip=False,scale=p_scale)
        self.damage_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/damage/{0}.png",1,3,flip=True,scale=p_scale)

        self.dead_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/dead/{0}.png",0,17,flip=False,scale=p_scale)
        self.dead_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/dead/{0}.png",0,17,flip=True,scale=p_scale)

        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.enemy = enemy
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/1.5,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H 
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H
        self.attack_shoot = False
        self.bullet = pygame.sprite.Group()
        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False
        self.is_damage = False
        self.is_dead = False

        self.item = item
        self.type_item = pygame.sprite.Group(item)
        

        self.invulnerable = False  # Variable de estado de invulnerabilidad
        self.invulnerable_timer = 0  # Temporizador de invulnerabilidad
        self.invulnerable_duration = 600  # Duración en milisegundos de la invulnerabilidad

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

    def walk(self,direction):
        if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l) ):
            self.frame = 0
            self.direction = direction
            if(direction == DIRECTION_R):
                self.move_x = self.speed_walk
                self.animation = self.walk_r
            else:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l

    def shoot(self,on_off = True):
        self.is_shoot = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):

            if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                self.frame = 0
                self.is_shoot = True
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_r
                else:
                    self.animation = self.shoot_l       



    def knife(self,on_off = True):
        self.is_knife = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.knife_r and self.animation != self.knife_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.knife_r
                    self.frame = 0
                else:
                    self.animation = self.knife_l    
                    self.frame = 0  

    def jump(self,on_off = True):
        if(on_off and self.is_jump == False and self.is_fall == False):
            
            self.y_start_jump = self.rect.y
            self.frame = 0
            self.is_jump = True

            if(self.direction == DIRECTION_R):
                self.move_x = int(self.move_x / 1)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
                self.frame = 0
            else:
                self.move_x = int(self.move_x / 1)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
                self.frame = 0
            

        if(on_off == False and self.is_fall == True):
            self.is_jump = False
            self.stay()

    def stay(self):
        if(self.is_knife or self.is_shoot):
            return

        if(self.animation != self.stay_r and self.animation != self.stay_l and self.is_dead == False):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def change_x(self, delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self, delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if (self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump:
                self.move_y = 0

            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if not self.is_on_plataform(plataform_list):
                if self.move_y == 0:
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if self.is_jump:
                    self.jump(False)
                self.is_fall = False     
     

    def is_on_plataform(self,plataform_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno                 

    def do_animation(self, delta_ms, player):
        self.tiempo_transcurrido_animation += delta_ms
        if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
            self.tiempo_transcurrido_animation = 0
            if self.frame < len(self.animation) - 1:
                self.frame += 1
            elif self.frame >= len(self.animation) - 1 :
                if self.animation==self.dead_r or self.animation==self.dead_l:
                    del player
                else:
                    self.frame=0



    def recibir_ataque(self):
        '''
        Reduce la vida del jugador cuando es alcanzado por un ataque.
        '''
        current_time = pygame.time.get_ticks()
        if not self.invulnerable or current_time - self.invulnerable_timer > self.invulnerable_duration:
            self.lives -= 1
            self.score -=2
            # print(self.lives)
            self.invulnerable = True
            self.invulnerable_timer = current_time
        if self.is_dead == False:
            if (self.animation != self.damage_r and self.animation != self.damage_l and self.is_dead == False):
                self.frame = 0
                self.is_damage = True
                if (self.direction == DIRECTION_R):
                    self.animation = self.damage_r
                    self.move_x = 0
                else:
                    self.animation = self.damage_l
                    self.move_x = 0

    def lanzar_objeto(self):
        '''
        Lanza un objeto desde la posición central del jugador en la dirección actual.
        '''        
        objeto = Bullet(self.rect.centerx, self.rect.centery, self.direction, self, p_scale=0.5,type_bullet="player")
        

        if self.direction == DIRECTION_R:
            objeto.velocidad_x = objeto.velocidad
        else:
            objeto.velocidad_x = -objeto.velocidad

        self.bullet.add(objeto)

    def dead_animation(self):
        if self.is_dead == False:
            if self.lives <= 0:
                self.move_x = 0
                if (self.animation != self.dead_r and self.animation != self.dead_l):
                    self.frame += 1
                    self.is_dead = True
                    if self.direction == DIRECTION_R:
                        self.animation = self.dead_r
                    else:
                        self.animation = self.dead_l
                    



    def draw_hearts(self, screen, scale):
        heart_image = pygame.image.load("images/item/38.png")
        heart_width = heart_image.get_width() * scale
        heart_height = heart_image.get_height() * scale
        spacing = 5
        x = ANCHO_VENTANA/2-599
        y = ALTO_VENTANA/2-390
        for _ in range(self.lives):
            heart_scaled = pygame.transform.scale(heart_image, (heart_width, heart_height))
            screen.blit(heart_scaled, (x, y))
            x += heart_width + spacing
    


    def verificar_colision_enemigo(self, enemy_list):
        if self.is_dead == False:
            for enemigo in enemy_list:
                if self.rect.colliderect(enemigo.rect):
                    self.recibir_ataque()
                    if self.direction == DIRECTION_R:
                        self.change_x(-50)
                    else:
                        self.change_x(-50)

 
    def update(self, delta_ms, plataform_list,enemy_list,player):
        self.verificar_colision_enemigo(enemy_list)
        self.do_movement(delta_ms, plataform_list)
        self.do_animation(delta_ms,player)
        # self.hit_player(1)

        if self.lives <= 0:
            self.dead_animation()
            
            if (self.animation != self.damage_r and self.animation != self.damage_l and self.is_dead == False):
                self.frame = 0
                self.is_damage = True
                if (self.direction == DIRECTION_R):
                    self.animation = self.damage_r
                    self.move_x = 0
                else:
                    self.animation = self.damage_l
                    self.move_x = 0

        for objeto in self.bullet:
            colisiones_enemigos = pygame.sprite.spritecollide(objeto, self.enemy, False)
            if colisiones_enemigos:
                for enemy in colisiones_enemigos:
                    enemy.receive_shoot(self.enemy)
                    self.score += 3
                    self.attack_shoot = False
                    objeto.kill()

        colision_items = pygame.sprite.spritecollide(self, self.item, True)  # Verifica colisión con el grupo de ítems
        
        if self.is_dead == False:
            for item in colision_items:
                if item.type_item == 1:
                    self.lives += 1
                elif item.type_item == 2:
                    self.score += 999
            
            for enemy in enemy_list:
                for objeto in enemy.bullet:
                    if self.collition_rect.colliderect(objeto.rect):
                        self.recibir_ataque()
                        objeto.kill()

    
    def draw(self,screen):

        self.draw_hearts(screen,0.08)
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        

    def events(self,delta_ms,keys):
        self.tiempo_transcurrido += delta_ms


        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and self.is_dead == False):
            self.walk(DIRECTION_L)

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and self.is_dead == False):
            self.walk(DIRECTION_R)

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()  

        
        if keys[pygame.K_SPACE] and self.is_dead == False:
            if (self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump:
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido

        if(not keys[pygame.K_a]):
                self.shoot(False)  

        if(not keys[pygame.K_a]):
                self.knife(False)  

        if(keys[pygame.K_s] and not keys[pygame.K_a] and not self.attack_shoot and self.is_dead == False):
            self.move_x = 0
            self.shoot()
            self.lanzar_objeto()
            self.attack_shoot = True  
        
        if(keys[pygame.K_a] and not keys[pygame.K_s] and self.is_dead == False):
            self.move_x = 0
            self.knife()   
