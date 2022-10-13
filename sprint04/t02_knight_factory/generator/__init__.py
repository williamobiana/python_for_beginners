# from .file import file
# Where '.file' is the name of the module/file and 'file' is the name of the function
# eg:
# from .name import name or 
# from . import name

from . import names, titles
import logging
import sys

logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='..::Knight Generator::.. %(process)d-%(levelname)s-%(message)s')


