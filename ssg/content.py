import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def load(self, cls, string):
        '''according to pep 8 Always use self for the first argument to instance methods and 
        Always use cls for the first argument to class methods.
        https://www.python.org/dev/peps/pep-0008/#function-and-method-arguments'''

        _, fm, content = cls.__regex.split(string, 2) # here we use cls per pep 8
        metadata = load(fm, Loader=FullLoader)
        return cls(metadata, content)

         