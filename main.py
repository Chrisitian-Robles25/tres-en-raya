import pygame
from utils.game_logic import check_winner

pygame.init()
pygame.mixer.init()
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tres en Raya - Neon Edition")

# Colores
BLACK = (0, 0, 0)
NEON_BLUE = (0, 255, 255)
NEON_PINK = (255, 0, 255)
WHITE = (255, 255, 255)
FONT = pygame.font.SysFont("Arial", 32)
BIG_FONT = pygame.font.SysFont("Arial", 48)

# Tablero
board = [""] * 9
turn = "X"
winner = None

# Sonidos
click_sound = None
win_sound = None
draw_sound = None

def draw_board():
    screen.fill(BLACK)
    # Panel superior
    pygame.draw.rect(screen, NEON_BLUE, (0, 0, WIDTH, 100), 2)
    text = f"Turno de: Jugador {'1 (X)' if turn == 'X' else '2 (O)'}"
    screen.blit(FONT.render(text, True, WHITE), (20, 30))

    # Tablero
    for i in range(3):
        for j in range(3):
            rect = pygame.Rect(j * 200, 100 + i * 200, 200, 200)
            pygame.draw.rect(screen, NEON_PINK, rect, 3)
            if board[i * 3 + j] != "":
                text = BIG_FONT.render(board[i * 3 + j], True, NEON_PINK)
                screen.blit(text, (rect.x + 70, rect.y + 60))

def get_box(pos):
    x, y = pos
    if y < 100:
        return None
    row = (y - 100) // 200
    col = x // 200
    return row * 3 + col

running = True
while running:
    draw_board()
    if winner:
        pygame.draw.rect(screen, NEON_BLUE, (0, 600, WIDTH, 100), 2)
        msg = f"{'Empate' if winner == 'Empate' else f'Ganó {winner}'}"
        screen.blit(BIG_FONT.render(msg, True, WHITE), (150, 630))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not winner:
            idx = get_box(pygame.mouse.get_pos())
            if idx is not None and board[idx] == "":
                if click_sound:
                    click_sound.play()
                board[idx] = turn
                winner = check_winner(board)
                if winner == "X" or winner == "O":
                    if win_sound:
                        win_sound.play()
                elif winner == "Empate":
                    if draw_sound:
                        draw_sound.play()
                else:
                    turn = "O" if turn == "X" else "X"
                    

pygame.quit()