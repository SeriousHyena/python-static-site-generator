'''Here we will set up the CLI.'''

import typer # I will need to pip install this module (https://pypi.org/project/typer/)
from ssg.site import Site

def main(source='content', dest='dist'):
    config = {'source': source, 'dest': dest}

    foo = Site(**config).build()