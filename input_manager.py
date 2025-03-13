#!/usr/bin/python3

from sys import argv


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


def inputManager() -> tuple:
    '''
    Description
    -----------
     Manages the input written in the command line and raises possibles errors within the command.
     If the command is followed by `--help` or nothing, it will print the help for that algorithm.
     Else, it will either return the text string (and the key if the algorithm uses one) or raise a `CommandError`.

    Returns
    -------
    - `tuple` Tuple containing either the raw text from the *.txt* file (with its key if it has one) or nothing.
    '''
    l = len(argv)

    if l == 1:
        return ()
    
    elif l == 2:
        if argv[1] == "--help" or argv[1] == "-h":
            return ()
        
        text = fileReader(argv[1])
        return tuple([text])
    
    elif l == 3:
        text = fileReader(argv[1])
        key = argv[2]

        return (text, key)
    
    else:
        raise CommandError


def textPreProcesser(text:str) -> str:
    '''
    Description
    -----------
    Digests text to make it suitable for encryption.

    Parameters
    ----------
    - `text : str` Text to process

    Returns
    -------
    `str` Processed text
    '''
    valids = set([chr(i) for i in range(ord("a"), ord("z")+1)])
    txt = text.lower().split()
    result = ""

    for word in txt:
        for char in word:
            if char not in valids:
                raise NonValidChar(f"\n \033[31mERROR:\033[0m {char} is not an accepted character.\n")

    for word in txt:
        result += word
    
    return result


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
    
        elif cypher := alg(*result) == None:
            return
        
        else:
            print(f"{cypher}")

    except CommandError:
        print("\n \033[31mERROR:\033[0m The command introduced had invalid syntax.\n")

    #! Descomentar al acabar de implementar RC4:
    #except TypeError:
    #    print(f"\n \033[31mERROR:\033[0m There was no key introduced for the '{alg.__name__}' algorithm.\n")

    except KeyboardInterrupt:
        print(f"\n\n \033[33mCONSOLE:\033[0m Program halted.\n")



if __name__ == "__main__":
    test_string = fileReader("test")
    print(test_string)
