import requests
import yt_dlp
import json
import os
import time
from datetime import datetime

# Configuration - Change these values as needed
SUBREDDIT = 'funny'
DOWNLOAD_DIR = os.path.expanduser('~/Videos')  # Default Windows Videos folder; change to any path
INTERVAL_SECONDS = 30  # 5 minutes; change to desired interval in seconds
JSON_FILE = 'downloaded_videos.json'

def get_top_video_last_24h():
    """Fetch all video posts from the last 24 hours in the subreddit, sorted by upvotes."""
    # Use 'new' sorting to get recent posts, then filter and sort by score
    url = f'https://www.reddit.com/r/{SUBREDDIT}/new.json?limit=100'
    headers = {'User-Agent': 'RedditVideoDownloader/1.0'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        videos = []
        current_time = datetime.now().timestamp()
        twenty_four_hours_ago = current_time - 86400
        
        for post in data['data']['children']:
            post_data = post['data']
            if post_data['created_utc'] > twenty_four_hours_ago:
                # Check if it's a video post
                if post_data.get('is_video', False) and 'media' in post_data and post_data['media']:
                    videos.append({
                        'url': post_data['url'],
                        'id': post_data['id'],
                        'score': post_data['score'],
                        'title': post_data['title'],
                        'created_utc': post_data['created_utc']
                    })
            else:
                # Since posts are sorted by new, we can break early
                break
        
        if videos:
            # Sort by score (upvotes) to get the most upvoted videos first
            videos.sort(key=lambda p: p['score'], reverse=True)
            return videos
    except Exception as e:
        print(f"Error fetching posts: {e}")
    
    return []

def download_video(url, download_dir):
    """Download the video using yt-dlp."""
    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',
        'noplaylist': True,
        'quiet': False,
        'no_warnings': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    # Ensure download directory exists
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    
    # Load or create downloaded videos list
    if not os.path.exists(JSON_FILE):
        downloaded_ids = []
    else:
        with open(JSON_FILE, 'r') as f:
            downloaded_ids = json.load(f)
    
    print(f"Starting video downloader. Checking every {INTERVAL_SECONDS} seconds.")
    print(f"Downloading to: {DOWNLOAD_DIR}")
    
    while True:
        try:
            # Get all videos from last 24 hours, sorted by upvotes
            videos = get_top_video_last_24h()
            
            if videos:
                downloaded_count = 0
                for video in videos:
                    url, video_id = video['url'], video['id']
                    if video_id not in downloaded_ids:
                        print(f"Downloading video: {video_id} (score: {video['score']})")
                        download_video(url, DOWNLOAD_DIR)
                        downloaded_ids.append(video_id)
                        
                        # Save updated list after each download
                        with open(JSON_FILE, 'w') as f:
                            json.dump(downloaded_ids, f, indent=2)
                        print(f"Downloaded and saved video ID: {video_id}")
                        downloaded_count += 1
                        
                        # Optional: limit downloads per run to avoid overwhelming
                        if downloaded_count >= 5:  # Download up to 5 videos per run
                            break
                    else:
                        print(f"Video {video_id} already downloaded. Skipping.")
            else:
                print("No video posts found in the last 24 hours.")
            
            time.sleep(INTERVAL_SECONDS)
            
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(INTERVAL_SECONDS)  # Continue even if there's an error

if __name__ == '__main__':
    main()