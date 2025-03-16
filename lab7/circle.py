import pygame
pygame.init()

WIDTH, HEIGHT = 500, 500
BALL_RADIUS = 25
MOVE_SPEED = 20
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
running = True
while running:
    screen.fill(WHITE) 
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)
    pygame.display.flip() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - BALL_RADIUS - MOVE_SPEED >= 0:
                ball_y -= MOVE_SPEED
            elif event.key == pygame.K_DOWN and ball_y + BALL_RADIUS + MOVE_SPEED <= HEIGHT:
                ball_y += MOVE_SPEED
            elif event.key == pygame.K_LEFT and ball_x - BALL_RADIUS - MOVE_SPEED >= 0:
                ball_x -= MOVE_SPEED
            elif event.key == pygame.K_RIGHT and ball_x + BALL_RADIUS + MOVE_SPEED <= WIDTH:
                ball_x += MOVE_SPEED
pygame.quit()