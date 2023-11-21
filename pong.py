
import pygame
from pygame.locals import QUIT
import random
import time
from tkinter import *
from tkinter import ttk

# Put the pygame window inside of a function in order to initialize it later
def screen_init(mode):
    
    global screen
    pygame.init()
    
    # mode 1 is single player and mode 2 is two player
    if mode == 1:
        screen = pygame.display.set_mode((400,300))
    
    elif mode == 2:
        screen = pygame.display.set_mode((600,450))

# A pause window for when the window is out of focus
def paused(mode):
    
    # This for loop keeps pygame responding and allows for smooth window closing
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    # Make a blank screen
    screen.fill("black")
    
    # Make the font bigger
    font = pygame.font.Font("PixeloidSansBold-PKnYd.ttf", 35)
    
    # Define the shape of the text for the pause window
    pause = font.render("PAUSED",False,"white")
    pause2 = pause.get_rect()
    
    # Make the font smaller
    font = pygame.font.Font("PixeloidSansBold-PKnYd.ttf", 18)
    
    # Define the shape of the text for the pause window
    info = font.render("The window is out of focus.",False,"white")
    info2 = info.get_rect()
    
    # Make the font smaller
    font = pygame.font.Font("PixeloidSansBold-PKnYd.ttf", 15)
    
    # Define the shape of the text for the pause windows
    resume = font.render("Click on this window to resume play.",False,"white")
    resume2 = resume.get_rect()
    
    # Mode 1 is for the single player window, else is for mode 2 (two player)
    if mode == 1:
        pause2.center = (200, 75)
        info2.center = (200, 150)
        resume2.center = (200, 185)
    
    else:
        pause2.center = (300, 150)
        info2.center = (300, 225)
        resume2.center = (300, 260)
    
    # Render the text
    screen.blit(pause, pause2)
    screen.blit(info, info2)
    screen.blit(resume, resume2)
    
    # Display the text on the screen
    pygame.display.update()
   
# The winner/loser screen for the two player mode
def winner(score1,score2):
    
    # The dimensions and placement for the dummy paddles and ball
    pad_width = 10
    pad_height = 55
    center_x = screen.get_width()/2
    center_y = screen.get_height()/2
    pad1_x = 20
    pad1_y = center_y-(pad_height/2)
    pad2_x = 570
    pad2_y = center_y-(pad_height/2)
    ball_x = (center_x)-4
    ball_y = (center_y)-4
    pygame.display.set_caption("Pong")
    greater = ""

    # go is another way to stop the while loop
    go = True
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            
            # If Enter hit, set go to False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    go = False
                    break
        
        # If go set False by hitting Enter, stop the while loop
        if go == False:
            break
        
        # Draw the summy paddles and ball + the final scores
        screen.fill("black")
        font = pygame.font.Font("PixeloidSansBold-PKnYd.ttf", 75)
        ball = pygame.draw.rect(screen, "white", (ball_x, ball_y, 8, 8))
        paddle1 = pygame.draw.rect(screen, "white", (pad1_x, pad1_y, pad_width, pad_height))
        paddle2 = pygame.draw.rect(screen, "white", (pad2_x, pad2_y, pad_width, pad_height))
        scr1 = font.render(str(score1), True, "white")
        scr2 = font.render(str(score2), True, "white")
        textRect = scr1.get_rect()
        textRect.center = (150, 75)
        screen.blit(scr1, textRect)
        textRect = scr2.get_rect()
        textRect.center = (450, 75)
        screen.blit(scr2, textRect)
        better = font.render(greater,False,"white")
        textRect = better.get_rect()
        textRect.center = (300, 75)
        screen.blit(better, textRect)
        
        # Orientes the loser/winner text
        if score1 > score2:
            font = pygame.font.Font("PixeloidSansBold-PKnYd.ttf", 50)
            greater = ">"
            worl1 = font.render("Winner!",False,"white")
            worl2 = font.render("Loser",False,"white")
        
        elif score1 < score2:
            font = pygame.font.Font("PixeloidSansBold-PKnYd.ttf", 50)
            greater = "<"
            worl1 = font.render("Loser",False,"white")
            worl2 = font.render("Winner!",False,"white")
           
        else:
            font = pygame.font.Font("PixeloidSansBold-PKnYd.ttf", 50)
            greater = "="
            worl1 = font.render("Loser",False,"white")
            worl2 = font.render("Loser",False,"white")
            
       
        textRect = worl1.get_rect()
        textRect.center = (150, 325)
        screen.blit(worl1, textRect)
        textRect = worl2.get_rect()
        textRect.center = (450, 325)
        screen.blit(worl2, textRect)
    
        # More text
        font = pygame.font.Font("PixeloidSansBold-PKnYd.ttf", 30)
        hitenter = font.render("Hit Enter to continue...",False,"white")
        textRect = hitenter.get_rect()
        textRect.center = (300, 400)
        screen.blit(hitenter, textRect)
        
        # Display everything
        pygame.display.update()
    
