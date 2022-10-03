import pygame
import os
pygame.font.init()

WIDTH, HEIGHT = 1000, 700
FPS = 60
VEL = 5

POINTS_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 50)

PACMAN_SIZE = 50

EAT = pygame.USEREVENT + 1
HIT = pygame.USEREVENT + 2

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PacMan')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

PACMAN_IMAGE = pygame.image.load(os.path.join('Assets', 'pacman.png'))
PACMAN_RIGHT = pygame.transform.scale(PACMAN_IMAGE, (PACMAN_SIZE, PACMAN_SIZE))
PACMAN_LEFT = pygame.transform.rotate(PACMAN_RIGHT, 180)
PACMAN_UP = pygame.transform.rotate(PACMAN_RIGHT, 90)
PACMAN_DOWN = pygame.transform.rotate(PACMAN_RIGHT, 270)

#FOOD = [pygame.Rect(x, 100, 10, 10) for x in range(100, 900, 50)]

def draw_window(pacman, direction, points, borders, food):
    WIN.fill(BLACK)
    points_text = POINTS_FONT.render(
        'Points: ' + str(points), 1, WHITE)
    for b in borders:
        pygame.draw.rect(WIN, BLUE, b)
    for f in food:
        pygame.draw.rect(WIN, WHITE, f)
    WIN.blit(points_text, (10, 10))
    WIN.blit(direction, (pacman.x, pacman.y))

    pygame.display.update()

def create_map():
    #This method will create the rectangles needed for the game
    top_left_border = pygame.Rect(0, 80, 450, 30)
    top_right_border = pygame.Rect(550, 80, 450, 30)
    top_1 = pygame.Rect(420, 0, 30, 80)
    top_2 = pygame.Rect(550, 0, 30, 80)
    r1 = pygame.Rect(0, 100, 100, 100),
    r2 = pygame.Rect(900, 100, 100, 100)
    r3 = pygame.Rect(200, 200, 100, 100)
    r4 = pygame.Rect(400, 200, 50, 200)
    r5 = pygame.Rect(550, 200, 50, 200)
    r6 = pygame.Rect(700, 200, 100, 100)
    r7 = pygame.Rect(0, 300, 100, 200)
    r8 = pygame.Rect(200, 400, 250, 100)
    r9 = pygame.Rect(550, 400, 250, 100)
    r10 = pygame.Rect(900, 300, 100, 200)
    r11 = pygame.Rect(0, 600, 450, 100)
    r12 = pygame.Rect(550, 600, 450, 100)

    return [top_1, top_2, top_left_border, top_right_border, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12]

def create_food():
    #FOOD = [pygame.Rect(x, 100, 10, 10) for x in range(100, 900, 50)]
    food = ([pygame.Rect(x, 150, 10, 10) for x in range(150, 900, 50)]
            + [pygame.Rect(150, y, 10, 10) for y in range(200, 600, 50)]
            + [pygame.Rect(x, 550, 10, 10) for x in range(50, 1000, 50)]
            + [pygame.Rect(850, y, 10, 10) for y in range(200, 550, 50)]
            + [pygame.Rect(650, y ,10, 10) for y in range(200, 400, 50)]
            + [pygame.Rect(350, y, 10, 10) for y in range(200, 400, 50)]
            + [pygame.Rect(500, y, 10, 10) for y in range(200, 550, 50)]
            + [pygame.Rect(x, 350, 10, 10) for x in range(200, 350, 50)]
            + [pygame.Rect(x, 350, 10, 10) for x in range(700, 850, 50)]
            + [pygame.Rect(x, 250, 10, 10) for x in range(50, 150, 50)]
            + [pygame.Rect(x, 250, 10, 10) for x in range(900, 1000, 50)]
            + [pygame.Rect(500, y, 10, 10) for y in range(600, 700, 50)]
            )

    return food



def handle_movement(keys_pressed, pacman, direction, borders):
    if keys_pressed[pygame.K_LEFT] and not pacman.move(-VEL, 0).collidelistall(borders):  # LEFT
        if pacman.x + PACMAN_SIZE - VEL == 0:
            pacman.x = WIDTH - PACMAN_SIZE
        else:
            pacman.x -= VEL
        return PACMAN_LEFT
    if keys_pressed[pygame.K_RIGHT] and not pacman.move(+VEL, 0).collidelistall(borders):  # RIGHT
        if pacman.x  + VEL == WIDTH:
            pacman.x = 0
        else:
            pacman.x += VEL
        return  PACMAN_RIGHT
    if keys_pressed[pygame.K_UP] and not pacman.move(0, -VEL).collidelistall(borders):  # UP
        if pacman.y + PACMAN_SIZE - VEL == 0:
            pacman.y = HEIGHT
        else:
            pacman.y -= VEL
        return  PACMAN_UP
    if keys_pressed[pygame.K_DOWN] and not pacman.move(0, +VEL).collidelistall(borders):  # DOWN
        if pacman.y + VEL == HEIGHT:
            pacman.y = 0
        else:
            pacman.y += VEL
        return  PACMAN_DOWN
    else:
        return direction

def handle_points(pacman, food):
    for f in food:
        if pacman.colliderect(f):
            pygame.event.post(pygame.event.Event(EAT))
            food.remove(f)

def handle_end(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (0, 400))
    #pygame.display.update()
    #pygame.time.delay(5000)
    #restart = []
    restart_text = WINNER_FONT.render('Would you like to play again Y/N', 1, WHITE)
    WIN.blit(restart_text, (100 ,100))
    pygame.display.update()
    #pygame.time.delay(5000)
    restart = pygame.key.get_pressed()
    pygame.time.delay(5000)
    if restart[pygame.K_y]:
        print('YES')
    else:
        print('No')

def main():
    winner_font = POINTS_FONT.render(
        'Congratulations You Have Won! ', 1, WHITE)

    pacman = pygame.Rect(500 - PACMAN_SIZE// 2, 550 - PACMAN_SIZE // 2, PACMAN_SIZE, PACMAN_SIZE)
    borders = create_map()
    food = create_food()
    food_len = len(food)
    direction = PACMAN_RIGHT
    points = 0

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == EAT:
                points += 1

       ##    winner = True
         #   break

        winner_text = ''
        if points == 5:
            winner_text = 'Congratulations you Have Won! '

        if winner_text != '':
            handle_end(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()

        direction = handle_movement(keys_pressed, pacman, direction, borders)
        handle_points(pacman, food)
        draw_window(pacman, direction, points, borders, food)


if __name__ == '__main__':
    main()