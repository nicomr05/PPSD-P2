#!/usr/bin/python3

from sys import argv


class CommandError(Exception):
    '''
    Description
    -----------
     Exception class to indicate an error in the command introduced.
    '''
    pass


def fileReader(file_name:str) -> str:
    '''
    Description
    -----------
     Searches for a text file with name `file_name` in the directory of `input_manager.py` and tries to read it.
    
    Parameters
    ----------
    - `file_name : str` Name of the file from which to read.

    Returns
    -------
    - `str`
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
     If the command is followed by `--help` or nothing, it will print the help for that algorithm.
     Else, it will either return the text string (and the key if the algorithm uses one) or raise a `CommandError`.

    Returns
    -------
    - `str`
    '''
    l = len(argv)

    if l == 1:
        return ()
    
    elif l == 2:
        if argv[1] == "--help":
            return ()
        
        text = fileReader(argv[1])
        return tuple([text])
    
    elif l == 3:
        text = fileReader(argv[1])
        key = argv[2]

        return text, key
    
    else:
        raise CommandError


def textProcesser(text:str) -> str:
    '''
    Description
    -----------
    Processes text to make it suitable for encrypting.

    Parameters
    ----------
    - `text : str` Text to process

    Returns
    -------
    `str`
    '''
    # TODO : Implementar esta función para poder usarla dentro de los algoritmos.
    valids = [chr(i) for i in range(ord("a"), ord("z")+1)] 

    return valids


def printResult(alg, help_name:str) -> None:
    '''
    Description
    -----------
     Runs the `inputManager` function, excepts possible misspellings, executes the algorithm and prints the output.

    Parameters
    ----------
    - `alg : function` encryption algorithm to use.
    - `help_name : str` name of the help text file for that algorithm.
     
    Returns
    -------
    - `None`
    '''
    try:
        result = inputManager()

        if not result:
            print(fileReader(help_name))
        else:
            print(f"\n{alg(*result)}\n")

    except CommandError:
        print('\nERROR : The command introduced has a spelling mistake.\n')



if __name__ == "__main__":
    test_string = fileReader("test")
    print(test_string)