# Get it? "fun" - because it's fun when you have friends
def fun():
    
    # Define dimensions and coordinates for all objects
    pygame.display.set_caption("Pong")
    pad_width = 10
    pad_height = 55
    center_x = screen.get_width()/2
    center_y = screen.get_height()/2
    pad1_x = 20
    pad1_y = center_y-(pad_height/2)
    pad2_x = 570
    pad2_y = center_y-(pad_height/2)
    ball_x = (center_x)-4
    ball_y = (center_y)-4
    rate_x = 2
    rate_y = 2
    game_speed = 1
    score1 = 0
    score2 = 0
    font = pygame.font.Font("PixeloidSansBold-PKnYd.ttf", 30)

    if random.randint(1,2) == 1:
        rate_x = -1*rate_x
        rate_y = -1*rate_y

    # Resets everything back to their original values and displays the winner/loser screen
    def reset(score1,score2,pad1_y,pad2_y):
        
        if score1 == 11 or score2 == 11:
            winner(score1,score2)
            score1 = 0
            score2 = 0
            pad1_y = center_y-(pad_height/2)
            pad2_y = pad1_y
            
        ball_x = (center_x)-4
        ball_y = (center_y)-4
        game_speed = 1
        return ball_x,ball_y,game_speed,score1,score2,pad1_y,pad2_y

    # Returns the value of the variable true if the ball is touching the given paddle or not
    def is_touching(ball_x,ball_y,paddle):
        true = False
        for i in range(8):
            if paddle.collidepoint(ball_x,(ball_y+i)) == True:
                true = True
                break

        return true

    # This function makes the entire game work
    def move_ball(game_speed,rate_x,rate_y,ball_x,ball_y,paddle1,paddle2,ball,score1,score2,pad1_y,pad2_y):
        
        def reset_sequence(game_speed,rate_x,rate_y,ball_x,ball_y,paddle1,paddle2,ball,score1,score2,pad1_y,pad2_y):
            ball_x,ball_y,game_speed,score1,score2,pad1_y,pad2_y = reset(score1,score2,pad1_y,pad2_y)
            
            # Choose the direction for the ball to go after everything has been reset
            if random.randint(1,2) == 1:
                rate_x = -2
                rate_y = -2

            else:
                rate_x = 2
                rate_y = 2
             
            return game_speed,rate_x,rate_y,ball_x,ball_y,paddle1,paddle2,ball,score1,score2,pad1_y,pad2_y
        
        # If the ball hits the left or right walls
        if ball_x <= 1:
            score2 += 1
            game_speed,rate_x,rate_y,ball_x,ball_y,paddle1,paddle2,ball,score1,score2,pad1_y,pad2_y = reset_sequence(game_speed,rate_x,rate_y,ball_x,ball_y,paddle1,paddle2,ball,score1,score2,pad1_y,pad2_y)
            move_ball(game_speed,rate_x,rate_y,ball_x,ball_y,paddle1,paddle2,ball,score1,score2,pad1_y,pad2_y)
         
        elif (ball_x+8) >= 599:
            score1 += 1
            game_speed,rate_x,rate_y,ball_x,ball_y,paddle1,paddle2,ball,score1,score2,pad1_y,pad2_y = reset_sequence(game_speed,rate_x,rate_y,ball_x,ball_y,paddle1,paddle2,ball,score1,score2,pad1_y,pad2_y)
            move_ball(game_speed,rate_x,rate_y,ball_x,ball_y,paddle1,paddle2,ball,score1,score2,pad1_y,pad2_y)
            
        # If the ball hits walls or the paddles, change movement accordingly
        else:
            if (ball_y) <= 1:
                rate_y = -1*rate_y
    
            elif (ball_y+8) >= 449:
                rate_y = -1*rate_y
    
            if is_touching(ball_x,ball_y,paddle1) == True:
                rate_x = -1*rate_x
        
            elif is_touching((ball_x+8),ball_y,paddle2) == True:
                rate_x = -1*rate_x
        
            ball_x += (game_speed*rate_x)
            ball_y += (game_speed*rate_y)
    
        # Return everything that was changed
        return rate_x,rate_y,ball_x,ball_y,game_speed,score1,score2,pad1_y,pad2_y
            
    # count is for game speed; as count increases, so do the game speed
    count = 0
    while True:
        
        # If the window isn't focused, run the paused function - In a while loop so that it keeps checking
        if pygame.key.get_focused() == False:
            while pygame.key.get_focused() == False:
                paused(2)
            
        count += 1
        
        # Keypress detection
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if pad2_y > 0:
                        pad2_y -= 25

                if event.key == pygame.K_DOWN:
                    if pad2_y < (screen.get_height()-pad_height):
                        pad2_y += 25
             
                if event.key == pygame.K_w:
                    if pad1_y > 0:
                        pad1_y -= 25

                if event.key == pygame.K_s:
                    if pad1_y < (screen.get_height()-pad_height):
                        pad1_y += 25
            

        
        screen.fill("black")

        # Increases game_speed with count
        if count == 25:
            count = 0
            game_speed += .01
        
        # Draw the Pong board, paddles, ball, and score
        top_wall = pygame.draw.rect(screen, "white", (0, 0, 600, 1))
        right_wall = pygame.draw.rect(screen, "white", (599, 0, 1, 450))
        bottom_wall = pygame.draw.rect(screen, "white", (0, 449, 600, 1))
        left_wall = pygame.draw.rect(screen, "white", (0, 0, 1, 450))
        paddle1 = pygame.draw.rect(screen, "white", (pad1_x, pad1_y, pad_width, pad_height))
        paddle2 = pygame.draw.rect(screen, "white", (pad2_x, pad2_y, pad_width, pad_height))
        ball = pygame.draw.rect(screen, "white", (ball_x, ball_y, 8, 8))
        rate_x,rate_y,ball_x,ball_y,game_speed,score1,score2,pad1_y,pad2_y=move_ball(game_speed,rate_x,rate_y,ball_x,ball_y,paddle1,paddle2,ball,score1,score2,pad1_y,pad2_y)
        scr1 = font.render(str(score1), True, "white")
        scr2 = font.render(str(score2), True, "white")
        textRect = scr1.get_rect()
        textRect.center = (150, 30)
        screen.blit(scr1, textRect)
        textRect = scr2.get_rect()
        textRect.center = (450, 30)
        screen.blit(scr2, textRect)
    
        time.sleep(.02)
    

        # Display everything
        pygame.display.update()

