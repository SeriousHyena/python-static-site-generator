from pathlib import Path

class Site:

    def __init__(self, source, dest):
        self._source = source(Path)
        self._dest = dest(Path)
 
