#!/usr/bin/python3

from sys import argv
from string import ascii_lowercase


class NonValidChar(Exception):
    '''
    Description
    -----------
     Exception class for a non-valid character in a text given.
    '''
    pass


class CommandError(Exception):
    '''
    Description
    -----------
     Exception class to indicate an error in the command introduced.
    '''
    pass


def readFile(file_name:str) -> str:
    '''
    Description
    -----------
     Searches for a text file with name `file_name` in the directory of `input_manager.py` and tries to read it.
    
    Parameters
    ----------
    - `file_name : str` Name of the file from which to read.

    Returns
    -------
    - `str` Raw text from the *.txt* file.
    '''
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    try:
        with open(file_name) as f:
            content = f.read()

    except FileNotFoundError:
        print(f"\n \033[31mERROR:\033[0m '{file_name}' not found.\n")
        return

    return content


def processText(text:str) -> str:
    '''
    Description
    -----------
    Digests text to make it suitable for encryption.

    Parameters
    ----------
    - `text : str` Text to process.

    Returns
    -------
    - `str` Processed text.
    '''
    # Initialization
    txt = text.lower().split()
    valid_chars = {*ascii_lowercase}
    valid_text = ""

    # Text processing
    for word in txt:
        valid_text += word

        for char in word:
            if char not in valid_chars:
                raise NonValidChar(char)

    return valid_text


def manageInput() -> tuple:
    '''
    Description
    -----------
     Manages the input written in the command line and raises possibles errors within the command.
     If the command is followed by `--help` or nothing, it will print the help for that algorithm.
     Else, it will either return the text string (and the key if the algorithm uses one) or raise a `CommandError`.

    Returns
    -------
    - `tuple` Contains either the raw text from the *.txt* file (with its key if it has one) or nothing.
    '''
    l = len(argv)

    if l == 1:
        return ()
    
    elif l == 2:
        if argv[1] == "--help" or argv[1] == "-h":
            return ()
        
        text = processText(readFile(argv[1]))
        return tuple([text])
    
    elif l == 3:
        text = processText(readFile(argv[1]))
        key = argv[2]

        return (text, key)
    
    else:
        raise CommandError


def printResult(alg, help_name:str) -> None:
    '''
    Description
    -----------
     Runs the `manageInput` function, excepts possible misspellings, executes the algorithm and prints the output.

    Parameters
    ----------
    - `alg : function` encryption algorithm to use.
    - `help_name : str` name of the help text file for that algorithm.
     
    Returns
    -------
    - `None`
    '''
    try:
        result = manageInput()
        ciphered = alg(*result)

        if not result:
            print(readFile(help_name))

        elif ciphered == None:
            return

        else:
            print(f"{ciphered}")

    except CommandError:
        print("\n \033[31mERROR:\033[0m Invalid command syntax.\n")

    #! Descomentar al acabar de implementar RC4:
    #except TypeError:
    #    print(f"\n \033[31mERROR:\033[0m There was no key introduced for the '{alg.__name__}' algorithm.\n")
    
    except NonValidChar as character:
        print(f"\n \033[31mERROR:\033[0m {character} is not an accepted character.\n")

    except AssertionError:
        print(f"\n \033[31mERROR:\033[0m The key must be between 1 and 7 characters long.\n")

    except KeyboardInterrupt:
        print(f"\n\n \033[33mCONSOLE:\033[0m Program halted.\n")



if __name__ == "__main__":
    test_string = readFile("test")
    print(test_string)
