import pygame
import os
pygame.init()
pygame.mixer.init()

MUSIC_FOLDER = "music"
playlist = [os.path.join(MUSIC_FOLDER, file) for file in os.listdir(MUSIC_FOLDER) if file.endswith(".mp3")]
if not playlist:
    print("No music files found in 'music' folder.")
    exit()

current_song = 0
def play_song(index):
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()
    print(f"Playing: {os.path.basename(playlist[index])}")

play_song(current_song) 
running = True
paused = False  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: 
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    print("Paused")
                    paused = True
                else:
                    pygame.mixer.music.unpause()
                    print("Resumed")
                    paused = False
            elif event.key == pygame.K_s: 
                pygame.mixer.music.stop()
                print("Stopped")
                paused = False 
            elif event.key == pygame.K_n: 
                current_song = (current_song + 1) % len(playlist)
                play_song(current_song)
                paused = False 
            elif event.key == pygame.K_b: 
                current_song = (current_song - 1) % len(playlist)
                play_song(current_song)
                paused = False 
pygame.quit()