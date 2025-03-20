#!/usr/bin/python3

from string import ascii_lowercase

from input_manager import printResult


def monoAlphabet(text:str, key:str) -> str:
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
    alphabet = [*ascii_lowercase]
    
    for char in text:
        char
    
    encrypted = text
    assert len(encrypted) == len(text) # Check output and input for same length

    return encrypted


def decryptMonoAlphabet(text:str) -> str:
    '''
    Description
    -----------
    Decrypting function for our monoalphabet sustitution algorithm.

    Parameters
    ----------
    - `text : str` String of text to decrypt.

    Returns
    -------
    - `str` Decrypted text.
    '''
    decrypted = text
    assert len(decrypted) == len(text) # Check output and input for same length

    return decrypted


if __name__ == "__main__":
    printResult(monoAlphabet, "HELP_mono")
