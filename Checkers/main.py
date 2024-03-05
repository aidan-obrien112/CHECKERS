import pygame
from Checkers.constants import WIDTH, HEIGHT
from Checkers.board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers Game')

#Game Logic
def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    #Run loop until game is ended
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        #Draws the board and updates the display
        board.draw(WIN)
        pygame.display.update()


    pygame.quit()

#Runs the game
main()