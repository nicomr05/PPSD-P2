#!/usr/bin/python3

from numpy import cos
from string import ascii_uppercase

from input_manager import EncryptionManager
from exceptions import KeyIsNotValidError, KeyLengthError


def formatKey(key:str) -> str:
    '''
    Description
    -----------
    Checks the key and performs a padding opperation to it.
    
    Parameters
    ----------
    `ket : str` Key string given.
    
    Returns
    -------
    `str` New formated key.
    '''
    if not key.isalpha():
        raise KeyIsNotValidError

    if not 1 <= len(key) <= 26:
        raise KeyLengthError

    i = 0
    while len(key) < 26:
        key += key[i % len(key)]
        i += 1

    return key


def coslynomic(key:str) -> list:
    '''
    Description
    -----------
    Generates the shuffled alphabet from the key given
    
    Parameters
    ----------
    `ket : str` Key string given.
    
    Returns
    -------
    `list` List with the permutated alphabet characters.
    '''
    # Key length and content checking
    key = formatKey(key)

    # Initialization
    INF = float("inf")
    shuffled = []

    coslynomial = [cos( ord(key[i]) * (27-i)**i ) for i in range(26)] # Load the cosine-polynomic function

    for _ in coslynomial:
        min_index = coslynomial.index(min(coslynomial))
        shuffled.append(min_index)
        coslynomial[min_index] = INF

    return shuffled


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
    shuffled = coslynomic(key)

    encrypted = ""
    for char in text:
        idx = ascii_uppercase.index(char)
        encrypted += chr(shuffled[idx] + ord("A"))

    assert len(encrypted) == len(text) # Check output and input for same length

    return encrypted


def coslynomicDecryption(text:str, key:str) -> str:
    '''
    Description
    -----------
    Decrypting function for our encrypting monoalphabetic subtitution algorithm, 'coslynomicEncryption'.

    Parameters
    ----------
    - `text : str` String of text to decrypt.
    - `key : str` String with the key to use for decryption.

    Returns
    -------
    - `str` Decrypted text.
    '''
    shuffled = coslynomic(key)

    decrypted = ""
    for char in text:
        idx = shuffled.index(ord(char) - ord("A"))
        decrypted += ascii_uppercase[idx]

    assert len(decrypted) == len(text) # Check output and input for same length

    return decrypted


if __name__ == "__main__":
    EM = EncryptionManager()
    EM.printResult({"ENCRYPT":coslynomicEncryption,
                    "DECRYPT":coslynomicDecryption},
                    "HELP_mono.txt")
