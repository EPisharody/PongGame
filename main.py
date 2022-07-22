# Esha
# October 15 2018
# Pong Game. Extras: Start screen, final display screen, being able to pause during the game, difficulty changes as the game goes on (player presses a key to change the level), user can choose level at startup

#Import modules
import pygame
import sys
pygame.init()

#Screen dimensions
screenWidth = 800
screenHeight = 600
screenSize = (screenWidth,screenHeight)
screen = pygame.display.set_mode((screenSize),0)
pygame.display.set_caption("Pong Game")

#Colours
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
TURQUOISE = (93,243,213)
NAVYBLUE = (3, 41, 91)
GREENBLUE = (38, 168, 159)
DARKGREENBLUE = (48, 211, 200)
LIGHTERBLUE = (4,68,245)

#Variables for left paddle
rectWidth = 30
rectHeight = 100
x = screenWidth / screenWidth
y = screenHeight / 2
dx = 0
dy = 0

#Variables for right paddle
rectWidth2 = 30
rectHeight2 = 100
x2 = screenWidth - rectWidth2
y2 = screenHeight / 2
dx2 = 0
dy2 = 0

#Variables for the ball
ballX = screenWidth / 2
ballX = int(ballX)
ballY = screenHeight / 2
ballY = int (ballY)
ballDx = 1
ballDy = 1
radius = 20
colour = (56, 98, 247)

#Clock object - to slow down the speed
clock = pygame.time.Clock()
speed = 250

#Variables for score
player1Score = 0
player2Score = 0

p1WonRounds = 0
p2WonRounds = 0

#Start screen
startScreen = True
rules = False
while startScreen:

    for event in pygame.event.get():
        # Checks if any key is pressed and executes the code that goes with the key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                difficultyLevel = "Easy"
                startScreen = False
            if event.key == pygame.K_r:
                rules = True
            if event.key == pygame.K_e:
                difficultyLevel = "Easy"
                startScreen = False
            if event.key == pygame.K_m:
                difficultyLevel = "Medium"
                ballDx = 2
                ballDy = 2
                startScreen = False
            if event.key == pygame.K_h:
                difficultyLevel = "Hard"
                ballDx = 3
                ballDy = 3
                startScreen = False

    screen.fill(NAVYBLUE)

    # Title
    fontTitle = pygame.font.SysFont("broadway",55)
    textTitle = fontTitle.render("Welcome to Pong!",True,(48, 211, 200))
    textWidth = textTitle.get_width()
    textHeight = textTitle.get_height()

    screen.blit(textTitle,(screenWidth / 2 - textWidth / 2,screenHeight / 2 - textHeight / 2))

    fontTitle2 = pygame.font.SysFont("bookman old style",25)
    fontTitle3 = pygame.font.SysFont("bookman old style",16)
    textTitle2 = fontTitle2.render("Press 'g' to begin or press 'r' to see the rules and controls",True,(38, 168, 159))
    textTitle3 = fontTitle3.render("Or choose your starting level now! Press 'e' for easy, 'm' for medium and 'h' for hard",True,(38,168,159))

    textWidth3 = textTitle3.get_width()
    textHeight3 = textTitle3.get_width()
    textWidth2 = textTitle2.get_width()
    textHeight2 = textTitle2.get_height()

    screen.blit(textTitle2,(screenWidth / 2 - textWidth2 / 2,(screenHeight / 2 - textHeight2 / 2)+ 50))
    screen.blit(textTitle3,(screenWidth / 2 - textWidth3 / 2, (screenHeight / 2 - textHeight2 / 2)+ 80))
    pygame.display.update()
    
    # Rules page
    while rules == True:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    rules = False
                
        screen.fill(NAVYBLUE)
        rulesTitleFont = pygame.font.SysFont("broadway",75)
        rulesTitle = rulesTitleFont.render("Rules and Controls",True,(48, 211, 200))
        rulesTitleWidth = rulesTitle.get_width()
        rulesTitleHeight = rulesTitle.get_height()

        screen.blit(rulesTitle,(screenWidth / 2 - rulesTitleWidth / 2,screenHeight / 2 - rulesTitleHeight / 2))

        # Rules
        rulesTextFont = pygame.font.SysFont("bookman old style",20)
        rulesText = rulesTextFont.render("Player 1: Use the 'w' and 's' keys to move the left paddle up and down", True,(48,211,200))
        rulesText2 = rulesTextFont.render("Player 2: Use the up and down arrow keys to move the right paddle up and down", True,(48,211,200))
        rulesText3 = rulesTextFont.render("To pause, press 'p'", True,(48,211,200))
        rulesText4 = rulesTextFont.render("Any time the ball hits the a player's goal, the other player gets a point", True,(48,211,200))
        rulesText5 = rulesTextFont.render("The first player to 5 points in each level wins the level", True,(48,211,200))
        rulesText6 = rulesTextFont.render("The player that wins the most rounds, wins the game!", True,(48,211,200))
        rulesText7 = rulesTextFont.render("Press 'b' to go back",True,(48, 211, 200))

        # Getting the width and height of all the rules
        rulesTextWidth = rulesText.get_width()
        rulesTextHeight = rulesText.get_height()

        rulesTextWidth2 = rulesText2.get_width()
        rulesTextHeight2 = rulesText2.get_height()

        rulesTextWidth3 = rulesText3.get_width()
        rulesTextHeight3 = rulesText3.get_height()

        rulesTextWidth4 = rulesText4.get_width()
        rulesTextHeight4 = rulesText4.get_height()

        rulesTextWidth5 = rulesText5.get_width()
        rulesTextHeight5 = rulesText5.get_height()

        rulesTextWidth6 = rulesText6.get_width()
        rulesTextHeight6 = rulesText6.get_height()

        rulesTextWidth7 = rulesText7.get_width()
        rulesTextHeight7 = rulesText7.get_height()
        

        # Displaying all the rules to the screen
        screen.blit(rulesText,(screenWidth / 2 - rulesTextWidth / 2,(screenHeight / 2 - rulesTextHeight / 2)+50))

        screen.blit(rulesText2,(screenWidth / 2 - rulesTextWidth2 / 2,(screenHeight / 2 - rulesTextHeight2 / 2)+ 75))

        screen.blit(rulesText3,(screenWidth / 2 - rulesTextWidth3 / 2,(screenHeight / 2 - rulesTextHeight3 / 2)+100))

        screen.blit(rulesText4,(screenWidth / 2 - rulesTextWidth4 / 2,(screenHeight / 2 - rulesTextHeight4 / 2)+125))

        screen.blit(rulesText5,(screenWidth / 2 - rulesTextWidth5 / 2,(screenHeight / 2 - rulesTextHeight5 / 2)+150))

        screen.blit(rulesText6,(screenWidth / 2 - rulesTextWidth6 / 2,(screenHeight / 2 - rulesTextHeight6 / 2)+175))

        screen.blit(rulesText7,(screenWidth / 2 - rulesTextWidth7 / 2,(screenHeight / 2 - rulesTextHeight7 / 2)+250))

        
        # Updates the screen
        pygame.display.update()

