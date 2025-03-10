#!/usr/bin/python3

from input_manager import fileReader, inputManager, CommandError


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
        text = inputManager()

        if len(text) == 0:
            print(fileReader("HELP_rc4"))
        else:
            print(f"\n{rc4(text)}\n")

    except CommandError:
        print('\nERROR : The command introduced has a spelling mistake.\n')


if __name__ == "__main__":
    main()
