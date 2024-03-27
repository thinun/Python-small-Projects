from moviepy.editor import *


def converter(video_file, audio_file_name):
    try:
        clip = VideoFileClip(video_file)
        audio = clip.audio
        audio.write_audiofile(audio_file_name)
        clip.close()
    except OSError:
        print("File Not Found !!")


if __name__ == "__main__":
    video = input('Enter the video file name: ').strip()
    audio_file = input('Enter the audio file name: ').strip()
    mp3 = '.mp3'
    mp4 = '.mp4'
    audio = audio_file + mp3
    video_file = video + mp4

    converter(video_file, audio)
