"""Make a program in Python that opens and plays audio from an MP3 file."""
import pygame
print("Challenge 021")
print("Make a program in Python that opens and plays audio from an MP3 file.")
pygame.init()
pygame.mixer.music.load('Challenge021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
