#!/usr/bin/python3

from input_manager import printResult


def monoAlphabet(text:str) -> str:
    '''
    Description
    -----------
    Implementation of our own encryption algorithm.

    Parameters
    ----------
    - `text : str` String of text to encrypt.

    Returns
    -------
    - `str` Encrypted text.
    '''
    return text


if __name__ == "__main__":
    printResult(monoAlphabet, "HELP_mono")
