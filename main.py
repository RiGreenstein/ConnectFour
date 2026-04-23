import pygame, sys
from element import *
from connectFour import *

pygame.init()

screen = pygame.display.set_mode((750, 447))
pygame.display.set_caption("Menu")
skill = 30
defensiveness = 30
aggressiveness = 30
outputDefensiveness = 1
outputAggressiveness = 1
depth = 1
settingsPage = 1


def getFont(size):
    return pygame.font.SysFont("calibri", size, bold=True)


def renderText(screen, color, text, xPos, yPos, size):
    label = getFont(size).render(text, 1, color)
    screen.blit(label, (xPos, yPos))


def Button2(screen, x, y, width, height, color, action=None):
    global skill, defensiveness, aggressiveness
    mousePos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(screen, color, (x, y, width, height))

    if x + width > mousePos[0] > x and y + height + 12 > mousePos[1] > y - 12:
        if click[0] == 1 and action != None:
            if action == "scroll1":
                skill = mousePos[0]
            elif action == "scroll2":
                defensiveness = mousePos[0]
            elif action == "scroll3":
                aggressiveness = mousePos[0]


def play():
    pygame.display.set_caption("Connect Four")
    startGame(depth, outputDefensiveness, outputAggressiveness)
    mainMenu()


def settings():
    pygame.display.set_caption("Settings")
    while True:
        global depth, outputDefensiveness, outputAggressiveness
        screen.fill("black")
        mousePos = pygame.mouse.get_pos()

        if settingsPage == 1:
            optionsText = getFont(75).render("AI Settings: ", True, "White")
            optionsRect = optionsText.get_rect(center=(350, 50))
            skillText = getFont(45).render("Skill: ", True, "White")
            skillRect = optionsText.get_rect(center=(300, 150))
            defensivnessText = getFont(45).render("Defensiveness: ", True, "White")
            defensivnessRect = optionsText.get_rect(center=(300, 300))
            aggressivenessText = getFont(45).render("Aggressiveness: ", True, "White")
            aggressivenessRect = optionsText.get_rect(center=(300, 450))
            screen.blit(optionsText, optionsRect)
            screen.blit(skillText, skillRect)
            screen.blit(defensivnessText, defensivnessRect)
            screen.blit(aggressivenessText, aggressivenessRect)
        elif settingsPage == 2:
            optionsText = getFont(75).render("Visual Settings: ", True, "White")
            optionsRect = optionsText.get_rect(center=(350, 50))
            skillText = getFont(45).render("Evaluation Bar", True, "White")
            skillRect = optionsText.get_rect(center=(200, 150))
            screen.blit(optionsText, optionsRect)

        optionsBack = Button(image=None, pos=(350, 630),
                             textInput="BACK", font=getFont(75), baseColor="White", hoveringColor="Green")

        if settingsPage == 1:
            # Skill
            Button2(screen, 30, 200, 400, 2, (255, 255, 255), action="scroll1")
            pygame.draw.rect(screen, (255, 255, 255), [skill, 200 - 12, 10, 24])
            depth = round((skill / 100 + 0.7), 0)
            renderText(screen, (255, 255, 255), str(depth), 470, 180, 45)

            # Defensiveness
            Button2(screen, 30, 350, 400, 2, (255, 255, 255), action="scroll2")
            pygame.draw.rect(screen, (255, 255, 255), [defensiveness, 350 - 12, 10, 24])
            outputDefensiveness = round((defensiveness / 100 + 0.7), 0)
            renderText(screen, (255, 255, 255), str(outputDefensiveness), 470, 330, 45)

            # Agressiveness
            Button2(screen, 30, 500, 400, 2, (255, 255, 255), action="scroll3")
            pygame.draw.rect(screen, (255, 255, 255), [aggressiveness, 500 - 12, 10, 24])
            outputAggressiveness = round((aggressiveness / 100 + 0.7), 0)
            renderText(screen, (255, 255, 255), str(outputAggressiveness), 470, 480, 45)
        elif settingsPage == 2:
            evalBarToggle = Button(image=pygame.image.load("menuRectangle.png"), pos=(400, 150), textInput="",
                                   font=getFont(75), baseColor="White", hoveringColor="Green")

            evalBarToggle.changeColor(mousePos)
            evalBarToggle.update(screen)

        optionsBack.changeColor(mousePos)
        optionsBack.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if optionsBack.checkForInput(mousePos):
                    mainMenu()

        pygame.display.update()


def mainMenu():
    global screen
    screen = pygame.display.set_mode((800, 700))

    while True:
        screen.fill("black")
        mousePos = pygame.mouse.get_pos()

        menuText1 = getFont(100).render("Connect Four", True, (255, 255, 255))
        menuRect1 = menuText1.get_rect(center=(350, 50))
        menuText2 = getFont(100).render("Main Menu", True, (255, 255, 255))
        menuRect2 = menuText2.get_rect(center=(375, 150))

        playButton = Button(image=pygame.image.load("menuRectangle.png"), pos=(350, 300),
                            textInput="Play", font=getFont(75), baseColor="White", hoveringColor="Green")
        settingsButton = Button(image=pygame.image.load("menuRectangle.png"), pos=(350, 450),
                                textInput="Settings", font=getFont(75), baseColor="White", hoveringColor="Green")
        quitButton = Button(image=pygame.image.load("menuRectangle.png"), pos=(350, 600),
                            textInput="Quit", font=getFont(75), baseColor="White", hoveringColor="Green")

        screen.blit(menuText1, menuRect1)
        screen.blit(menuText2, menuRect2)

        for button in [playButton, settingsButton, quitButton]:
            button.changeColor(mousePos)
            button.update(screen)

        eventList = pygame.event.get()

        for event in eventList:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(mousePos):
                    play()
                if settingsButton.checkForInput(mousePos):
                    settings()
                if quitButton.checkForInput(mousePos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


mainMenu()
