#!/usr/bin/python3

from input_manager import printResult


def ksa(S:list, T:list, key:str) -> list:
    '''
    '''
    # Initial permutation
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j], S[i]
    
    # Keystream generation
    i, j = 0, 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        k = S[t]    

    return NotImplemented


def prga(S:list) -> list:
    '''
    '''
    return

def rc4Encrypt(key:str, text:str) -> str:
    S = ksa(key)
    keystream_generator = prga(S)
    
    ciphertext = ""
    for char, keystream_byte in zip(text, keystream_generator):
        ciphertext += chr(ord(char) ^ keystream_byte)
        
    assert len(ciphertext) == len(text) # Check output and input for same length
    
    return ciphertext


def rc4(text:str, key:str) -> str:
    '''
    Description
    -----------
    Implementation of the RC4 encryption algorithm.

    Parameters
    ----------
    - `text : str` String of text to encrypt.
    - `key : str` String with the hex code for the key.
    
    Returns
    -------
    - `str` Encrypted text.
    '''
    # Initialization
    key = int(key, 16)
    S = [i for i in range(256)]
    T = [key[i % len(key)] for i in range(256)]    

    # Main part
    forward = ksa(S, T, key)
    encrypted = prga(*forward)

    assert len(encrypted) == len(text) # Check output and input for same length
    
    return text


if __name__ == "__main__":
    printResult(rc4, "HELP_rc4")
