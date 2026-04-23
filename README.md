# Reddit Video Downloader

A component of the Moneybot automated content pipeline that scrapes and downloads top videos from Reddit subreddits.

## Overview

This module automatically discovers and downloads the most upvoted videos from Reddit in the last 24 hours. It's designed as part of a larger social media automation pipeline, providing fresh content for distribution across multiple platforms.

## Features

- **Automated Discovery**: Fetches videos from configurable subreddits using Reddit's public API
- **Quality Selection**: Downloads videos in the best available quality with audio
- **Duplicate Prevention**: Tracks downloaded videos to avoid re-downloading
- **Batch Processing**: Downloads multiple videos per run (up to 5) in order of popularity
- **Configurable**: Easy to change subreddit, download directory, and check intervals
- **24/7 Operation**: Designed for continuous operation on cloud servers
- **Cross-Platform**: Works on Windows, Linux, and macOS

## Installation

### Prerequisites

- Python 3.8+
- FFmpeg (for video merging)
- Git

### Setup Steps

1. **Clone and switch to the branch:**
   ```bash
   git clone https://github.com/Niklas-1999/Moneybot.git
   cd Moneybot
   git checkout reddit_video_downloader
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install FFmpeg:**
   - **Windows**: `winget install -e --id BtbN.FFmpeg.GPL.8.1`
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg`

4. **Configure the script:**
   Edit `reddit_video_downloader.py` to customize:
   - `SUBREDDIT`: Change from 'funny' to any subreddit
   - `DOWNLOAD_DIR`: Set your preferred download directory
   - `INTERVAL_SECONDS`: Adjust check frequency (default: 30 seconds for testing)

## Usage

Run the downloader:
```bash
python reddit_video_downloader.py
```

The script will:
1. Check for new videos every configured interval
2. Download up to 5 undownloaded videos per check, sorted by upvotes
3. Save videos to the configured directory
4. Track downloaded videos in `downloaded_videos.json`

## Configuration

Key settings in `reddit_video_downloader.py`:

```python
SUBREDDIT = 'funny'                    # Target subreddit
DOWNLOAD_DIR = os.path.expanduser('~/Videos')  # Download location
INTERVAL_SECONDS = 30                  # Check frequency
```

## Output

- Videos are saved as MP4 files with audio
- `downloaded_videos.json` tracks processed video IDs
- Console output shows download progress and status

## Integration

This component feeds into the larger Moneybot pipeline:

1. **Input**: Reddit API (no authentication required)
2. **Output**: Downloaded MP4 videos ready for processing
3. **Next Steps**: Video editing, platform-specific formatting, automated posting

## Notes

- Uses Reddit's public JSON API to avoid authentication requirements
- Respects rate limits with configurable intervals
- Includes error handling for network issues and API changes
- Videos are filtered to those posted in the last 24 hours

## Troubleshooting

- **No videos found**: Check subreddit name and ensure it has recent video content
- **Download fails**: Verify FFmpeg installation and internet connection
- **Permission errors**: Ensure write access to the download directory

## License

Part of the Moneybot project - see main branch for license details.