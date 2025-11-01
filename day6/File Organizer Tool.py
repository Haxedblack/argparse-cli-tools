import argparse 
from pathlib import Path 
from colorma import init, Force

init(autoreset=True)

FILE_TYPE_MAP = {
    "Images": ['.jpeg', '.jpg', '.png', '.gif', '.svg'],
    "Documents": ['.pdf', '.docx', '.doc', '.txt', '.xls', '.ppt', '.xlsx'],
    "Video": ['.mp4', '.mov', '.avi', 'mkv'],
    "Music": ['.mp3', '.wav', '.flac'],
    "Code": ['.py', '.js',  '.html', '.css', '.java', '.c', '.cpp'],
    "Archives": ['.zip', '.rar', 'tar.gz', '.7z'],
}
