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

def organize_directory(path: Path):
    """
    Organizes files in the given directory by moving them into subdirectories
    based on their file type.
    """
    if not path.is_dir():
        print(Fore.RED + f"Error: '{path}' is not a valid directory.")
        return

    for item in path.iterdir():
        if item.is_file():
            # Don't move the script itself!
            if item.name == "organizer.py":
                continue

            file_extension = item.suffix.lower()
            moved = False

            for dir_name, extensions in FILE_TYPE_MAP.items():
                if file_extension in extensions:
                    target_dir = path / dir_name
                    target_dir.mkdir(exist_ok=True)
                    item.rename(target_dir / item.name)
                    print(f"{Fore.GREEN}Moved '{item.name}' to '{dir_name}'")
                    moved = True
                    break

            if not moved:
                print(f"{Fore.YELLOW}Skipped '{item.name}' (unknown file type)")

def main():
    parser = argparse.ArgumentParser(description="File Organizer CLI Tool")
    parser.add_argument("--path", type=str, required=True, help="Path to the directory to organize")
    args = parser.parse_args()

    # Convert the string from argparse into a Path object and call the function
    organize_directory(Path(args.path))

if __name__ == "__main__":
    main()
