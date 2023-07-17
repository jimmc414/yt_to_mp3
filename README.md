
# YouTube Audio Downloader

This Python program allows you to download the audio from a YouTube video as an MP3 file.

## Prerequisites

Before you can run this program, you will need to have the following installed:

- Python 3.6 or later
- `youtube_dl` Python module
- `ffmpeg`

### Python

You can download Python from the [official website](https://www.python.org/downloads/).

### `youtube_dl`

Once you have Python installed, you can install `youtube_dl` with pip:

```bash
pip install youtube_dl
```

### `ffmpeg`

The installation of `ffmpeg` varies depending on your operating system.

**On Windows:**

1. Download `ffmpeg` from the [official website](https://www.ffmpeg.org/download.html).
2. Extract the downloaded file.
3. Add the `bin` directory from the extracted folder to your system's PATH.

To add the `ffmpeg` bin directory to your PATH, you can use the following command in a new Command Prompt window:

```bash
setx /M PATH "%PATH%;C:\\path\\to\\your\\ffmpeg\\bin"
```

Replace `C:\\path\\to\\your\\ffmpeg\\bin` with the actual path to the `bin` directory where you extracted `ffmpeg`.

**On Linux (Debian-based distributions):**

You can install `ffmpeg` from the official repositories:

```bash
sudo apt update
sudo apt install ffmpeg
```

## Usage

To run the program, navigate to the directory containing the Python script in a Command Prompt or Terminal window, then enter the following command:

```bash
python yt_to_mp3.py
```


When prompted, enter the URL of the YouTube video you want to download the audio from. The program will download the audio and save it as an MP3 file in the same directory.

Please ensure that you have the necessary permissions to download and use the content from YouTube videos, as unauthorized downloading or use may infringe on the rights of the content owner.
