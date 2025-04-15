import pygame
import random
import psycopg2
from datetime import datetime
from color_palette2 import *
pygame.init()

conn = psycopg2.connect(
    dbname="aminasabit",
    user="aminasabit",
    password="1342",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def get_or_create_user(username):
    cur.execute("SELECT id FROM users WHERE username = %s;", (username,))
    user = cur.fetchone()
    if user:
        user_id = user[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id;", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
    cur.execute("SELECT level, score FROM user_score WHERE user_id = %s ORDER BY updated_at DESC LIMIT 1;", (user_id,))
    row = cur.fetchone()
    if row:
        return user_id, row[0], row[1]
    else:
        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s);", (user_id, 0, 1))
        conn.commit()
        return user_id, 1, 0

def save_progress(user_id, score, level):
    cur.execute("INSERT INTO user_score (user_id, score, level, updated_at) VALUES (%s, %s, %s, %s);", (user_id, score, level, datetime.now()))
    conn.commit()

WIDTH = 600
HEIGHT = 600
CELL = 30
COLS = WIDTH // CELL
ROWS = HEIGHT // CELL
FPS = 5
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake with weighted food")
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

# Food with weight and timer
class Food:
    def __init__(self, snake):
        self.snake = snake
        self.pos = Point(0, 0)
        self.weight = 1
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 5000  # food stops showing after 5 seconds
        self.generate_position()
    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
    def generate_position(self):
        while True:
            x = random.randint(0, COLS - 1)
            y = random.randint(0, ROWS - 1)
            if all(segment.x != x or segment.y != y for segment in self.snake.body):
                self.pos = Point(x, y)
                self.weight = random.randint(1, 3)  # random food weight
                self.spawn_time = pygame.time.get_ticks()
                break
    def is_expired(self):
        # Check if timer ended
        return pygame.time.get_ticks() - self.spawn_time > self.lifetime

username = input("Enter your username: ")
user_id, level, score = get_or_create_user(username)
snake = Snake()
food = Food(snake)
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
            elif event.key == pygame.K_p:
                save_progress(user_id, score, level)
                print("Game paused and progress saved.")
                running = False

    snake.move()

    if snake.body[0].x == food.pos.x and snake.body[0].y == food.pos.y:
        score += food.weight
        snake.grow()
        food.generate_position()

        if score // food_to_next_level + 1 > level:
            level += 1
            speed += 2
    if food.is_expired():
        food.generate_position()
    if snake.check_wall_collision() or snake.check_collision_with_self():
        running = False
    snake.draw()
    food.draw()

    score_text = font.render(f"Score: {score}", True, colorWHITE)
    level_text = font.render(f"Level: {level}", True, colorWHITE)
    weight_text = font.render(f"Food: +{food.weight}", True, colorGREEN)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    screen.blit(weight_text, (WIDTH - 120, 10))
    pygame.display.flip()
    clock.tick(speed)
def save_progress(user_id, score, level):
    cur.execute(
        "INSERT INTO user_score (user_id, score, level, updated_at) VALUES (%s, %s, %s, %s);",
        (user_id, score, level, datetime.now())
    )
    conn.commit()
    print(f"[DB] Saved: user_id={user_id}, score={score}, level={level}")

print("Final progress saved.")
cur.execute("SELECT u.username, s.score, s.level FROM users u JOIN user_score s ON u.id = s.user_id ORDER BY s.updated_at DESC LIMIT 1;")
print("[Latest in DB]:", cur.fetchone())
cur.close()
conn.close()
pygame.quit()