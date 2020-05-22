# Libraries

import pygame as pg
import sys
import time
import random

# Inits

pg.font.init()

# Global Variables

# ----- Window properties

WIDTH = 500
HEIGHT = 500
rw = 10
rh = 10

WHITE = (255,255,255)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (200,200,255)
BLACK = (0,0,0)

REC_WIDTH = 450
REC_HEIGHT = 450

# Defaults text

myfont = pg.font.SysFont('Comic Sans MS',12)

class Snake():


    def __init__(self):

        self.speed = 100
        self.posx = WIDTH//2 - rw//2
        self.posy = HEIGHT//2 - rh//2

        
        self.body = [pg.Rect((self.posx,self.posy),(rw,rh)), pg.Rect((self.posx,self.posy),(rw,rh))]
        self.body_len = len(self.body)
        
        self.snake_state = "up"
        
        
        
        
        pass

    def Draw(self,screen,color):
        
        for i in range(len(self.body)):

            if i == 0:
                pg.draw.rect(screen,BLUE,self.body[i],0)
            else:
                pg.draw.rect(screen,color,self.body[i],0)
            #print("Posiciong y ", self.body[i].centery, " Cuerpo ",  i)
            #print(i)    
        pass
    
    def SetState(self,key):
        

        if key == pg.K_UP and self.snake_state != "down":

            self.snake_state = "up"
            #print("Up pressed")
            return self.snake_state
        
        elif key == pg.K_DOWN and self.snake_state != "up":
            
            self.snake_state = "down"
            #print("Down pressed")
            return self.snake_state
        
        elif key == pg.K_LEFT and self.snake_state != "right":

            self.snake_state = "left"
            #print("Left pressed")
            return self.snake_state
        
        elif key == pg.K_RIGHT and self.snake_state != "left":
            
            self.snake_state = "right"
            #print("Right pressed")
            return self.snake_state
        
        else:
            #print("Else setstate")
            return self.snake_state
        
        pass


        
    
    def Move(self,screen,color):
        
        #print(current_move_state)
        #time.sleep(1/2)
        
        
        
        for i in range(len(self.body)-1,0,-1):


            if self.snake_state == "up":

                if i == len(self.body)-1:
                    self.body[0].centery -= rh
                    self.body[i].centerx = self.body[i-1].centerx
                    self.body[i].centery = self.body[i-1].centery         
                
                else:
                    
                    self.body[i].centerx = self.body[i-1].centerx
                    self.body[i].centery = self.body[i-1].centery
                            
                
            elif self.snake_state == "down":
                
                if i == len(self.body)-1:
                    self.body[0].centery += rh
                    self.body[i].centerx = self.body[i-1].centerx
                    self.body[i].centery = self.body[i-1].centery         
                
                else:
                    
                    self.body[i].centerx = self.body[i-1].centerx
                    self.body[i].centery = self.body[i-1].centery
   
            elif self.snake_state == "right":
                
                if i == len(self.body)-1:
                    self.body[0].centerx += rh
                    self.body[i].centerx = self.body[i-1].centerx
                    self.body[i].centery = self.body[i-1].centery         
                
                else:
                    
                    self.body[i].centerx = self.body[i-1].centerx
                    self.body[i].centery = self.body[i-1].centery

            elif self.snake_state == "left":
                
                if i == len(self.body)-1:
                    self.body[0].centerx -= rh
                    self.body[i].centerx = self.body[i-1].centerx
                    self.body[i].centery = self.body[i-1].centery         
                
                else:
                    
                    self.body[i].centerx = self.body[i-1].centerx
                    self.body[i].centery = self.body[i-1].centery
                
        
        self.Draw(screen,color)            

                 
    def Eating(self,apple):
        
        print(self.body)
        
        if apple.colliderect(self.body[0]) == True:
            
            self.body.append(pg.Rect((self.body[-1].left,self.body[-1].top),(rw,rh)))

            
        pass

    

    def Colide(self,mapa):
                 
        if self.body[0].right >= mapa.right or self.body[0].left <= mapa.left or self.body[0].bottom >= mapa.bottom or self.body[0].top <= mapa.top or self.body[0].collidelist(self.body[2:]) != -1:

            self.body[0].center = (WIDTH//2,HEIGHT//2)

            self.body = [pg.Rect((self.posx,self.posy),(rw,rh)), pg.Rect((self.posx,self.posy),(rw,rh))]
            
            return "gameover"
        
        else:
            
            return "running"



class Apple():

    def __init__(self):

        self.apx = rh*20-rh//2
        self.apy = rh*20-rh//2
        self.apw = rh
        self.aph = rh
        self.ap = pg.Rect((self.apx,self.apy),(self.apw,self.aph))

    def Draw_Apple(self,screen):

        pg.draw.rect(screen,RED,self.ap,0)

    def Collide(self,head,map):

        if head.colliderect(self.ap) != False:

            self.ap.right = random.randrange(map.left+20,map.right-20,rh)
            self.ap.top = random.randrange(map.top+20,map.bottom-20,rh)
            
            


class Map():

    def __init__(self):

        self.mx = rh
        self.my = rh
        self.mw = REC_WIDTH
        self.mh = REC_HEIGHT
        self.map = pg.Rect((self.mx,self.my),(self.mw,self.mh))
        self.map.centerx = WIDTH//2
        self.map.centery = HEIGHT//2
        
    def Draw_Map(self,screen):

        pg.draw.rect(screen,BLACK,self.map,4)


def Main():

      
    screen = pg.display.set_mode((HEIGHT,WIDTH))
    background = WHITE
    screen.fill(background)

    game_state = ("start","running","pause","gameover")
    current_game_state = "start"


    # INIT SCREEN TEXTS

    Init_Screen_Text = myfont.render(" PRESS SPACE TO PLAY ", False, BLACK)
    GO_Screen_Text = myfont.render(" PERDISTE MARICON ", False, RED)

    # GAME SCREEN TEXTS

    Game_Screen_Pause = myfont.render("PAUSE", False, RED)

    orochi = Snake()
    mapita = Map()
    mansana = Apple()
    
    while True:

        pressed = pg.key.get_pressed()
        

        # FIRST SCREEN TO START THE GAME

        if current_game_state == "start":

            #Here goes any display logic to game start screen
            
            #print("start state")
            screen.fill(BLUE)
            screen.blit(Init_Screen_Text,(WIDTH//3,HEIGHT//2))
            
            #Here ends any display logic to game start screen

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        current_game_state = "running"
                        print("Game state changed to RUNNING")
                if event.type == pg.QUIT:
                    print("QUIT")
                    pg.quit()
                    sys.exit()
               
            pass


        # MAIN GAME SCREEN
        elif current_game_state == "running":


            
            #Here goes any display logic to game start screen
            screen.fill(WHITE)
            pg.time.delay(orochi.speed)
            mapita.Draw_Map(screen)
            mansana.Draw_Apple(screen)
            current_game_state = orochi.Colide(mapita.map)
            orochi.Eating(mansana.ap)
            mansana.Collide(orochi.body[0],mapita.map)       
            
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:                                        
                    orochi.SetState(event.key)

                    if event.key == pg.K_SPACE:
                        current_game_state = "pause"
                        print("Game state changed to PAUSE")
                    
                if event.type == pg.QUIT:
                    print("QUIT")
                    pg.quit()
                    sys.exit()
                    
            orochi.Move(screen,GREEN)
           
            
            #Here ends any display logic to game start screen

            pass

        # PAUSE SCREEN
        elif current_game_state == "pause":

            #Here goes any display logic to game start screen
            screen.fill((200,200,200))
            screen.blit(Game_Screen_Pause,(10,10))
            
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        current_game_state = "running"
                        print("Game state changed to RUNNING")
                if event.type == pg.QUIT:
                    print("QUIT")
                    pg.quit()
                    sys.exit()

            
            #Here ends any display logic to game start screen

            

        # GAMEOVER SCREEN
        elif current_game_state == "gameover":

            
            screen.fill(BLACK)
            screen.blit(GO_Screen_Text,(WIDTH//3,HEIGHT//2))
            
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        current_game_state = "running"
                        print("Game state changed to RUNNING")
                if event.type == pg.QUIT:
                    print("QUIT")
                    pg.quit()
                    sys.exit()
            
            

            pass

        # IN CASE OF ERROR
        else:
            print("An error ocured, no game state existing")

        
        # GET QUIT EVENT
        for event in pg.event.get():
            if event.type == pg.QUIT:
                print("quit pressed")
                pg.quit()
                sys.exit()
              

        pg.display.update()
        #print("flipped")
          
          
          
        




if __name__=="__main__":

    Main()
    
    pass
