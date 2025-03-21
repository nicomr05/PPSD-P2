#!/usr/bin/python3

from numpy import cos, inf
from string import ascii_uppercase

from input_manager import printResult
from exceptions import KeyIsNotAlphaError, KeyLengthError


def coslynomicEncryption(text:str, key:str) -> str:
    '''
    Description
    -----------
    Our own encryption algorithm. It shuffles the alphabet given
    the images of the indeces by the given function, which uses the
    coefficients in the `key`. Then, it substitutes the letter of the
    `text` with that new alphabet.

    Parameters
    ----------
    - `text : str` String of text to encrypt.
    - `key : str` String with the key to use for encryption.

    Returns 
    -------
    - `str` Encrypted text.
    '''
    # Key length and content checking
    if not key.isalpha():
        raise KeyIsNotAlphaError

    if len(key) > 26:
        raise KeyLengthError
    
    if len(key) < 26:
        i = 0
        while len(key) < 26:
            key += key[i % len(key)]
            i += 1
    
    # Initialization
    shuffled = []
    encrypted = ""

    coslynomial = lambda x: list( cos([float(ord(key[i]))*x[i]**i for i in range(26)]) ) # Load the cosine-polynomic function

    values = coslynomial([i for i in range(26)]) # Compute the "coslynomial" of the array of indeces

    for _ in values:
        min_index = values.index(min(values))
        shuffled.append(min_index)
        values[min_index] = inf
    
    for char in text:
        idx = [*ascii_uppercase].index(char)
        encrypted += chr(shuffled[idx] + ord("A"))

    assert len(encrypted) == len(text) # Check output and input for same length
    
    return encrypted


def decryptCoslynomicEncryption(text:str, key:str) -> str:
    '''
    Description
    -----------
    Decrypting function for our encrypting monoalphabetic subtitution algorithm.

    Parameters
    ----------
    - `text : str` String of text to decrypt.
    - `key : str` String with the numbers which will represent the
                  coefficients of the function.

    Returns
    -------
    - `str` Decrypted text.
    '''
    # Key length and content checking
    if not key.isalpha():
        raise KeyIsNotAlphaError

    if len(key) > 26:
        raise KeyLengthError
    
    if len(key) < 26:
        i = 0
        while len(key) < 26:
            key += key[i % len(key)]
            i += 1
    
    # Initialization
    shuffled = []
    encrypted = ""

    coslynomial = lambda x: list( cos([float(ord(key[i]))*x[i]**i for i in range(26)]) ) # Load the cosine-polynomic function

    values = coslynomial([i for i in range(26)]) # Compute the "coslynomial" of the array of indeces

    for _ in values:
        min_index = values.index(min(values))
        shuffled.append(min_index)
        values[min_index] = inf
    
    for char in text:
        idx = [*ascii_uppercase].index(char)
        encrypted += chr(shuffled[idx] + ord("A"))

    assert len(encrypted) == len(text) # Check output and input for same length
    
    return encrypted


if __name__ == "__main__":
    printResult(coslynomicEncryption, "HELP_mono")
