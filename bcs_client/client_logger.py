#!usr/bin/env python
# -*-coding:utf8-*-

import sys
import logging
from logging import handlers

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


    We have different logging requirements for client.

    * Unlike server, there can be different clients running on same machine.
    * Every client should have it's own logger
    * Messages cannot be printed on screen, only in files.

    Therefore each client has a different log file identified by
    it's port number.
    File logs keep the CLI clean.

"""


def setup_logging(name):
    _clientLogger = logging.getLogger(name)
    _clientLogger.setLevel(logging.DEBUG)
    _formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s',
                                   '%b %d,%Y %I:%M:%S %p')

    # Define a handler which writes Debug messages or higher to log files
    _file_handler = logging.handlers.RotatingFileHandler(
                    'logs/%s.log' % name, maxBytes=20*1024, backupCount=2,)
    _file_handler.setFormatter(_formatter)

    # Save logs with level debug and above in files
    _file_handler.setLevel(logging.DEBUG)
    _clientLogger.addHandler(_file_handler)


def getLogger(name):
    return logging.getLogger(name)