# This is the single player version of everything from above (meaning it's simpler). If you have a question about this one, just find the bit of code from above closest to it and read the comments for that code (I'm not writing comments twice).
def lonely():
    pygame.display.set_caption('1 Player Pong')
    pad_width = 10
    pad_height = 55
    center_x = screen.get_width()/2
    center_y = screen.get_height()/2
    pad_x = 20
    pad_y = center_y-(pad_height/2)
    ball_x = (center_x)-4
    ball_y = (center_y)-4
    rate_x = 2
    rate_y = 2
    game_speed = 1
    score = 0
    font = pygame.font.Font('PixeloidSansBold-PKnYd.ttf', 20)

    if random.randint(1,2) == 1:
        rate_x = -1*rate_x
        rate_y = -1*rate_y

    def reset():
        ball_x = (center_x)-4
        ball_y = (center_y)-4
        game_speed = 1
        score = 0
        return ball_x,ball_y,game_speed,score

    def is_touching(ball_x,ball_y,paddle1):
        true = False
        for i in range(8):
            if paddle1.collidepoint(ball_x,(ball_y+i)) == True:
                true = True
                break

        return true

    def move_ball(game_speed,rate_x,rate_y,ball_x,ball_y,paddle1,ball,score):
        if (ball_x) <= 1:
            ball_x,ball_y,game_speed,score = reset()
            move_ball(game_speed,rate_x,rate_y,ball_x,ball_y,paddle1,ball,score)
            if random.randint(1,2) == 1:
                rate_x = -2
                rate_y = -2

            else:
                rate_x = 2
                rate_y = 2

        else:
            if (ball_y) <= 1:
                rate_y = -1*rate_y
    
            elif (ball_y+8) >= 299:
                rate_y = -1*rate_y
    
            if (ball_x+8) >= 399:
                rate_x = -1*rate_x
    
            if is_touching(ball_x,ball_y,paddle1) == True:
                rate_x = -1*rate_x
                score += 1
        
            ball_x += (game_speed*rate_x)
            ball_y += (game_speed*rate_y)
    
        return rate_x,rate_y,ball_x,ball_y,game_speed,score
            

    count = 0
    while True:
        if pygame.key.get_focused() == False:
            while pygame.key.get_focused() == False:
                paused(1)
            
        count += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if pad_y > 0:
                        pad_y -= 25

                if event.key == pygame.K_DOWN:
                    if pad_y < (screen.get_height()-pad_height):
                        pad_y += 25
            


        screen.fill("black")

        if count == 25:
            count = 0
            game_speed += .01
        
        top_wall = pygame.draw.rect(screen, "white", (0, 0, 400, 1))
        right_wall = pygame.draw.rect(screen, "white", (399, 0, 1, 300))
        bottom_wall = pygame.draw.rect(screen, "white", (0, 299, 400, 1))
        left_wall = pygame.draw.rect(screen, "white", (0, 0, 1, 300))
        paddle1 = pygame.draw.rect(screen, "white", (pad_x, pad_y, pad_width, pad_height))
        ball = pygame.draw.rect(screen, "white", (ball_x, ball_y, 8, 8))
        rate_x,rate_y,ball_x,ball_y,game_speed,score=move_ball(game_speed,rate_x,rate_y,ball_x,ball_y,paddle1,ball,score)
        text = font.render(str(score), True, "white")
        textRect = text.get_rect()
        textRect.center = (400 // 2, 20)
        screen.blit(text, textRect)
    
        time.sleep(.02)
    

    
        pygame.display.update()
        

display_window = True

# Putting the Tkinter window in a while loop allows the mode-selection window to popup again if pong is closed.
while display_window == True:
    root = Tk()
    root.title("Pong Selection")

    # The one_player(), two_players(), and stop_all() functions are so multiple commands can be run by one button-press.
    def one_player():
        global root
        root.destroy()
        screen_init(1)
        lonely()
    
    def two_players():
        global root
        root.destroy()
        screen_init(2)
        fun()
    
    def stop_all():
        global root,display_window
        root.destroy()
        display_window = False
    
    # Defining the window's geometry and placement
    root.geometry(f"300x200+{int((root.winfo_screenwidth()/2)-150)}+{int((root.winfo_screenheight()/2)-125)}")
    
    # The text and buttons in the Tkinter windows
    ttk.Label(root, text="Which mode of Pong would you like to play?").place(x=30,y=35)
    ttk.Button(root, text="1 Player", command=one_player).place(x=75,y=90)
    ttk.Button(root, text="2 Players", command=two_players).place(x=155,y=90)
    ttk.Button(root, text="Quit", command=stop_all).place(x=115,y=140)
    ttk.Label(root, text="Zakkai Thomas | 2023").place(x=2,y=180)
    root.mainloop()
    

# This took way longer to make than I care to admit.
#
# I hope that you learned something cool from my code.
#
# Thanks for being cool,
#
# - Zakkai Thomas
