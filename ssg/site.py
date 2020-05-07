from pathlib import Path

class Site:

    def __init__(self, source, dest, parsers=None): # this is the class constructor
        '''Find the root directory.'''
        self.source = Path(source)
        self.dest = Path(dest)

        '''Instance variable tutorial here:
        https://www.digitalocean.com/community/tutorials/understanding-class-and-instance-variables-in-python-3'''
        self.parsers = parsers or [] # this is my new instance variable for 


 
    def create_dir(self, path):
        '''Create the directory but see if it exists before we create it.'''
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

     
    def build(self):
        '''Now we can create then directory.  Path.rglob(pattern) to find the match we want'''
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)

    def load_parser(self, extension):
        for parser in self.parsers:
            if parser.valid_extension(extension): # parser is an extension of Parser class so dot.chain the method
                return parser

    def run_parser(self, path):
        parser = load_parser(path.suffix) #From pathlib- .suffix = The file extension of the final component, if any.