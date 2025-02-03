import os
from time import sleep

# Song filename
song_file_name = 'surprise.MP3'

# Construct the command for playing the song
song_command = f'mpg123 -q {song_file_name} &'

# Pass a command to the operating system to announce the song name using Festival
os.system(f"echo 'playing song {song_file_name}' | festival --tts")

# Print files in the current directory (optional)
print(os.system("ls"))

# Play the song
os.system(song_command)
print(f"Now playing: {song_file_name}")

# Wait while the song plays (adjust sleep duration as needed)
sleep(30)

# Stop the song playback by killing the mpg123 process
os.system('pkill mpg123')
