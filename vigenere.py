#!/usr/bin/python3

from string import ascii_uppercase

from input_manager import printResult
from exceptions import KeyLengthError


def caesar(text:str, b=3) -> str:
    '''
    Description
    -----------
    Implementation of the Caesar encryption algorithm.

    Parameters
    ----------
    - `text : str` String of text in uppercase to apply a Caesar shift.
    - `b : int` Number of positions shifted.
    
    Returns
    -------
    - `str` Shifted text.
    '''
    result = ""
    
    for char in text:
        result += chr(((ord(char) + b - ord("A")) % 26) + ord("A"))

    return result


def vigenere(text:str, key:str) -> str:
    '''
    Description
    -----------
    Implementation of the Vigenère encryption algorithm.

    Parameters
    ----------
    - `text : str` String of text to encrypt.
    - `key : str` String with the key to use in the encryption process.
    
    Returns
    -------
    - `str` Encrypted text.
    '''
    # Key length checking
    keylength = len(key)
    
    if not 1 < keylength <= 7:
        raise KeyLengthError

    # Initialization
    textlength = len(text)
    caesars = tuple([caesar(ascii_uppercase, ord(i) - ord("A")) for i in key])
    encrypted = ""
    
    # Ciphering loop
    for i in range(textlength):
        char_num = ord(text[i]) - ord("A")
        encrypted += caesars[i % keylength][char_num]

    assert len(encrypted) == len(text) # Check output and input for same length
    
    return encrypted


if __name__ == "__main__":
    printResult(vigenere, "HELP_vigenere")
