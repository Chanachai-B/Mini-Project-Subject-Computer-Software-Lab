import pygame
pygame.init()

SCREEN_SIZE = 600
CELL_SIZE = SCREEN_SIZE // 3
PICTURE_SIZE = CELL_SIZE *0.8
ROW = 3
COLUMN = 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
YELLOW1 = (204,204,0)
FPS = 60

x_img = pygame.image.load("X_modified.png")
o_img = pygame.image.load("o_modified.png")
icon = pygame.image.load("icon.png")

x_img = pygame.transform.scale(x_img, (PICTURE_SIZE, PICTURE_SIZE))
o_img = pygame.transform.scale(o_img, (PICTURE_SIZE, PICTURE_SIZE))

table = [[None]*3,[None]*3,[None]*3]
#print(table)
turn = 'X'
draw = None
winner = None

screen = pygame.display.set_mode((SCREEN_SIZE,SCREEN_SIZE))

pygame.display.set_caption("เกม X O")

pygame.display.set_icon(icon)

clock = pygame.time.Clock()

def draw_table(screen):
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (SCREEN_SIZE // 3, 0), (SCREEN_SIZE // 3, SCREEN_SIZE), 10)
    pygame.draw.line(screen, BLACK, ((SCREEN_SIZE / 3) * 2, 0), ((SCREEN_SIZE / 3) * 2, SCREEN_SIZE), 10)

    pygame.draw.line(screen, BLACK, (0, SCREEN_SIZE / 3), (SCREEN_SIZE, SCREEN_SIZE / 3), 10)
    pygame.draw.line(screen, BLACK, (0, (SCREEN_SIZE / 3) * 2), (SCREEN_SIZE, (SCREEN_SIZE / 3) * 2), 10)

def draw_object(x,y):
    global turn, table,winner
    if table[y][x] == None and winner == None:
        table[y][x] = turn
        #print(table)
        
        if turn == 'X':
            screen.blit(x_img, (x * CELL_SIZE + CELL_SIZE *0.1, y * CELL_SIZE + CELL_SIZE * 0.1))
            turn = 'O'
        else :
            screen.blit(o_img, (x * CELL_SIZE + CELL_SIZE *0.1, y * CELL_SIZE + CELL_SIZE * 0.1))
            turn = 'X'

def draw_result():
    global draw,winner
    if winner:
        message = winner + " won!"
    if draw:
        message = "Game Draw!"
    font = pygame.font.SysFont('arial', 70)
    text = font.render(message, True, YELLOW1)	
    text_rect = text.get_rect(center =(SCREEN_SIZE // 2, SCREEN_SIZE//2))
    screen.blit(text, text_rect)
    pygame.display.update()

def win_case():
    global table, winner , draw
    for row in range(0, 3):
        if((table[row][0] == table[row][1] == table[row][2]) and (table[row][0] != None)):
            print(table)
            winner = table[row][0]
            pygame.draw.line(screen, RED,(0, row * CELL_SIZE + CELL_SIZE / 2),(SCREEN_SIZE, row * CELL_SIZE + CELL_SIZE / 2), 10)
            draw_result()
            break
    
    for column in range(0, 3):
        if((table[0][column] == table[1][column] == table[2][column]) and (table[0][column] != None)):
            print(table)
            winner = table[0][column]
            pygame.draw.line (screen, RED, (column * CELL_SIZE + CELL_SIZE / 2, 0),(column * CELL_SIZE + CELL_SIZE / 2, SCREEN_SIZE), 10)
            draw_result()  
            break

    if (table[0][0] == table[1][1] == table[2][2]) and (table[0][0] != None):
        print(table)
        winner = table[0][0]
        pygame.draw.line (screen, RED, (0, 0),(SCREEN_SIZE, SCREEN_SIZE), 10)
        draw_result()

    if (table[0][2] == table[1][1] == table[2][0]) and (table[0][2] != None):
        print(table)
        winner = table[0][2]
        pygame.draw.line (screen, RED, (0, SCREEN_SIZE), (SCREEN_SIZE, 0), 10)
        draw_result()
    
    if table[0].count(None) == 0 and table[1].count(None) == 0 and table[2].count(None) == 0 and winner == None:
        print(table)
        draw = True
        draw_result()

def input_from_mouse():
    x,y = pygame.mouse.get_pos()
    x = x // CELL_SIZE
    y = y // CELL_SIZE
    draw_object(x,y)
    win_case()

draw_table(screen)

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            input_from_mouse()
    clock.tick(FPS)
    pygame.display.update()
pygame.quit()