# Main while loop for the game
pause = False
go = True
while go:
    for event in pygame.event.get():
        #Checks if any key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                go = False
            if event.key == pygame.K_s:
                dy = 2
            elif event.key == pygame.K_w:
                dy = -2
            if event.key == pygame.K_DOWN:
                dy2 = 2
            elif event.key == pygame.K_UP:
                dy2 = -2
            if event.key == pygame.K_p:
                pause = True
    
                
        #Checks if any key is not pressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                dy = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dy2 = 0


    #Text for difficulty level
    
    difficultyLevelFont = pygame.font.SysFont("broadway",75)
    difficultyLevelText = difficultyLevelFont.render(difficultyLevel, True,GREENBLUE)
    difficultyLevelWidth = difficultyLevelText.get_width()
    difficultyLevelHeight = difficultyLevelText.get_height()


    # Displaying the number of rounds won by each player
    p1WonRounds = str(p1WonRounds)
    p2WonRounds = str(p2WonRounds)

    overallScore = p1WonRounds + "   -   " + p2WonRounds
    overallScore = str (overallScore)

    overallScoreFont = pygame.font.SysFont("broadway",75)
    overallScoreText = overallScoreFont.render(overallScore, True,GREENBLUE)
    overallScoreWidth = overallScoreText.get_width()
    overallScoreHeight = overallScoreText.get_height()

    
    screen.fill(NAVYBLUE)
    
    #moving the left paddle
    x = x + dx
    y = y + dy

    #moving the right paddle
    x2 = x2 + dx2
    y2 = y2 + dy2


    # Checks for collision between the ball and paddles
    if (ballX + radius >= screenWidth - rectWidth2) and (ballY >= y2 + rectHeight2) and (ballY <= y2):
        ballDx = -ballDx
        
    # Moving the ball
    ballX = ballX + ballDx
    ballY = ballY + ballDy

    clock.tick(speed)

    # Resets ball to the center of the screen after it hits the right or left wall and adds to score of other player
    if (ballX >= screenWidth - radius):
        ballX = screenWidth / 2
        ballX = int(ballX)
        ballY = screenHeight / 2
        ballY = int(ballY)

        player1Score = int(player1Score)
        player1Score = player1Score + 1
        
    elif (ballX<=radius):
        ballX = screenWidth / 2
        ballX = int(ballX)
        ballY = screenHeight / 2
        ballY = int(ballY)

        player2Score = int(player2Score)
        player2Score = player2Score + 1

    # Checks if the ball has hit the top and bottom walls
    if (ballY>=screenHeight - radius):
        ballDy = -ballDy

    elif (ballY<=radius):
        ballDy = -ballDy

    #CHECK FOR LEFT PADDLE
    #checks for collision with the bottom wall
    if (y + rectHeight>=screenHeight):
        y = screenHeight - (rectHeight + 1)
       
    #checks for collision with the top wall
    elif (y<=0):
        y = 1

    #CHECK FOR RIGHT PADDLE
    #checks for collision with the bottom wall 
    if (y2 + rectHeight>=screenHeight):
        y2 = screenHeight - (rectHeight + 1)
        
    #checks for collision with the top wall 
    elif (y2<=0):
        y2 = 1

    #Checks if the ball collided with any of the paddles
    if (ballX + radius >= screenWidth - rectWidth2) and (ballY <= y2 + rectHeight2) and (ballY >= y2):
        ballDx = -ballDx

    if (ballX - radius <= 0 + rectWidth) and (ballY <= y + rectHeight) and (ballY >= y):
        ballDx = -ballDx

    #Changing the Score for player 1 and changing the level
    while player1Score == 5:
        ballDx = 0
        ballDy = 0

        # Runs a another while loop for displaying the final score when the game is over (FOR WHEN THE GAME IS OVER)
        while difficultyLevel == "Hard":
            continueToFinalScreenFont = pygame.font.SysFont("bookman old style",27)
            continueToFinalScreenText = continueToFinalScreenFont.render("Press 'c' to continue",True,GREENBLUE)
            continueToFinalScreenWidth = continueToFinalScreenText.get_width()
            continueToFinalScreenHeight = continueToFinalScreenText.get_height()

            screen.blit (continueToFinalScreenText, (screenWidth - continueToFinalScreenWidth,screenHeight - (p1TextHeight)))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    go = False
                    player1Score = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        p1WonRounds = int(p1WonRounds)
                        p1WonRounds = p1WonRounds + 1

                        screen.fill(NAVYBLUE)
                        p1WonRounds = int(p1WonRounds)
                        p2WonRounds = int(p2WonRounds)

                        # Depending on the number of rounds won, the winner will be displayed
                        if p1WonRounds > p2WonRounds:
                            overallScoreFont = pygame.font.SysFont("broadway",35)
                            overallScoreText = overallScoreFont.render("Player 1 Wins Overall! Congratulations!",True,GREENBLUE)
                            overallScoreWidth = overallScoreText.get_width()
                            overallScoreHeight = overallScoreText.get_height()

                            screen.blit(overallScoreText,(screenWidth / 2 - overallScoreWidth / 2, screenHeight / 8))
                            
                        if p1WonRounds < p2WonRounds:
                            overallScoreFont = pygame.font.SysFont("broadway",35)
                            overallScoreText = overallScoreFont.render("Player 2 Wins Overall! Congratulations!",True,GREENBLUE)
                            overallScoreWidth = overallScoreText.get_width()
                            overallScoreHeight = overallScoreText.get_height()

                            screen.blit(overallScoreText,(screenWidth / 2 - overallScoreWidth / 2, screenHeight / 8))
                            
                        if p1WonRounds == p2WonRounds:

                            overallScoreFont = pygame.font.SysFont("broadway",55)
                            overallScoreText = overallScoreFont.render("It's a tie overall! Good job!",True,GREENBLUE)
                            overallScoreWidth = overallScoreText.get_width()
                            overallScoreHeight = overallScoreText.get_height()

                            screen.blit(overallScoreText,(screenWidth / 2 - overallScoreWidth / 2, screenHeight / 8))


                        pygame.display.update()

                    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #Changing the level from "Easy" to "Medium"
                if event.key == pygame.K_m:
                    ballDx = 2
                    ballDy = 2

                    if difficultyLevel == "Easy":
                        difficultyLevel = "Medium"

                        # Adding to the number of rounds that are won
                        player1Score = 0
                        player2Score = 0
                        p1WonRounds = int(p1WonRounds)
                        p1WonRounds = p1WonRounds + 1
            
                #Changing the level from "Medium" to "Hard"
                if event.key == pygame.K_h:
                    ballDx = 3
                    ballDy = 3

                    if difficultyLevel == "Medium":
                        difficultyLevel = "Hard"

                        # Adding to the number of rounds that are won
                        player1Score = 0
                        player2Score = 0
                        p1WonRounds = int(p1WonRounds)
                        p1WonRounds = p1WonRounds + 1
                        
                if event.key == pygame.K_q:
                    player1Score == 0
                    go = False


        screen.fill(NAVYBLUE)

        # Between each level, this codes displays the winner of an individual round
        # Executes code if Player 1 won the "Easy" round
        changeDifficultyFont = pygame.font.SysFont("bookman old style",27)
        if difficultyLevel == "Easy":
            changeDifficultyText = changeDifficultyFont.render("Player 1 Wins! Press 'm' to move on to the next level",True,GREENBLUE)
            changeDifficultyWidth = changeDifficultyText.get_width()
            changeDifficultyHeight = changeDifficultyText.get_height()

            screen.blit (changeDifficultyText, (screenWidth / 2 - changeDifficultyWidth / 2, screenHeight / 2 - changeDifficultyHeight / 2))

        # Executes code if Player 1 won the "Medium" round
        if difficultyLevel == "Medium":
            changeDifficultyText = changeDifficultyFont.render("Player 1 Wins! Press 'h' to move on to the next level",True,GREENBLUE)
            changeDifficultyWidth = changeDifficultyText.get_width()
            changeDifficultyHeight = changeDifficultyText.get_height()

            screen.blit (changeDifficultyText, (screenWidth / 2 - changeDifficultyWidth / 2, screenHeight / 2 - changeDifficultyHeight / 2))
        

        pygame.display.update()

    #Changing the Score for player 2 and changing the level
    while player2Score == 5:
        ballDx = 0
        ballDy = 0
        
        # Runs a another while loop for displaying the final score when the game is over (FOR WHEN THE GAME IS OVER)
        while difficultyLevel == "Hard":
            continueToFinalScreenFont = pygame.font.SysFont("bookman old style",27)
            continueToFinalScreenText = continueToFinalScreenFont.render("Press 'c' to continue",True,GREENBLUE)
            continueToFinalScreenWidth = continueToFinalScreenText.get_width()
            continueToFinalScreenHeight = continueToFinalScreenText.get_height()

            screen.blit (continueToFinalScreenText, (screenWidth - continueToFinalScreenWidth,screenHeight - (p1TextHeight)))

            # pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    player2Score = 0
                    go = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        p1WonRounds = int(p1WonRounds)
                        p1WonRounds = p1WonRounds + 1
                        
                        p2WonRounds = int(p2WonRounds)

                        # Depending on the number of rounds won, the winner will be displayed
                        screen.fill(NAVYBLUE)
                        if p1WonRounds > p2WonRounds:
                            overallScoreFont = pygame.font.SysFont("broadway",35)
                            overallScoreText = overallScoreFont.render("Player 1 Wins Overall! Congratulations!",True,GREENBLUE)
                            overallScoreWidth = overallScoreText.get_width()
                            overallScoreHeight = overallScoreText.get_height()

                            screen.blit(overallScoreText,(screenWidth / 2 - overallScoreWidth / 2, screenHeight / 8))
                            
                        if p1WonRounds < p2WonRounds:
                            overallScoreFont = pygame.font.SysFont("broadway",35)
                            overallScoreText = overallScoreFont.render("Player 2 Wins Overall! Congratulations!",True,GREENBLUE)
                            overallScoreWidth = overallScoreText.get_width()
                            overallScoreHeight = overallScoreText.get_height()

                            screen.blit(overallScoreText,(screenWidth / 2 - overallScoreWidth / 2, screenHeight / 8))
                            
                        if p1WonRounds == p2WonRounds:

                            overallScoreFont = pygame.font.SysFont("broadway",55)
                            overallScoreText = overallScoreFont.render("It's a tie overall! Good job!",True,GREENBLUE)
                            overallScoreWidth = overallScoreText.get_width()
                            overallScoreHeight = overallScoreText.get_height()

                            screen.blit(overallScoreText,(screenWidth / 2 - overallScoreWidth / 2, screenHeight / 8))

                        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #Changing the level from "Easy" to "Medium"
                if event.key == pygame.K_m:
                    ballDx = 2
                    ballDy = 2

                     # Adding to the number of rounds that are won
                    if difficultyLevel == "Easy":
                        difficultyLevel = "Medium"
                        
                        player1Score = 0
                        player2Score = 0
                        p2WonRounds = int(p2WonRounds)
                        p2WonRounds = p2WonRounds + 1

                #Changing the level from "Medium" to "Hard"
                if event.key == pygame.K_h:
                    ballDx = 3
                    ballDy = 3

                     # Adding to the number of rounds that are won
                    if difficultyLevel == "Medium":
                        difficultyLevel = "Hard"
                        player1Score = 0
                        player2Score = 0
                        p2WonRounds = int(p2WonRounds)
                        p2WonRounds = p2WonRounds + 1
                
                if event.key == pygame.K_q:
                    go = False
                    player2Score = 0

        screen.fill(NAVYBLUE)

        # Between each level, this codes displays the winner of an individual round
        # Executes code if Player 2 won the "Easy" round
        changeDifficultyFont = pygame.font.SysFont("bookman old style",27)
        if difficultyLevel == "Easy":
            changeDifficultyText = changeDifficultyFont.render("Player 2 Wins! Press 'm' to move on to the next level",True,GREENBLUE)
            changeDifficultyWidth = changeDifficultyText.get_width()
            changeDifficultyHeight = changeDifficultyText.get_height()

            screen.blit (changeDifficultyText, (screenWidth / 2 - changeDifficultyWidth / 2, screenHeight / 2 - changeDifficultyHeight / 2))
            
        # Executes code if Player 2 won the "Medium" round
        if difficultyLevel == "Medium":
            changeDifficultyText = changeDifficultyFont.render("Player 2 Wins! Press 'h' to move on to the next level",True,GREENBLUE)
            changeDifficultyWidth = changeDifficultyText.get_width()
            changeDifficultyHeight = changeDifficultyText.get_height()

            screen.blit (changeDifficultyText, (screenWidth / 2 - changeDifficultyWidth / 2, screenHeight / 2 - changeDifficultyHeight / 2))
            

        pygame.display.update()

    # Pause Screen

    while pause == True:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # When 'r' is pressed, the game resumes
                if event.key == pygame.K_r:
                    pause = False
                # When 'q' is pressed the game exits
                if event.key == pygame.K_q:
                    go = False
                    pause = False

        # Displaying header and text
        screen.fill(NAVYBLUE)
        pauseFontTitle = pygame.font.SysFont("broadway",75)
        pauseTextTitle = pauseFontTitle.render("Game Paused",True,(48, 211, 200))
        pauseTextWidth = pauseTextTitle.get_width()
        pauseTextHeight = pauseTextTitle.get_height()

        screen.blit(pauseTextTitle,(screenWidth / 2 - pauseTextWidth / 2,screenHeight / 2 - pauseTextHeight / 2))

        pauseFont = pygame.font.SysFont("bookman old style",25)
        pauseText = pauseFont.render("Press 'r' to resume or 'q' to quit",True,(38, 168, 159))
        pauseWidth = pauseText.get_width()
        pauseHeight = pauseText.get_height()
        
        screen.blit(pauseText,(screenWidth / 2 - pauseWidth / 2,(screenHeight / 2 - pauseHeight / 2)+50))

        pygame.display.update()
            
    #Updating Score
    player1Score = str(player1Score)
    p1FontTitle = pygame.font.SysFont("forte",35)
    p1TextTitle = p1FontTitle.render("Player 1 Score: " + player1Score, True,GREENBLUE)
    p1TextWidth = p1TextTitle.get_width()
    p1TextHeight = p1TextTitle.get_height()

    player2Score = str(player2Score)
    p2FontTitle = pygame.font.SysFont("forte",35)
    p2TextTitle = p2FontTitle.render("Player 2 Score: " + player2Score, True,GREENBLUE)
    p2TextWidth = p2TextTitle.get_width()
    p2TextHeight = p2TextTitle.get_height()
    

    #Draw the rectangles and update the screen and display the updated score on screen
    screen.blit(difficultyLevelText,(screenWidth / 2 - difficultyLevelWidth / 2,0))
    screen.blit(overallScoreText, (screenWidth / 2 - overallScoreWidth / 2,difficultyLevelHeight))
    screen.blit(p1TextTitle,(0,screenHeight - p1TextHeight))
    screen.blit(p2TextTitle, (screenWidth - p2TextWidth,screenHeight - p2TextHeight))
    pygame.draw.circle (screen, DARKGREENBLUE, (ballX,ballY),radius,0)
    pygame.draw.rect(screen,LIGHTERBLUE,(x,y,rectWidth,rectHeight), 0)
    pygame.draw.rect(screen,LIGHTERBLUE, (x2,y2,rectWidth2,rectHeight2), 0)
    pygame.display.update()
    
pygame.quit()
sys.exit()
