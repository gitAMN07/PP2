import pygame
import math
import time
pygame.init()

WIDTH, HEIGHT = 500, 500
CENTER = (WIDTH // 2, HEIGHT // 2)
back = pygame.image.load("clock1.jpeg")
back = pygame.transform.scale(back, (WIDTH, HEIGHT)) 
minute = pygame.image.load("min_hand.png") 
second = pygame.image.load("sec_hand.png") 
minute = pygame.transform.scale(minute, (890, 600))  
second = pygame.transform.scale(second, (850, 800))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Time")

def rotate_hand(image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=pivot)
    return rotated_image, new_rect

running = True
while running:
    screen.fill((255, 255, 255))  
    screen.blit(back, (0, 0))

    t = time.localtime()
    minutes = t.tm_min
    seconds = t.tm_sec

    minute_angle = (minutes % 60) * 6 
    second_angle = (seconds % 60) * 6 
    
    rotated_minute, min_rect = rotate_hand(minute, minute_angle, CENTER)
    rotated_second, sec_rect = rotate_hand(second, second_angle, CENTER)

    screen.blit(rotated_minute, min_rect.topleft)
    screen.blit(rotated_second, sec_rect.topleft)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1000)
pygame.quit()