import pygame
from Checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from Checkers.board import Board
from Checkers.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers Game')

#Game Logic
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    if game.winner() != None:
        print(game.winner())


    #Run loop until game is ended
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        #Draws the board and updates the display
        game.update()



    pygame.quit()

#Runs the game
main()