#!/usr/bin/python3

from numpy import cos, Inf

from input_manager import printResult
from exceptions import KeyIsNotDigitError



def monoAlphabet(text:str, key:str) -> str:
    '''
    Description
    -----------
    Our own encryption algorithm. It shuffles the alphabet given
    the images of the indeces by the given `key` function. Then, it
    substitutes the letter of the `text` with that new alphabet.

    Parameters
    ----------
    - `text : str` String of text to encrypt.
    - `key : str` String with the name of the mathematical function to use.

    Returns
    -------
    - `str` Encrypted text.
    '''
    # Key length and content checking
    if not key.isdigit():
        raise KeyIsNotDigitError
    
    keylength = len(key)

    if keylength < 26:
        i = 0
        while keylength < 26:
            key += key[i % keylength]
            i += 1
    
    # Initialization
    shuffled = []
    encrypted = ""
    
    coslynomial = lambda x: list( cos([float(key[i])*x[i]**i for i in range(keylength)]) ) # Compute the cos() of the polynomyal vector
    values = coslynomial([i for i in range(26)])
    
    for _ in values:
        min_index = values.index(min(values))
        shuffled.append(min_index)
        values[min_index] = Inf
    
    for i in range(len(text)):
        encrypted += chr(shuffled[ord(text[i]) - 97] + 97)
    
    assert len(encrypted) == len(text) # Check output and input for same length
    
    return encrypted


def decryptMonoAlphabet(text:str, key:str, ) -> str:
    '''
    Description
    -----------
    Decrypting function for our encrypting monoalphabetic subtitution algorithm.

    Parameters
    ----------
    - `text : str` String of text to decrypt.
    - `key : str` String with the name of the mathematical function used.

    Returns
    -------
    - `str` Decrypted text.
    '''
    # Key length and content checking
    if not key.isdigit():
        raise KeyIsNotDigitError
    
    if len(key) < 26:
        i = 0
        while len(key) < 26:
            key += key[i % len(key)]
            i += 1
    
    # Initialization
    shuffled = []
    decrypted = ""
    
    values = list(FUNCS[key](range(1,27))) # Function values from x=1 to x=26 (to avoid problems with 0 division and so on)
    
    for _ in values:
        min_index = values.index(min(values))
        shuffled.append(min_index)
        values[min_index] = Inf
    
    for i in range(len(text)):      # TODO : Mirar para invertir la dirección en la que se cogen los indices para desencriptar
        decrypted += chr(shuffled[ord(text[i]) - 97] + 97)
    
    assert len(decrypted) == len(text) # Check output and input for same length
    
    return decrypted


if __name__ == "__main__":
    printResult(monoAlphabet, "HELP_mono")
