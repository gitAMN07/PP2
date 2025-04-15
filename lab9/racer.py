import pygame
import random
import time
pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Rush")
background = pygame.image.load('/Users/aminasabit/Desktop/PP2/AnimatedStreet.png')
player_img = pygame.image.load('/Users/aminasabit/Desktop/PP2/Player.png')
enemy_img = pygame.image.load('/Users/aminasabit/Desktop/PP2/Enemy.png')
original_coin_img = pygame.image.load('/Users/aminasabit/Desktop/PP2/Coin.webp')
coin_img = pygame.transform.scale(original_coin_img, (32, 32))

pygame.mixer.music.load('/Users/aminasabit/Desktop/PP2/background.wav')
crash_sound = pygame.mixer.Sound('/Users/aminasabit/Desktop/PP2/crash.wav')
pygame.mixer.music.play(-1)
font_big = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font_big.render("Game Over", True, "black")

PLAYER_SPEED = 5
ENEMY_SPEED = 10
COIN_SPEED = 5
COIN_WEIGHT_OPTIONS = [1, 2, 3]  # Coin weigt
INCREASE_SPEED_EVERY_N_COINS = 5  # Enemy speed increase
clock = pygame.time.Clock()
FPS = 60

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        # Border limits
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIDTH)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.reset_position()
    def move(self):
        self.rect.y += ENEMY_SPEED
        if self.rect.top > HEIGHT:
            self.reset_position()
    def reset_position(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height

# Coins with weight
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.weight = random.choice(COIN_WEIGHT_OPTIONS)
        self.reset_position()
    def move(self):
        self.rect.y += COIN_SPEED
        if self.rect.top > HEIGHT:
            self.reset_position()
    def reset_position(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-150, -50)
        self.weight = random.choice(COIN_WEIGHT_OPTIONS)  # Randomize

player = Player()
enemy = Enemy()
coin = Coin()
all_sprites = pygame.sprite.Group(player, enemy, coin)
enemy_sprites = pygame.sprite.Group(enemy)
coin_sprites = pygame.sprite.Group(coin)
coins_collected = 0

running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.move()
    enemy.move()
    coin.move()
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    if pygame.sprite.spritecollideany(player, coin_sprites):
        coins_collected += coin.weight
        coin.reset_position()
        # Increase speed every N
        if coins_collected % INCREASE_SPEED_EVERY_N_COINS == 0:
            ENEMY_SPEED += 1
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()
        coins_collected -= coin.weight
        coin.reset_position()
        if coins_collected < 0:
            time.sleep(1)
            screen.fill("red")
            center_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(game_over, center_rect)
        pygame.display.flip()
        time.sleep(2)
        break

    coin_text = font_small.render(f"Coins: {coins_collected}", True, "black")
    screen.blit(coin_text, (WIDTH - 120, 10))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()