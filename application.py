import sys

# There may be a better way to do this...
#sys.path.insert(0, 'b2')

from pyramid.paster import get_app, setup_logging
from b2 import main

ini_path = 'development.ini'
setup_logging(ini_path)
application = main({})
#application = get_app(ini_path, 'main')
