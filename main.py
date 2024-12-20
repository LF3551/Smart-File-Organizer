import os
import shutil
from argparse import ArgumentParser

def organize_files(directory):
    categories = {
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'Archives': ['.zip', '.tar', '.rar', '.7z'],
        'Others': []
    }

    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        if os.path.isfile(filepath):
            file_ext = os.path.splitext(filename)[-1].lower()
            moved = False

            for category, extensions in categories.items():
                if file_ext in extensions:
                    category_dir = os.path.join(directory, category)
                    if not os.path.exists(category_dir):
                        os.makedirs(category_dir)
                    shutil.move(filepath, os.path.join(category_dir, filename))
                    print(f"Moved: {filename} -> {category}/")
                    moved = True
                    break

            if not moved:
                other_dir = os.path.join(directory, 'Others')
                if not os.path.exists(other_dir):
                    os.makedirs(other_dir)
                shutil.move(filepath, os.path.join(other_dir, filename))
                print(f"Moved: {filename} -> Others/")


def main():
    parser = ArgumentParser(description="Smart File Organizer - Automatically organize files into categories.")
    parser.add_argument('--directory', '-d', required=True, help="Path to the directory to organize")

    args = parser.parse_args()

    organize_files(args.directory)

if __name__ == "__main__":
    main()
