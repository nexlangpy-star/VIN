import os
import sys
from .TOP import *
lib_dir = os.path.dirname(__file__)
os.environ['LD_LIBRARY_PATH'] = lib_dir + ':' + os.environ.get('LD_LIBRARY_PATH', '')

if lib_dir not in sys.path:
    sys.path.insert(0, lib_dir)
__version__ = "1.0.0"