#!/usr/bin/python3

from input_manager import printResult


def rc4(text:str, key:str) -> str:
    '''
    Description
    -----------
    Implementation of the RC4 encryption algorithm.

    Parameters
    ----------
    - `text : str` String of text to encrypt.
    - `key : str` String with the key to use in the encryption process.
    
    Returns
    -------
    - `str`
    '''
    result = "TEST"
    return result


if __name__ == "__main__":
    printResult(rc4, "HELP_rc4")
