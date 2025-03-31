import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Drawing Tool")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
PURPLE = (128, 0, 128)
colors = [BLACK, RED, GREEN, BLUE, PURPLE]
current_color = BLACK

mode = 'pen'

drawing = False
start_pos = (0, 0)

screen.fill(WHITE)

def draw_palette():
    for i, color in enumerate(colors):
        pygame.draw.rect(screen, color, (10 + i*40, 10, 30, 30))
        if current_color == color:
            pygame.draw.rect(screen, BLACK, (10 + i*40, 10, 30, 30), 2)

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pygame.mouse.get_pos()
            if start_pos[1] <= 40:
                for i, color in enumerate(colors):
                    if 10 + i*40 <= start_pos[0] <= 40 + i*40 and 10 <= start_pos[1] <= 40:
                        current_color = color
            if mode == 'pen' or mode == 'eraser':
                pygame.draw.circle(screen, WHITE if mode == 'eraser' else current_color, start_pos, 5)

        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = pygame.mouse.get_pos()
            if drawing and mode == 'rect':
                rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, current_color, rect, 2)
            elif drawing and mode == 'circle':
                radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)
            drawing = False

        elif event.type == pygame.MOUSEMOTION:
            if drawing and (mode == 'pen' or mode == 'eraser'):
                end_pos = pygame.mouse.get_pos()
                pygame.draw.line(screen, WHITE if mode == 'eraser' else current_color, start_pos, end_pos, 5)
                start_pos = end_pos

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = 'rect'
            elif event.key == pygame.K_c:
                mode = 'circle'
            elif event.key == pygame.K_e:
                mode = 'eraser'
            elif event.key == pygame.K_p:
                mode = 'pen'
            elif event.key == pygame.K_1:
                current_color = colors[0]
            elif event.key == pygame.K_2:
                current_color = colors[1]
            elif event.key == pygame.K_3:
                current_color = colors[2]
            elif event.key == pygame.K_4:
                current_color = colors[3]
            elif event.key == pygame.K_5:
                current_color = colors[4]

    draw_palette()
    pygame.display.flip()