#!/usr/bin/python3

from string import ascii_lowercase

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
    alphabet = [*ascii_lowercase]

    domain = alphabet[::-1] # Alphabet inversion
    codomain = ""
    encrypted = ""

    # Alphabet shuffling
    i = 1
    while i < len(domain):
        codomain += domain[i] + domain[i-1]
        i += 2
    
    # Text encryption
    for i in range(len(text)):
        print(text[i])
        print(ord(text[i]) - 97)
        encrypted += codomain[ord(text[i]) - 97]

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
    domain = ascii_lowercase[::-1] # Alphabet inversion
    codomain = ""
    decrypted = ""

    # Alphabet shuffling
    i = 1
    print(domain[1] + domain[0])
    while i < len(codomain):
        print(domain)
        codomain += domain[i] + domain[i-1]
        i += 2

    # Text decryption
    for i in range(len(text)):
        print(ord(text[i]) - 97)
        decrypted += codomain[ord(text[i]) - 97]

    assert len(decrypted) == len(text) # Check output and input for same length

    return decrypted


if __name__ == "__main__":
    printResult(monoAlphabet, "HELP_mono")
