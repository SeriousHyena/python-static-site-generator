from typing import List
from pathlib import Path #https://docs.python.org/3/library/pathlib.html
import shutil # https://docs.python.org/3/library/shutil.html

'''This module uses Typer. More information about Typer here:
https://typer.tiangolo.com/#example'''

class Parser:

    extensions: List[str] = []

    def valid_extension(self, extension):  
        return extension in self.extensions
        
    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path, 'r', encoding='utf-8') as file: # Use r to open for reading
            return file.read() 

    def write(self, path, dest, content, ext='.html'):
        full_path = dest / path.with_suffix(ext).name # .name = A string representing the final path component, excluding the drive and root, if any
        with open(full_path, 'w') as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest / path.relative_to(source))

class ResourceParser(Parser):
    '''Good tutorial here for implementing class methods: 
    https://www.geeksforgeeks.org/classmethod-in-python/'''
    def __init__(self, extensions):
        extensions = ['.jpg', '.png', '.gif', '.css', '.html']
        self._extensions = extensions

    def parse(self, path: Path, source: Path, dest: Path):
        self.copy(path, source, dest)


