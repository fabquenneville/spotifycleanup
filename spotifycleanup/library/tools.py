#!/usr/bin/env python3
'''
    These are various tools used by spotifycleanup
'''

import sys
import configparser

def load_arguments():
    '''Get/load command parameters 

    Args:

    Returns:
        arguments: A dictionary of lists of the options passed by the user
    '''
    arguments = {
        "account"   : str()
    }

    for arg in sys.argv:
        # Confirm with the user that he selected to delete found files
        if "-account:" in arg:
            arguments["account"] = arg[9:]

    return arguments

def load_config(filepath):
    '''Get/load command parameters 

    Args:

    Returns:
        arguments: A dictionary of lists of the options passed by the user
    '''
    config = configparser.ConfigParser()
    config.read(filepath)
    return config._sections