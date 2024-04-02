"""Establish major logger functions for individual scripts.

MainLogger is the main class containing 1 main function that provides a unique logging instance to each script.
"""

import logging # Importing log
import os, pathlib # Importing os and pathlib
from dotenv import load_dotenv # Importing load_dotenv
load_dotenv() # Loading the .env file


class CustomFormatter(logging.Formatter):

    blue = '\033[34m' # Blue
    green = '\033[92m' # Green
    grey = "\x1b[38;20m" # Grey
    yellow = "\x1b[33;20m" # Yellow
    red = "\x1b[31;20m" # Red
    bold_red = "\x1b[31;1m" # Bold Red
    reset = "\x1b[0m" # Reset
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s" # Format of the log

    FORMATS = { # Different formats for different log levels
        logging.DEBUG: blue + format + reset, 
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno) # Get the format of the log
        formatter = logging.Formatter(log_fmt) # Set the format of the log
        return formatter.format(record) # Return the formatted log

class MainLogger():
    # Logging Class

    def __init__(self):
        """Initialize class and parse config

        :param config: A relative or absolute path to master config JSON file.
        """
        #config = pathlib.Path(config)
        #config = config.resolve() # Find absolute path from a relative one.
        #f = open(config)
        #config = json.load(f)

        #for i in config['paths']:
        #    try:
        #        self.log_dir = i["log_dir"]
        #    except KeyError:
        #        pass
        #for j in config['basic_variables']i:
        #    try:
        #        self.verbose = j["verbose"]
        #    except KeyError:
        #        pass

        self.log_dir = str(os.getenv("LOGDIR")) if os.getenv("LOGDIR") != None else "logs" # Setting the log directory
        self.verbose = bool(int(os.getenv("VERBOSE"))) if os.getenv("VERBOSE") != None else True # Setting the verbose flag
        self.log_dir = pathlib.Path(self.log_dir) # Setting the log directory as a path
        self.log_dir = self.log_dir.resolve()  # Find absolute path from a relative one.
        self.log_dir = str(self.log_dir) # Setting the log directory as a string

    def StandardLogger(self, name):
        logger = logging.getLogger(name) # Creating a logger instance
        if not self.verbose: # Enable verbose depending on flag set by the config file.
            logger.setLevel(logging.WARNING)
        else:
            logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        try: # Try to create a file handler
            fh = logging.FileHandler(os.path.join(self.log_dir, 'complete.log'))
        except FileNotFoundError:
            os.makedirs(self.log_dir)
            fh = logging.FileHandler(os.path.join(self.log_dir, 'complete.log'))

        # create console handler with a higher log level
        error = logging.StreamHandler()

        error.setFormatter(CustomFormatter())

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter) # Set the formatter for the file handler
        # error.setFormatter(formatter)

        # add the handlers to the logger
        logger.addHandler(fh) # Add the file handler to the logger
        logger.addHandler(error) # Add the console handler to the logger

        logger.info(f"{name}'s LogMaster Instance Initialized Successfully ===> {os.path.join(self.log_dir, 'complete.log')}") # Log that the logger has been initialized

        return logger # Return the logger instance



