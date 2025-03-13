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
    - `str` Encrypted text.
    '''
    # KSA
    # ---

    # Inicialization
    S = [i for i in range(256)]
    T = [ord(key[i % len(key)]) for i in range(256)]

    # Initial permutation
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j], S[i]
    
    # Keystream generation
    i, j = 0, 0
    while not True:         #! Quitar el "not" y hacer que no sea infinito
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        k = S[t]
    
    
    # PRGA
    # ----

    return text


if __name__ == "__main__":
    printResult(rc4, "HELP_rc4")
