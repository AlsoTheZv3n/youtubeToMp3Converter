from pytube import YouTube
import os

def download_audio(url, output_path):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        if audio_stream:
            audio_stream.download(output_path=output_path, filename='temp')
            return True
        else:
            print("Error: No audio stream available for the given URL.")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    youtube_url = input("Enter YouTube URL: ")

    # Output directory path should not include the output filename
    output_directory = input("Enter output directory path: ")
    output_filename = input("Enter output filename (without extension): ")
    output_path = os.path.join(output_directory, output_filename + '.mp3')

    # Ensure output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Download audio stream
    if download_audio(youtube_url, output_directory):
        print("Audio downloaded successfully.")
    else:
        print("Audio download failed!")
