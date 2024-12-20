# Smart File Organizer is open-sourced under the Universal Permissive License (UPL), Version 1.0
# See the LICENSE file in the repository for more details.


import unittest
import os
from tempfile import TemporaryDirectory
from main import organize_files
import logging

class TestFileOrganizer(unittest.TestCase):
    def setUp(self):

        self.test_dir = TemporaryDirectory()
        self.directory = self.test_dir.name


        self.files = [
            "document.pdf",
            "spreadsheet.xlsx",
            "image.jpg",
            "song.mp3",
            "video.mp4",
            "archive.zip",
            "unknown_file.xyz"
        ]

        for file in self.files:
            with open(os.path.join(self.directory, file), 'w') as f:
                f.write("Test content")

    def tearDown(self):
  
        self.test_dir.cleanup()

    def test_organize_files(self):
      
        organize_files(self.directory)

        expected_structure = {
            "Documents": ["document.pdf", "spreadsheet.xlsx"],
            "Images": ["image.jpg"],
            "Audio": ["song.mp3"],
            "Videos": ["video.mp4"],
            "Archives": ["archive.zip"],
            "Others": ["unknown_file.xyz"]
        }

        # Проверка структуры
        for category, files in expected_structure.items():
            category_path = os.path.join(self.directory, category)
            self.assertTrue(os.path.exists(category_path), f"Category {category} folder does not exist.")
            organized_files = os.listdir(category_path)
            self.assertEqual(set(organized_files), set(files), f"Files in {category} folder do not match expected.")

def test_nonexistent_directory(self):
    nonexistent_dir = os.path.join(self.directory, "nonexistent")

    with self.assertLogs(level="ERROR") as log:
        organize_files(nonexistent_dir)
    
  
    self.assertTrue(any(f"Error: Directory '{nonexistent_dir}' does not exist." in message for message in log.output))


if __name__ == "__main__":
    unittest.main()
