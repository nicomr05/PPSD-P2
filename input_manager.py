#!/usr/bin/python3

from sys import argv
from string import ascii_uppercase
from collections.abc import Callable

from exceptions import (
    CommandError,
    NonValidCharError,
    KeyLengthError,
    KeyIsNotAlphaError
)


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
        print(f"\n \033[31m[ERROR]\033[0m '{file_name}' not found.")
        return ""

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
    txt = text.upper().split()
    valid_chars = {*ascii_uppercase}
    valid_text = ""

    # Text processing
    for word in txt:
        valid_text += word

        for char in word:
            if char not in valid_chars:
                raise NonValidCharError(char)

    return valid_text


def manageInput() -> tuple[str]|None:
    '''
    Description
    -----------
     Manages the input written in the command line and raises possibles errors within the command.
     If the command is followed by `--help`, `-h` or nothing, it will print the help for that algorithm.
     Else, it will either return the text string and the key or `None` or raise a `CommandError`.

    Returns
    -------
    - `tuple | NoneType` If it is a tuple, it contains the raw text from the *.txt* file with its key.
    '''
    l = len(argv)
    help_strings = {"--help", "-h"}

    if l==1 or (l == 2 and argv[1] in help_strings):
            return None
    
    elif l == 3:
        text = processText(readFile(argv[1]))
        key = argv[2].lower()

        return (text, key)
    
    else:
        raise CommandError


def printResult(alg:Callable, help_name:str) -> None:
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
    - `NoneType`
    '''
    try:
        result = manageInput()

        if result is None:
            print(readFile(help_name))

        else:
            print(alg(*result).upper())

    except CommandError:
        print("\n \033[31m[ERROR]\033[0m Invalid command syntax.\n")

    #! Descomentar al acabar de implementar RC4:
    #except TypeError:
    #    print(f"\n \033[31m[ERROR]\033[0m There was no key introduced for the '{alg.__name__}' algorithm.\n")
    
    except NonValidCharError as character:
        print(f"\n \033[31m[ERROR]\033[0m '{character}' is not an accepted character.\n")

    except KeyLengthError:
        if alg.__name__ == "vigenere":
            print("\n \033[31m[ERROR]\033[0m The key must be between 1 and 7 characters long.\n")
        if alg.__name__ == "coslynomicEncryption":
            print("\n \033[31m[ERROR]\033[0m The key must be between 1 and 26 characters long.\n")
    
    except KeyIsNotAlphaError:
        print("\n \033[31m[ERROR]\033[0m The key must be a string of alphabetic characters.\n")

    except AssertionError:
        print("\n \033[31m[ERROR]\033[0m The encrypted text's length does not match the original text's length.\n")

    except KeyboardInterrupt:
        print("\n\n \033[33m[CONSOLE]\033[0m Program halted.\n")


if __name__ == "__main__":
    test_string = readFile("test")
    print(test_string)
