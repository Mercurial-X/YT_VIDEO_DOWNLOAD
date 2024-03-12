import os
from pytube import YouTube

# YouTube video URLs to download
video_urls = [

            "https://youtu.be/DH4ugAjuCHA",
            "https://youtu.be/ubkwRMq50p8",
            "https://youtu.be/ENVW3uZ3a-4",
            ""
            "",
    #video_url_here
    
]

# Function to download a video if it's not already downloaded
def download_video(url):
    try:
        yt = YouTube(url)
        output_folder = "downloaded_videos"
        output_path = os.path.join(output_folder, f"{yt.title}.mp4")
        if not os.path.isfile(output_path):
            stream = yt.streams.get_highest_resolution()
            print("Downloading:", yt.title)
            stream.download(output_path=output_folder)
            print("Download completed for:", yt.title)
        else:
            print("Video already downloaded:", yt.title)
    except Exception as e:
        print("Error downloading video from URL:", url)
        print(e)

# Main script execution
if __name__ == "__main__":
    for url in video_urls:
        download_video(url)
