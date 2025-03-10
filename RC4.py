#!/usr/bin/python3

from input_manager import inputManager, CommandError


def rc4(text:str, key:str) -> str:
    '''
    '''
    return


def main() -> None:
    '''
    Description
    -----------
     Main function that runs the `inputManager`, excepts possible misspellings, executes the algorithm and prints the output.

    Returns
    -------
     None
    '''
    try:
        text, key = inputManager()
        result = rc4(text, key)
        print(f"\n{result}\n")
    
    except CommandError:
        print('\nERROR : The command has a spelling mistake.\n')


if __name__ == "__main__":
    main()
