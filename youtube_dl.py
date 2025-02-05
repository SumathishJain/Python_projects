
import yt_dlp

def download_youtube_playlist(playlist_url, output_path=".", start_video=1, end_video=None):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_path}/%(playlist_title)s/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'noplaylist': False,
        'playliststart': start_video,
    }
    if end_video:
        ydl_opts['playlistend'] = end_video

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print("Playlist download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube playlist URL: ")
    start = int(input("Enter the starting video number: "))
    end = input("Enter the ending video number (leave blank for full playlist): ")
    end = int(end) if end else None
    output_directory = r'your path'
    download_youtube_playlist(url, output_directory, start, end)
