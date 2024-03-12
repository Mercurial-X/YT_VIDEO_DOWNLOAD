from flask import Flask, render_template, request
import os
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    if data and 'videoId' in data:
        video_id = data['videoId']
        # Call the Python script to download the video
        download_video(video_id)
        return '', 200  # Return success response
    else:
        return '', 400  # Return bad request response if videoId is missing or invalid

def download_video(video_id):
    try:
        yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
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
        print("Error downloading video with ID:", video_id)
        print(e)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
