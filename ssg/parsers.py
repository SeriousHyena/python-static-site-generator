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
        with open(path) as file: 
            return path  

