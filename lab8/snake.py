import pygame
import random
from color_palette import *

pygame.init()
WIDTH = 600
HEIGHT = 600
CELL = 30
COLS = WIDTH // CELL
ROWS = HEIGHT // CELL
FPS = 5
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 20)

def draw_grid():
    for i in range(ROWS):
        for j in range(COLS):
            pygame.draw.rect(screen, colorGRAY, (j * CELL, i * CELL, CELL, CELL), 1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.grow_flag = False

    def move(self):
        if not self.grow_flag:
            self.body.pop()
        else:
            self.grow_flag = False
        # new head
        new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)
        self.body.insert(0, new_head)

    def grow(self):
        self.grow_flag = True
    def draw(self):
        for i, segment in enumerate(self.body):
            color = colorRED if i == 0 else colorYELLOW
            pygame.draw.rect(screen, color, (segment.x * CELL, segment.y * CELL, CELL, CELL))
    def check_collision_with_self(self):
        head = self.body[0]
        return any(head.x == p.x and head.y == p.y for p in self.body[1:])
    def check_wall_collision(self):
        head = self.body[0]
        return head.x < 0 or head.x >= COLS or head.y < 0 or head.y >= ROWS

# Food
class Food:
    def __init__(self, snake):
        self.snake = snake
        self.pos = Point(0, 0)
        self.generate_position()
    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
    def generate_position(self):
        while True:
            x = random.randint(0, COLS - 1)
            y = random.randint(0, ROWS - 1)
            # Place it right
            if all(segment.x != x or segment.y != y for segment in self.snake.body):
                self.pos = Point(x, y)
                break

snake = Snake()
food = Food(snake)
score = 0
level = 1
speed = FPS
food_to_next_level = 4
running = True
while running:
    screen.fill(colorBLACK)
    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy != 1:
                snake.dx, snake.dy = 0, -1
    snake.move()
    if snake.body[0].x == food.pos.x and snake.body[0].y == food.pos.y:
        score += 1
        snake.grow()
        food.generate_position()

        # New level
        if score % food_to_next_level == 0:
            level += 1
            speed += 2 

    # Check collisions
    if snake.check_wall_collision() or snake.check_collision_with_self():
        running = False
    snake.draw()
    food.draw()
    score_text = font.render(f"Score: {score}", True, colorWHITE)
    level_text = font.render(f"Level: {level}", True, colorWHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()