"""
Task 7-2:
Implementation of Directory and File classes with type annotations.
Includes a tree-like string representation for directories.
"""

from __future__ import annotations
from typing import List, Optional


class File:
    """Represents a file inside a directory."""

    def __init__(self, name: str, directory: Optional[Directory] = None) -> None:
        self.name: str = name
        self.directory: Optional[Directory] = directory

    def __repr__(self) -> str:
        return f"File(name='{self.name}')"


class Directory:
    """Represents a directory that can contain files and subdirectories."""

    def __init__(self, name: str, root: Optional[Directory] = None) -> None:
        self.name: str = name
        self.root: Optional[Directory] = root
        self.files: List[File] = []
        self.sub_directories: List[Directory] = []

    def add_sub_directory(self, sub_dir: Directory) -> None:
        """Add a subdirectory and set its root."""
        sub_dir.root = self
        self.sub_directories.append(sub_dir)

    def remove_sub_directory(self, sub_dir: Directory) -> None:
        """Remove a subdirectory and reset its root."""
        if sub_dir in self.sub_directories:
            sub_dir.root = None
            self.sub_directories.remove(sub_dir)

    def add_file(self, file: File) -> None:
        """Add a file to this directory and set its directory reference."""
        file.directory = self
        self.files.append(file)

    def remove_file(self, file: File) -> None:
        """Remove a file from this directory and reset its directory reference."""
        if file in self.files:
            file.directory = None
            self.files.remove(file)

    def __repr__(self) -> str:
        return f"Directory(name='{self.name}')"

    def __str__(self, level: int = 0) -> str:
        """Return a formatted tree-like view of the directory structure."""
        indent = "    " * level
        result = f"{indent}📁 {self.name}\n"

        for file in self.files:
            result += f"{indent}    📄 {file.name}\n"

        for sub_dir in self.sub_directories:
            result += sub_dir.__str__(level + 1)

        return result


if __name__ == "__main__":
    # Example usage
    root_dir = Directory("root")
    docs = Directory("documents")
    images = Directory("images")
    music = Directory("music")

    file1 = File("notes.txt")
    file2 = File("report.pdf")
    img1 = File("photo.jpg")
    song = File("song.mp3")

    root_dir.add_sub_directory(docs)
    root_dir.add_sub_directory(images)
    root_dir.add_sub_directory(music)

    docs.add_file(file1)
    docs.add_file(file2)
    images.add_file(img1)
    music.add_file(song)

    print(root_dir)
