import pygame
import random
import time

pygame.init()
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load('/Users/aminasabit/Desktop/PP2/AnimatedStreet.png')
clock = pygame.time.Clock()
FPS = 60

player_img = pygame.image.load('/Users/aminasabit/Desktop/PP2/Player.png')
enemy_img = pygame.image.load('/Users/aminasabit/Desktop/PP2/Enemy.png')
original_coin_img = pygame.image.load('/Users/aminasabit/Desktop/PP2/Coin.webp') # add coin pic
coin_img = pygame.transform.scale(original_coin_img, (32, 32))  # 32x32 px
background_music = pygame.mixer.music.load('/Users/aminasabit/Desktop/PP2/background.wav')
crash_sound = pygame.mixer.Sound('/Users/aminasabit/Desktop/PP2/crash.wav')
pygame.mixer.music.play(-1) 
font_big = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font_big.render("Game Over", True, "black")
PLAYER_SPEED = 5
ENEMY_SPEED = 10
COIN_SPEED = 5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - self.rect.w // 2
        self.rect.y = HEIGHT - self.rect.h

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.generate_random_rect()
    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()
    def generate_random_rect(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = 0

# Coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.reset_position()

    def move(self):
        self.rect.move_ip(0, COIN_SPEED)
        if self.rect.top > HEIGHT:
            self.reset_position()

    def reset_position(self):
        max_x = max(0, WIDTH - self.rect.width)
        self.rect.x = random.randint(0, max_x)
        self.rect.y = random.randint(-100, -40)

player = Player()
enemy = Enemy()
coin = Coin()
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

all_sprites.add([player, enemy, coin])
enemy_sprites.add(enemy)
coin_sprites.add(coin)

# Coins counter
coins_collected = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
    player.move()
    enemy.move()
    coin.move()
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # Coin collection
    if pygame.sprite.spritecollideany(player, coin_sprites):
        coins_collected += 1
        coin.reset_position()
    # Draw coin counter
    coin_text = font_small.render(f"Coins: {coins_collected}", True, "black")
    screen.blit(coin_text, (WIDTH - 100, 10))

    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()
        time.sleep(1)
        screen.fill("red")
        center_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over, center_rect)
        pygame.display.flip()
        time.sleep(2)
        running = False

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()