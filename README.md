# Moneybot

An automated content pipeline that scrapes top Reddit videos and publishes them across Instagram, TikTok, and YouTube, streamlining social media distribution.

## Overview

Moneybot is a comprehensive social media automation tool designed to:

- **Scrape Content**: Automatically discover and download trending videos from Reddit
- **Process Media**: Handle video formatting, compression, and optimization for different platforms
- **Multi-Platform Publishing**: Distribute content across Instagram, TikTok, and YouTube with platform-specific optimizations
- **Scheduling**: Intelligent posting schedules to maximize engagement
- **Analytics**: Track performance across all platforms

## Architecture

The system consists of several modular components:

- **Reddit Video Scraper** (`reddit_video_downloader` branch): Discovers and downloads top videos from Reddit
- **Media Processor**: Handles video editing, compression, and platform-specific formatting
- **Social Media APIs**: Interfaces with Instagram, TikTok, and YouTube APIs for automated posting
- **Scheduler**: Manages posting times and frequencies
- **Analytics Dashboard**: Monitors engagement and performance metrics

## Getting Started

### Prerequisites

- Python 3.8+
- FFmpeg (for video processing)
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Niklas-1999/Moneybot.git
   cd Moneybot
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install FFmpeg:
   - **Windows**: `winget install -e --id BtbN.FFmpeg.GPL.8.1`
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg`

### Usage

Switch to the appropriate branch for the component you want to use:

```bash
# Reddit video downloader
git checkout reddit_video_downloader
python reddit_video_downloader.py
```

## Branches

- `main`: Project overview and documentation
- `reddit_video_downloader`: Automated Reddit video scraping component

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for educational and personal use only. Please respect platform terms of service and Reddit's API usage policies.