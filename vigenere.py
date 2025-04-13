#!/usr/bin/python3

from input_manager import EncryptionManager
from exceptions import KeyLengthError, KeyIsNotValidError


def vigenereEncrypt(text:str, key:str) -> str:
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
    # Key length and content checking
    keyLength = len(key)
    
    if not 1 <= keyLength <= 7:
        raise KeyLengthError
    
    if not key.isalpha():
        raise KeyIsNotValidError

    # Initialization
    textlength = len(text)
    encrypted = ""

    # Ciphering loop
    for i in range(textlength):
        charNum = (ord(text[i]) + ord(key[i % keyLength])) % 26
        encrypted += chr(charNum + ord("A"))

    assert len(encrypted) == len(text) # Check output and input for same length
    
    return encrypted


def vigenereDecrypt(text:str, key:str) -> str:
    '''
    Description
    -----------
    Implementation of the Vigenère decryption algorithm.

    Parameters
    ----------
    - `text : str` String of text to decrypt.
    - `key : str` String with the key to use in the decryption process.
    
    Returns
    -------
    - `str` Decrypted text.
    '''
    # Key length and content checking
    keyLength = len(key)
    
    if not 1 <= keyLength <= 7:
        raise KeyLengthError
    
    if not key.isalpha():
        raise KeyIsNotValidError

    # Initialization
    textlength = len(text)
    decrypted = ""

    # Deciphering loop
    for i in range(textlength):
        charNum = (ord(text[i]) - ord(key[i % keyLength])) % 26
        decrypted += chr(charNum + ord("A"))

    assert len(decrypted) == len(text) # Check output and input for same length
    
    return decrypted


if __name__ == "__main__":
    EM = EncryptionManager()
    EM.printResult({"ENCRYPT":vigenereEncrypt,
                    "DECRYPT":vigenereDecrypt},
                    "HELP_vigenere.txt")
