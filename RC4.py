#!/usr/bin/python3

from input_manager import EncryptionManager
from exceptions import KeyIsNotValidError, KeyLengthError


def rc4(key:str):
    '''
    Description
    -----------
    Implementation of the RC4 encryption algorithm until the actual encryption phase.

    Parameters
    ----------
    - `text : str` String of text to encrypt.
    - `key : str` String with the hex code for the key.
    
    Yields
    ------
    - `int` Current keystream.
    '''
    if (key[0:2] != "0x") or (not key[2:].isdigit()):
        raise KeyIsNotValidError
    
    if 0 < len(key[2:]) <= 512: # Limit the key between 1 and 256*2 bytes
        raise KeyLengthError

    # Initialization
    key = key[2:]
    K = []
    for i in range(0, len(key), 2):
        K.append(K[i:i+2])

    S = [i for i in range(256)]
    T = [K[i % len(K)] for i in range(256)]

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

        print(f"Keystream actual : {k}")
        yield k


def rc4Encrypt(text:str, key:str) -> str:
    '''
    Description
    -----------
    Encryption part of the rc4 algorithm.
    
    Parameters
    ----------
    `text : str` Text to encrypt.
    `key : str` String with the hex code for th key.

    Returns
    -------
    `str` Encrypted text.
    '''
    encrypted = ""
    for char, keystream_byte in zip(text, rc4(key)):
        encrypted += chr(ord(char) ^ keystream_byte)

    assert len(encrypted) == len(text) # Check output and input for same length
    
    return encrypted


def rc4Decrypt(text:str, key:str) -> str:
    '''
    Description
    -----------
    Decryption part of the rc4 algorithm.
    
    Parameters
    ----------
    `text : str` Text to decrypt.
    `key : str` String with the hex code for th key.

    Returns
    -------
    `str` Decrypted text.
    '''
    decrypted = ""
    for char, keystream_byte in zip(text, rc4(key)):
        encrypted += chr(ord(char) ^ keystream_byte)
    
    assert len(decrypted) == len(text) # Check output and input for same length

    return decrypted


if __name__ == "__main__":
    EM = EncryptionManager()
    EM.printResult({"E":rc4Encrypt,"D":rc4Decrypt}, "HELP_rc4")
