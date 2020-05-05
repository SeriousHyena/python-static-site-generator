from pathlib import Path

class Site:
    

    def __init__(self, source, dest):
        '''Find the root directory.'''
        self.source = Path(source)
        self.dest = Path(dest)
 
    def create_dir(self, path):
        '''See if a directory exists before we create it.'''
        directory = self.dest / path.relative_to(self.source)
        Path.mkdir(directory, parents=True, exist_ok=True)
     
    def build(self):
        '''Now we can create then directory.  Path.rglob(pattern) to find the match we want'''
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)