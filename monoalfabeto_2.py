#!/usr/bin/python3

from string import ascii_lowercase
from numpy import sin, cos, exp

from input_manager import printResult
from exceptions import NonExistentFunctionError


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
    # Initialization
    alphabet = [*ascii_lowercase]
    positions = []
    encrypted = ""
    callables = {
        "sin":sin,
        "cos":cos,
        "exp":exp,
        "quad":lambda x: x**2,
        "polinomial":lambda x: x**3
    }

    if key not in callables:
        raise NonExistentFunctionError

    for i in range(len(alphabet)):
        positions.append(key(i))
    
    positions.sort()

    for char in text:
        encrypted += positions
    
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
