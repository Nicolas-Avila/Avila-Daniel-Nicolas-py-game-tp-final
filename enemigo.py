from player import *
from constantes import *
from auxiliar import Auxiliar
from bulletbn import *
class Enemy(pygame.sprite.Sprite):
    
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,num_enemy,life,p_scale=1,interval_time_jump=100) -> None:
        super().__init__()
        self.num_enemy = num_enemy

        if self.num_enemy == 1:    
            self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/bringer/walk/{0}.png",1,8,flip=False,scale=p_scale)
            self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/bringer/walk/{0}.png",1,8,flip=True,scale=p_scale)
            # self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/bringer/idle/{0}.png",1,8,scale=p_scale)
            # self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/bringer/idle/IDLE_00{0}.png",0,7,flip=False,scale=p_scale)

            self.dead_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/bringer/dead/{0}.png",0,10,flip=False,scale=p_scale)
            self.dead_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/bringer/dead/{0}.png",0,10,flip=True,scale=p_scale)

            self.attack_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/bringer/attack/{0}.png",0,4,flip=False,scale=p_scale)
            self.attack_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/bringer/attack/{0}.png",0,4,flip=True,scale=p_scale)
        elif self.num_enemy == 2:
            # self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/stay/{0}.png",0,5,flip=False,scale=p_scale)
            self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/archer/run/{0}.png",1,8,flip=False,scale=p_scale)
            self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/archer/run/{0}.png",1,8,flip=True,scale=p_scale)
            
            self.attack_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/archer/atk/{0}.png",0,7,flip=False,scale=p_scale)
            self.attack_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/archer/atk/{0}.png",0,7,flip=True,scale=p_scale)

            self.dead_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/archer/death/{0}.png",1,5,flip=False,scale=p_scale)
            self.dead_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/archer/death/{0}.png",1,5,flip=True,scale=p_scale)
        elif self.num_enemy == 3:
            self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/demon/individual/walk/{0}.png",1,12,flip=True,scale=p_scale)
            self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/demon/individual/walk/{0}.png",1,12,flip=False,scale=p_scale)

            self.dead_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/demon/individual/dead/{0}.png",1,22,flip=True,scale=p_scale)
            self.dead_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/demon/individual/dead/{0}.png",1,22,flip=False,scale=p_scale)

            self.attack_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/demon/individual/atack/{0}.png",1,5,flip=True,scale=p_scale)
            self.attack_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/demon/individual/atack/{0}.png",1,5,flip=False,scale=p_scale)
        elif self.num_enemy == 4:
            self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/wizard/walk/{0}.png",1,8,flip=False,scale=p_scale)
            self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/wizard/walk/{0}.png",1,8,flip=True,scale=p_scale)

            self.dead_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/wizard/dead/{0}.png",1,7,flip=False,scale=p_scale)
            self.dead_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/wizard/dead/{0}.png",1,7,flip=True,scale=p_scale)

            self.attack_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/wizard/attack/{0}.png",1,7,flip=False,scale=p_scale)
            self.attack_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/wizard/attack/{0}.png",1,7,flip=True,scale=p_scale)

        elif self.num_enemy == 5:
            self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/armelito/arme/{0}.png",0,17,flip=False,scale=p_scale)
            self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/armelito/arme/{0}.png",0,17,flip=True,scale=p_scale)

            self.dead_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/armelito/dead/{0}.png",1,3,flip=False,scale=p_scale)
            self.dead_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/armelito/dead/{0}.png",1,3,flip=True,scale=p_scale)

            self.attack_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/armelito/arme/{0}.png",0,17,flip=False,scale=p_scale)
            self.attack_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/armelito/arme/{0}.png",0,17,flip=True,scale=p_scale)

        


        self.contador = 0
        self.frame = 0
        self.lives = life
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.walk_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
       
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/1.5,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H 
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False
        self.is_dead = False
        self.check_collition = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        #self.attack_shoot = False
        self.bullet = pygame.sprite.Group()
        self.attack_cooldown = 1000 
        self.last_attack_time = pygame.time.get_ticks()

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump
   
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
    
        if self.lives > 0 :
            if(self.tiempo_transcurrido_move >= self.move_rate_ms):
                self.tiempo_transcurrido_move = 0

                if(not self.is_on_plataform(plataform_list)):
                    if(self.move_y == 0):
                        self.is_fall = True
                        self.change_y(self.gravity)
                        self.contador = 0
                else:
                    self.is_fall = False
                    self.change_x(self.move_x)
                    if self.contador <= 50:
                        self.move_x = -self.speed_walk
                        self.animation = self.walk_l
                        self.direction = DIRECTION_L
                        self.contador += 1 
                    elif self.contador <= 100 :
                        self.move_x = self.speed_walk
                        self.animation = self.walk_r
                        self.direction = DIRECTION_R
                        self.contador += 1
                    else:
                        self.contador = 0
        
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


    def shooting(self):
        Player.lanzar_objeto(self)
    
    def death_animation(self):

        self.is_dead = True
        if self.direction == DIRECTION_R:
            self.animation = self.dead_r
            self.frame = 0
        else:
            self.animation = self.dead_l
            self.frame = 0
        
        

    def do_animation(self,delta_ms, enemy_list, index):
           
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1           
            elif self.frame >= len(self.animation) - 1 :
                if self.lives <= 0:
                    del enemy_list[index]
                else:
                    self.frame=0

    def puede_atacar(self,player):
         #para atacar cuadno esta frente tuyo
        if player.rect.y == self.rect.y:
            if player.rect.x > self.rect.x and self.direction == DIRECTION_R:
                # El enemigo está a la derecha del jugador
                current_time = pygame.time.get_ticks()
                elapsed_time = current_time - self.last_attack_time
                if elapsed_time >= self.attack_cooldown:
                    # Realizar el ataque
                    self.last_attack_time = current_time
                    return True

            elif player.rect.x < self.rect.x and self.direction == DIRECTION_L:
                # El enemigo está a la izquierda del jugador
                current_time = pygame.time.get_ticks()
                elapsed_time = current_time - self.last_attack_time
                if elapsed_time >= self.attack_cooldown:
                    # Realizar el ataque
                    self.last_attack_time = current_time
                    return True

        return False

    def lanzar_disparo(self):
           
            if self.num_enemy == 2 or self.num_enemy == 4 or self.num_enemy == 5:
                
                objeto = Bullet(self.rect.centerx, self.rect.centery, self.direction, self, p_scale=0.3,type_bullet="enemy")
                
                if self.direction == DIRECTION_R:
                    objeto.velocidad_x = objeto.velocidad

                    
                elif self.direction == DIRECTION_L:
                    objeto.velocidad_x = -objeto.velocidad

                
                self.bullet.add(objeto)

    def atacar(self,player):
        if not player.pause:
            if self.puede_atacar(player):
                self.lanzar_disparo()
                self.last_attack_time = pygame.time.get_ticks()

    def check_collision(self,player):
        if self.num_enemy == 1 or self.num_enemy == 3:
            if player.is_dead == False:
                if self.rect.colliderect(player.rect):  # Colisión detectada
                    if self.direction == DIRECTION_R:
                        self.check_collition == True
                        self.move_x = 0
                        self.animation = self.attack_r
                        self.frame = 0
                        player.lives-=1
                        
                        
                        print(player.lives)
                    elif self.direction == DIRECTION_L:
                        self.check_collition == True
                        self.move_x = 0
                        self.animation = self.attack_l
                        self.frame = 0
                        player.lives-=1
                        

    def update(self,delta_ms,plataform_list,index,enemy_list,player):
        if not player.pause:
            self.do_movement(delta_ms,plataform_list)
            self.do_animation(delta_ms,index,enemy_list)
            self.check_collision(player)
            self.atacar(player)

    def draw(self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        

    def receive_shoot(self,enemy_list):
        self.lives -= 1

        
        print(self.lives)
        if self.lives <= 0:
            self.lives = 0
            self.death_animation()
            if self.num_enemy == 3:
                pygame.mixer.music.load("images/sonido/demonio.mp3")
                volumen = 100  # Establecer el volumen deseado (en este caso, la mitad del volumen máximo)
                pygame.mixer.music.set_volume(volumen)
                pygame.mixer.music.play()
            if self.num_enemy == 4:
                pygame.mixer.music.load("images/sonido/demon_dead.mp3")
                volumen = 100  # Establecer el volumen deseado (en este caso, la mitad del volumen máximo)
                pygame.mixer.music.set_volume(volumen)
                pygame.mixer.music.play()
            if self.num_enemy == 5:
                pygame.mixer.music.load("images/sonido/cuak.mp3")
                volumen = 0.4  # Establecer el volumen deseado (en este caso, la mitad del volumen máximo)
                pygame.mixer.music.set_volume(volumen)
                pygame.mixer.music.play()
            
            enemy_list.remove(self)

