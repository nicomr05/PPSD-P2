#!/usr/bin/python3

from input_manager import inputManager, CommandError


def monoAlphabet(text:str) -> tuple[str]:
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
        result = monoAlphabet(text) # TODO : Meter la función main() en input_manager y pasarle la función como parámetro, que sino es una chapuza.
        print(f"\n{result}\n")
    
    except CommandError:
        print('\nERROR : The command has a spelling mistake.\n')


if __name__ == "__main__":
    main()
