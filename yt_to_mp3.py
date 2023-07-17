import os
import subprocess
from youtube_dl import YoutubeDL

def check_ffmpeg():
    try:
        # Try to call ffmpeg
        subprocess.call(['ffmpeg', '-version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("ffmpeg is installed.")
    except FileNotFoundError:
        # If ffmpeg is not found, print a message
        print("ffmpeg is not installed. Please download it from the official website: https://www.ffmpeg.org/download.html")
        print("After downloading, please add it to your system's PATH.")
        sys.exit(1)

def download_audio():
    check_ffmpeg()

    video_url = input("Please enter the YouTube video URL: ")

    # Options for youtube-dl
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s'
    }

    # Download video
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)

if __name__ == "__main__":
    download_audio()
