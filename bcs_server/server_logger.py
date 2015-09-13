#!usr/bin/env python
#-*-coding:utf8-*-

__doc__ = """
    Logging reference: https://pymotw.com/2/logging/

    Level   Value
    -------------
    CRITICAL    50
    ERROR       40
    WARNING     30
    INFO        20
    DEBUG       10
    UNSET        0

"""

import sys
import logging
from logging import handlers
from config import LOG_FILENAME, MAX_SIZE_IN_KB, NUMBER_OF_FILES

_serverLogger = logging.getLogger('bcs_server')
_serverLogger.setLevel(logging.DEBUG)
_formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s', '%b %d,%Y %I:%M:%S %p')

# define a Handler which writes INFO messages or higher to the sys.stderr
_console = logging.StreamHandler(sys.stdout)
_console.setFormatter(_formatter)
# Define a handler which writes Debug messages or higher to log files
_file_handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=MAX_SIZE_IN_KB*1024,
                                                     backupCount=NUMBER_OF_FILES,)
_file_handler.setFormatter(_formatter)

# Print logs with level info and above on screen
_console.setLevel(logging.INFO)
# Save logs with level debug and above in files
_file_handler.setLevel(logging.DEBUG)

_serverLogger.addHandler(_console)
_serverLogger.addHandler(_file_handler)

log = _serverLogger
