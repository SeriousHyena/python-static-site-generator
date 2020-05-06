from typing import List
from pathlib import Path

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
            return path.read()  

