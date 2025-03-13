#!/usr/bin/python3

from string import ascii_lowercase

from input_manager import printResult


def caesar(text:str, b=3) -> str:
    '''
    Description
    -----------
    Implementation of the Caesar encryption algorithm.

    Parameters
    ----------
    - `text : str` String of text in lowercase to apply a Caesar shift.
    - `b : int` Number of positions shifted.
    
    Returns
    -------
    - `str` Shifted text.
    '''
    result = ""
    
    for char in text:
        result += chr(((ord(char) + b - 97) % 26) + 97)

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
    # Initialization
    keylength = len(key)
    textlength = len(text)
    caesars = tuple([caesar(ascii_lowercase, ord(i)-97) for i in key])
    encrypted = ""
    
    assert 0 < keylength <= 7

    # Ciphering loop
    for i in range(textlength):
        char_num = ord(text[i]) - 97
        encrypted += caesars[i % keylength][char_num]

    return encrypted


if __name__ == "__main__":
    printResult(vigenere, "HELP_vigenere")
