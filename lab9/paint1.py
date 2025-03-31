import pygame
import sys
import math
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

            if mode in ['pen', 'eraser']:
                pygame.draw.circle(screen, WHITE if mode == 'eraser' else current_color, start_pos, 5)

        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = pygame.mouse.get_pos()

            x1, y1 = start_pos
            x2, y2 = end_pos

            width = x2 - x1
            height = y2 - y1

            if drawing:
                if mode == 'rect':
                    pygame.draw.rect(screen, current_color, (x1, y1, width, height), 2)

                elif mode == 'circle':
                    radius = int(math.hypot(width, height))
                    pygame.draw.circle(screen, current_color, start_pos, radius, 2)

                #draw square
                elif mode == 'square':
                    side = min(abs(width), abs(height))
                    pygame.draw.rect(screen, current_color, (x1, y1, side * (1 if width >= 0 else -1), side * (1 if height >= 0 else -1)), 2)
               
                #draw right triangle
                elif mode == 'right_triangle':
                    pygame.draw.polygon(screen, current_color, [start_pos, (x1, y2), end_pos], 2)

                #draw equilateral triangle
                elif mode == 'equilateral_triangle':
                    side = math.hypot(width, height)
                    height_eq = (3**0.5 / 2) * side
                    pygame.draw.polygon(screen, current_color, [
                        (x1, y2),
                        (x1 + side, y2),
                        (x1 + side/2, y2 - height_eq)
                    ], 2)

                #draw rhomb
                elif mode == 'rhombus':
                    mid_x = (x1 + x2) // 2
                    mid_y = (y1 + y2) // 2
                    pygame.draw.polygon(screen, current_color, [
                        (mid_x, y1), 
                        (x2, mid_y), 
                        (mid_x, y2), 
                        (x1, mid_y) 
                    ], 2)
                    
            drawing = False

        elif event.type == pygame.MOUSEMOTION:
            if drawing and mode in ['pen', 'eraser']:
                end_pos = pygame.mouse.get_pos()
                pygame.draw.line(screen, WHITE if mode == 'eraser' else current_color, start_pos, end_pos, 5)
                start_pos = end_pos

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = 'rect'
            elif event.key == pygame.K_c:
                mode = 'circle'
            elif event.key == pygame.K_p:
                mode = 'pen'
            elif event.key == pygame.K_e:
                mode = 'eraser'
            elif event.key == pygame.K_s:
                mode = 'square'
            elif event.key == pygame.K_t:
                mode = 'right_triangle'
            elif event.key == pygame.K_h:
                mode = 'rhombus'
            elif event.key == pygame.K_q:
                mode = 'equilateral_triangle'
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