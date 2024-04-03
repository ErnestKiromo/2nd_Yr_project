from gtts import gTTS
import pygame
import os

# Text to be converted to speech
text = "Dreaming of a Future in Computer Science, ML, and AI is like..As a young student entering college or university, the world of Computer Science offers endless possibilities and opportunities for exploration. Many dream of delving into the realms of Machine Learning (ML) and Artificial Intelligence (AI), drawn by the excitement of innovation and the potential to shape the future.Pursuing Computer Science:For those passionate about technology and problem-solving, Computer Science provides a solid foundation."

# Create a gTTS object
tts = gTTS(text=text, lang='en')

# Save the speech as a file
tts.save("output.mp3")

# Initialize pygame mixer
pygame.mixer.init()

# Load the MP3 file
pygame.mixer.music.load("output.mp3")
# play speed
# pygame.mixer.music.set_rate(1.5) 
# Play the MP3 file
pygame.mixer.music.play()

# Wait until the speech finishes playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(30)  # Adjust the playback speed

# Delete the MP3 file after playing
os.remove("output.mp3")
