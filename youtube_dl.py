
# import yt_dlp

# def download_youtube_video(video_url, output_path="."):
#     ydl_opts = {
#         'format': 'best',  # Best quality video and audio
#         'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save format
#     }
#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([video_url])
#         print("Download completed successfully!")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     url = input("Enter the YouTube video URL: ")
#     output_directory = r'C:\Users\SUMATHISH JAIN B R\Videos\YouTube'
#     download_youtube_video(url, output_directory)


# import yt_dlp

# def download_youtube_playlist(playlist_url, output_path="."):
#     ydl_opts = {
#         'format': 'best',  # Best quality video and audio
#         'outtmpl': f'{output_path}/%(playlist_title)s/%(title)s.%(ext)s',  # Organize videos in a folder named after the playlist
#         'noplaylist': False,  # Ensure playlists are treated as playlists
#     }
#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([playlist_url])
#         print("Playlist download completed successfully!")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     url = input("Enter the YouTube playlist URL: ")
#     output_directory = r'C:\Users\SUMATHISH JAIN B R\Videos\YouTube\Python_in_100_days'
#     download_youtube_playlist(url, output_directory)



import yt_dlp

def download_youtube_playlist(playlist_url, output_path=".", start_video=1, end_video=None):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_path}/%(playlist_title)s/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'noplaylist': False,
        'playliststart': start_video,
    }
    if end_video:  # Add playlistend if specified
        ydl_opts['playlistend'] = end_video

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print("Playlist download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube playlist URL: ")
    start = int(input("Enter the starting video number: "))  # Specify start video
    end = input("Enter the ending video number (leave blank for full playlist): ")
    end = int(end) if end else None  # Convert input to integer or leave as None
    output_directory = r'C:\Users\SUMATHISH JAIN B R\Videos'
    download_youtube_playlist(url, output_directory, start, end)
