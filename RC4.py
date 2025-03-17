#!/usr/bin/python3

from input_manager import printResult

T = [ord(key[i % len(key)]) for i in range(256)] 

def ksa(key: str) -> list:
    S = [i for i in range(256)]
    j = 0
    
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    
    return S

def prga(S: list):
    i, j = 0, 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        yield S[(S[i] + S[j]) % 256]
        
def rc4_encrypt(key: str, text: str) -> str:
    S = ksa(key)
    keystream_generator = prga(S)
    
    ciphertext = ""
    for char, keystream_byte in zip(text, keystream_generator):
        ciphertext += chr(ord(char) ^ keystream_byte)
        
    assert len(ciphertext) == len (text), "Error: la longitud del texto cifrado no coincide con la del texto descifrado"
    
    return ciphertext
    
    
    
def rc4_decrypt(key: str, ciphertext: str) -> str:
    


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
