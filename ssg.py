import ssg.parsers

'''Here we will set up the CLI.'''

import typer # I will need to pip install this module (https://pypi.org/project/typer/)
from ssg.site import Site

def main(source='content', dest='dist'):
    config = {'source': source, 
        'dest': dest, 
        'parsers': [ssg.parsers.ResourceParser()]} # This key-value pair produces an array hence the square brackets

    Site(**config).build()

typer.run(main)