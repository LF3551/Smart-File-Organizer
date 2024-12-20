# Smart File Organizer

**Smart File Organizer** is a Python-based CLI tool for automatically organizing files into categories such as documents, images, audio, and more. Perfect for keeping your workspace or downloads folder neat and tidy.

## Features
- Automatically organize files by type.
- Supports categories like Documents, Images, Audio, Videos, Archives, and Others.
- Quick and lightweight CLI interface.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/LF3551/Smart-File-Organizer.git
   cd SmartFileOrganizer
   ```


## Usage

### Organizing Files
1. Prepare a folder with files to organize. For example:
   ```bash
   mkdir test_files
   touch test_files/document.pdf test_files/image.jpg test_files/song.mp3 test_files/video.mp4 test_files/archive.zip test_files/unknown_file.xyz
   ```

2. Run the script to organize the files:
   ```bash
   python main.py --directory test_files
   ```

3. After execution, the files will be sorted into subfolders like `Documents`, `Images`, `Audio`, etc.
   Example output:
   ```plaintext
   Moved: document.pdf -> Documents/
   Moved: unknown_file.xyz -> Others/
   Moved: video.mp4 -> Videos/
   Moved: archive.zip -> Archives/
   Moved: image.jpg -> Images/
   Moved: song.mp3 -> Audio/
   ```

## License

This project is open-sourced under the Universal Permissive License (UPL), Version 1.0. See the LICENSE file for more details.
