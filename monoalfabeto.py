#!/usr/bin/python3

from numpy import cos
from string import ascii_uppercase

from input_manager import EncryptionManager
from exceptions import KeyIsNotValidError, KeyLengthError


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
        raise KeyIsNotValidError

    if len(key) > 26:
        raise KeyLengthError
    
    if len(key) < 26:
        i = 0
        while len(key) < 26:
            key += key[i % len(key)]
            i += 1
    
    # Initialization
    INF = float("inf")
    shuffled = []
    encrypted = ""

    coslynomial = lambda x: list( cos([float(ord(key[i]))*x[i]**i for i in range(26)]) ) # Load the cosine-polynomic function

    values = coslynomial([i for i in range(26)]) # Compute the "coslynomial" of the array of indeces

    for _ in values:
        min_index = values.index(min(values))
        shuffled.append(min_index)
        values[min_index] = float("inf")
    
    for char in text:
        idx = [*ascii_uppercase].index(char)
        encrypted += chr(shuffled[idx] + ord("A"))

    assert len(encrypted) == len(text) # Check output and input for same length
    
    return encrypted


def coslynomicDecryption(text:str, key:str) -> str:
    '''
    Description
    -----------
    Decrypting function for our encrypting monoalphabetic subtitution algorithm.

    Parameters
    ----------
    - `text : str` String of text to decrypt.
    - `key : str` String with the key to use for encryption.

    Returns
    -------
    - `str` Decrypted text.
    '''
    # Key length and content checking
    if not key.isalpha():
        raise KeyIsNotValidError

    if len(key) > 26:
        raise KeyLengthError
    
    if len(key) < 26:
        i = 0
        while len(key) < 26:
            key += key[i % len(key)]
            i += 1
    
    # Initialization
    INF = float("inf")
    shuffled = []
    decrypted = ""

    coslynomial = lambda x: list( cos([float(ord(key[i]))*x[i]**i for i in range(26)]) ) # Load the cosine-polynomic function

    values = coslynomial([i for i in range(26)]) # Compute the "coslynomial" of the array of indeces

    for _ in values:
        min_index = values.index(min(values))
        shuffled.append(min_index)
        values[min_index] = float("inf")
    
    for char in text:
        idx = shuffled.index(ord(char) - ord("A"))
        decrypted += ascii_uppercase[idx]
    
    assert len(decrypted) == len(text) # Check output and input for same length
    
    return decrypted


if __name__ == "__main__":
    EM = EncryptionManager()
    EM.printResult({"ENCRYPT":coslynomicEncryption, "DECRYPT":coslynomicDecryption}, "HELP_mono")
