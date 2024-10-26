import pygame
import sys
import numpy as np

pygame.init()

Width = 600
Height = 600
Line_width = 15
Board_rows = 3
Board_cols = 3
Square_size = Width // Board_cols
Circle_radius = Square_size // 3
Circle_width = 15
Cross_width = 25
Space = Square_size // 4

BG_color = (28, 170, 156)
Line_color = (23, 145, 200)
Circle_color = (239, 231, 200)
Cross_color = (66, 66, 66)
Button_color = (200, 0, 0)
Button_text_color = (255, 255, 255)

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_color)

board = np.zeros((Board_rows, Board_cols))

reset_button = pygame.Rect(Width - 100, Height - 50, 80, 40)
font = pygame.font.Font(None, 40)

def draw_lines():
    pygame.draw.line(screen, Line_color, (0, Square_size), (Width, Square_size), Line_width)
    pygame.draw.line(screen, Line_color, (0, 2*Square_size), (Width, 2*Square_size), Line_width)

    pygame.draw.line(screen, Line_color, (Square_size, 0), (Square_size, Height), Line_width)
    pygame.draw.line(screen, Line_color, (2*Square_size, 0), (2*Square_size, Height), Line_width)

def draw_figure():
    for row in range(Board_rows):
        for col in range(Board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen, Circle_color, (int(col * Square_size + Square_size//2), int(row * Square_size + Square_size//2)), Circle_radius, Circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, Cross_color, (col * Square_size + Space, row * Square_size + Square_size - Space), (col * Square_size + Square_size - Space, row * Square_size + Space), Cross_width)
                pygame.draw.line(screen, Cross_color, (col * Square_size + Space, row * Square_size + Space), (col * Square_size + Square_size - Space, row * Square_size + Square_size - Space), Cross_width)

def draw_reset_button():
    pygame.draw.rect(screen, Button_color, reset_button)
    text_surface = font.render('Reset', True, Button_text_color)
    screen.blit(text_surface, (Width - 95, Height - 45))

def check_win(player):
    for col in range( Board_cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    
    for row in range(Board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
        
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False

def draw_vertical_winning_line(col, player):
    posX = col * Square_size + Square_size//2
    if player == 1:
        color = Circle_color
        print("player 1 win")
    elif player == 2:
        color = Cross_color
        print("player 2 win")
    pygame.draw.line(screen, color, (posX, 15), (posX, Height - 15), Line_width-5)

def  draw_horizontal_winning_line(row, player):
    posY = row * Square_size + Square_size//2
    if player == 1:
        color = Circle_color
        print("player 1 win")
    elif player == 2:
        color = Cross_color
        print("player 2 win")
    pygame.draw.line(screen, color, (15, posY), (Width - 15, posY), Line_width)

def draw_asc_diagonal(player):
    if player == 1:
        color = Circle_color
        print("player 1 win")
    elif player == 2:
        color = Cross_color
        print("player 2 win")
    pygame.draw.line(screen, color, (15, Height -15), (Width -15, 15), Line_width)

def draw_desc_diagonal(player):
    if player == 1:
        color = Circle_color
        print("player 1 win")
    elif player == 2:
        color = Cross_color
        print("player 2 win")
    pygame.draw.line(screen, color, (15, 15), (Width - 15, Height - 15), Line_width)

def restart():
    screen.fill(BG_color)
    draw_lines()
    for row in range(Board_rows):
        for col in range( Board_cols):
            board[row][col] = 0

player = 1
game_over = False

draw_lines()
draw_reset_button()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // Square_size)
            clicked_col = int(mouseX // Square_size)

            if board[clicked_row][clicked_col] == 0:
                board[clicked_row][clicked_col] = player
                if check_win(player):
                    game_over = True
                player = 2 if player == 1 else 1

                draw_figure()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if reset_button.collidepoint(event.pos):
                restart()
                game_over = False

    pygame.display.update()