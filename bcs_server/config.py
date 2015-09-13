
__doc__ = """
    This module all the config parameters for bcs serevr
"""

# Storage config
DB_FILE = 'bank.db'

# Server config
TCP_IP = '127.0.0.1'
TCP_PORT = 5010
MAX_CONNECTIONS = 2
MESSAGE_LENGTH = 1024

# Superuser account
ADMIN_NAME = 'admin'
ADMIN_EMAIL = 'admin@bcs.com'
ADMIN_PASSWORD = 'admin'

# Log config
LOG_FILENAME = 'logs/bcs_server.log'
MAX_SIZE_IN_KB = 20
NUMBER_OF_FILES = 5
