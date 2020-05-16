# Libraries

import pygame as pg
import sys
import time

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

# Defaults text

myfont = pg.font.SysFont('Comic Sans MS',12)

class Snake():


    def __init__(self):

        self.speed = 500
        self.posx = WIDTH//2 - rw//2
        self.posy = HEIGHT//2 - rh//2

        
        self.body = [pg.Rect((self.posx,self.posy),(rw,rh)), pg.Rect((self.posx,self.posy),(rw,rh)), pg.Rect((self.posx,self.posy),(rw,rh)), pg.Rect((self.posx,self.posy),(rw,rh)), pg.Rect((self.posx,self.posy),(rw,rh))]
        self.body_len = len(self.body)
        
        self.snake_state = "up"
        
        
        
        
        pass

    def Draw(self,screen,color):
        
        for i in range(len(self.body)):

            if i == 0:
                pg.draw.rect(screen,RED,self.body[i],0)
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
        
        
        
        for i in range(len(self.body)):

            if self.snake_state == "up":
                if self.body_len-i-1 > 0:
                    self.body[self.body_len-i-1].centerx = self.body[self.body_len-i-2].centerx
                    self.body[self.body_len-i-1].centery = self.body[self.body_len-i-2].centery
                else:
                    self.body[0].centery -= rh         
                
            elif self.snake_state == "down":
                if self.body_len-i-1 > 0:
                    self.body[self.body_len-i-1].centerx = self.body[self.body_len-i-2].centerx
                    self.body[self.body_len-i-1].centery = self.body[self.body_len-i-2].centery
                else:
                    self.body[0].centery += rh
   
            elif self.snake_state == "right":
                if self.body_len-i-1 > 0:
                    self.body[self.body_len-i-1].centerx = self.body[self.body_len-i-2].centerx
                    self.body[self.body_len-i-1].centery = self.body[self.body_len-i-2].centery
                else:
                    self.body[0].centerx += rh

            elif self.snake_state == "left":
                if self.body_len-i-1 > 0:
                    self.body[self.body_len-i-1].centerx = self.body[self.body_len-i-2].centerx
                    self.body[self.body_len-i-1].centery = self.body[self.body_len-i-2].centery
                else:
                    self.body[0].centerx -= rh
                
        
        self.Draw(screen,color)            
                 
        
        
            

    def Eating(self,apple):

        pass

    def Colide(self, array):

        pass
    


class Apple():

    def __init__(self):

        pass
    
    def Draw(self):

        pass
    
    pass


def Main():

      
    screen = pg.display.set_mode((HEIGHT,WIDTH))
    background = WHITE
    screen.fill(background)

    game_state = ("start","running","pause","gameover")
    current_game_state = "start"


    # INIT SCREEN TEXTS

    Init_Screen_Text = myfont.render(" PRESS SPACE TO PLAY ", False, BLACK)

    # GAME SCREEN TEXTS

    Game_Screen_Pause = myfont.render("PAUSE", False, RED)

    orochi = Snake()

    c = 0
    
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

            #Here goes any display logic to game start screen
            screen.fill(BLACK)

            
            #Here ends any display logic to game start screen

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
