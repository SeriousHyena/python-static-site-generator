from pathlib import Path

class Site:

    def __init__(self, source, dest):
        self.source = source(Path)
        self.dest = dest(Path)
 
