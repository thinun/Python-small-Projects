from moviepy.editor import *

video = VideoFileClip("Thunderstruck.mp4")
audio_name = 'audio'
mp3 = '.mp3'
audio_file_name = audio_name + mp3


audio = video.audio
audio.write_audiofile(audio_file_name)
