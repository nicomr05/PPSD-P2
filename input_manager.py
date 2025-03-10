#!/usr/bin/python3

from sys import argv


class CommandError(Exception):
    '''
    Description
    -----------
     Exception class to indicate an error produced by a misspell in the command line.
    '''
    pass


def fileReader(file_name:str) -> str:
    '''
    Description
    -----------
     Searches for a .txt file with name `file_name` in the directory of `input_manager.py` and tries to read it.
    
    Parameters
    ----------
     `file_name : str`
     Name of the file from which to read.

    Returns
    -------
     `content : str`
     The content of the file as a string.
    '''
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    
    with open(file_name) as f:
        content = f.read()
    
    return content


def inputManager() -> str|tuple:
    '''
    Description
    -----------
     Manages the input written in the command line and raises possibles errors within the command.
     If the command is followed by --help

    Returns
    -------
     `str`
    '''
    l = len(argv)

    if l == 2:
        if argv[1] == "--help":
            return ()
        
        text = fileReader(argv[1])
        return tuple(text)
    
    elif l == 3:
        text = fileReader(argv[1])
        key = argv[2]

        return text, key
    
    else:
        raise CommandError



if __name__ == "__main__":
    test_string = fileReader("test")
    print(test_string)
