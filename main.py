import pygame

# Initialization of the game
pygame.init()

# Title and icon
pygame.display.set_caption("Monkey Warfare")
icon = pygame.image.load("monkey.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("monkey-facing-right.png")
playerX = 300
playerY = 300
playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# The screen
screen = pygame.display.set_mode((1200, 600))

running = True


def MONKEMOVE():
    global playerX_change, playerY_change
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.5
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            playerY_change = -0.5
        if event.key == pygame.K_DOWN:
            playerY_change = 0.5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            playerY_change = 0


def BOUNDARIES():
    global playerX, playerY
    if playerX <= 0:
        playerX = 0
    if playerX >= 1168:
        playerX = 1168
    if playerY <= 0:
        playerY = 0
    if playerY >= 568:
        playerY = 568


def MOVEMENT():
    global playerX, playerY
    player(playerX, playerY)
    playerX += playerX_change
    playerY += playerY_change


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # monkey move
    MONKEMOVE()

    screen.fill((250, 250, 225))
    # Movement
    MOVEMENT()

    # boundaries
    BOUNDARIES()

    pygame.display.update()
