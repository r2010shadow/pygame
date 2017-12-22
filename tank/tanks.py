import pygame
import time
import random

pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
light_red = (255,0,0)
green = (0,155,0)
light_green = (0,255,0)
yellow = (200,200,0)
light_yellow = (250,250,0)


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tanks')


clock = pygame.time.Clock()

FPS = 15


tankWidth = 40
tankHeight = 20

turretWidth = 5
wheelWidth = 5

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


def tank(x,y):
    x = int(x)
    y = int(y)
    pygame.draw.circle(gameDisplay, black, (x,y), int(tankHeight/2))
    pygame.draw.rect(gameDisplay, black, (x-tankHeight , y, tankWidth, tankHeight))
    pygame.draw.line(gameDisplay, black, (x,y), (x-10,y-20), turretWidth)
 
    startX = -15
    for z in range(7):
        pygame.draw.circle(gameDisplay, black, (x-startX, y+20), wheelWidth-3)
        startX += 5

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height  > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "controls":
                game_controls()
            if action == "play":
                gameLoop()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))
    text_to_button(text, black, x,y,width, height)


def pause():
    paused = True
#    gameDisplay.fill(white)
    message_to_screen("Paused", black, -100, size = "large")
#    message_to_screen("Press C to continue or Q to quit", black, 25)
    pygame.display.update()
    clock.tick(5)

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        clock.tick(5)

def score(score):
    text = smallfont.render("Score: "  +  str(score), True, black)
    gameDisplay.blit(text, [0,0])

def game_controls():

    gcont = True

    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        message_to_screen("Controls", green, -100, "large")
        message_to_screen("Fire: Spacebar", black, -30)
        message_to_screen("Move Turret: use arrows", black, 10)
        message_to_screen("Pause: P", black, 90)

        button("play",  150, 500, 100, 50, green , light_green,action = "play")
        #button("controls", 350, 500, 100, 50, yellow, light_yellow, action = "controls")                
        button("quit", 550, 500, 100, 50, red, light_red, action = "quit")

        pygame.display.update()
        clock.tick(5)

def game_intro():
    intro = True
    while intro:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:                 
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
#        message_to_screen("welcome to Tanks", green, -100, "large")
        message_to_screen("The objective of the game is to shut and destroy",black, -30)
        message_to_screen(" ", black , 10)
        message_to_screen(" ", black, 50)
        message_to_screen("Press C to play or Q to quit.", black , 180)

        button("play",  150, 500, 100, 50, green , light_green,action = "play")
        button("controls", 350, 500, 100, 50, yellow, light_yellow, action = "controls")
        button("quit", 550, 500, 100, 50, red, light_red, action = "quit")
        pygame.display.update()
        clock.tick(5)

    ## make text display center
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
                textSurface = medfont.render(text, True, color)
    elif size == "large":
                textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth/2)), buttony + (buttonheight/2))
    gameDisplay.blit(textSurf, textRect)


    ## y_displace make  message two line wider
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace 
    gameDisplay.blit(textSurf, textRect)

def gameLoop():

    gameExit = False
    gameOver = False

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0

    while not gameExit:
        if gameOver == True:
            message_to_screen("Game over",red,size = "large")
            message_to_screen("press C to AG, Q to quit",black, 50,size = "medium")
            pygame.display.update()
    ## choose
        while gameOver == True:
#            gameDisplay.fill(white)

            for event in pygame.event.get():
    ## click windows exit 
                    if event.type == pygame.QUIT:
                        gameOver = False
                        gameExit = True
    ## choose key exit
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameExit = True
                            gameOver = False
                        if event.key == pygame.K_c:
                            gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5
                elif event.key == pygame.K_RIGHT:
                    tankMove = 5
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_p:
                    pause()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

        gameDisplay.fill(white)
        mainTankX += tankMove
        tank(mainTankX, mainTankY)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()
