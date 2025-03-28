#!/usr/bin/python3

from input_manager import EncryptionManager, bcolors
from exceptions import KeyIsNotValidError, KeyLengthError


def processKey(key:str) -> list:
    '''
    Description
    -----------
    Digests the key string to make it more manageable.

    Parameters
    ----------
    - `key : str` String with the hex code for the key.
    
    Returns
    -------
    - `list` List of bytes which represent the key in the rc4 algorithm.
    '''
    # Key checking
    
    if key[0:2] != "0x":
        raise KeyIsNotValidError
    
    key = key[2:]

    hex_symbols = "0123456789abcdef"
    for i in key:
        if i not in hex_symbols:
            raise KeyIsNotValidError
    
    if not 0 < len(key[2:]) <= 512: # Limit the key between 1 and 256*2 hex digits (256 bytes)
        raise KeyLengthError

    # Key formatting

    if len(key) % 2 == 1: # Fix odd keylength
        k = "0"
        for i in key:
            k += i
        key = k

    K = [int(key[i:i+2], 16) for i in range(0, len(key), 2)]

    
    return K


def ksa(S:list, T:list):
    '''
    Description
    -----------
    'Key Schedulling Algorithm' part for the rc4 implementation.

    Parameters
    ----------
    - `key : str` String with the hex code for the key.
    
    Returns
    -------
    - `list` Current S state.
    '''
        # Initial permutation
    print(f"\n {bcolors.SYSTEM}[SYSTEM]{bcolors.ENDC} Initial S state:\n\n{S}\n")
    
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j], S[i]

    print(f"\n {bcolors.SYSTEM}[SYSTEM]{bcolors.ENDC} S after the first permutation:\n\n{S}\n")

    return S


def prga(S:list):
    '''
    Description
    -----------
    'Pseudo-Random Generation Algorithm' part for the rc4 implementation.

    Parameters
    ----------
    - `S : list` Current S-vector state.
    
    Yields
    ------
    - `int` Current keystream.
    '''
    i, j = 0, 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        k = S[t]

        yield k


def rc4Encrypt(key:str) -> None:
    '''
    Description
    -----------
    Prints the rc4-encrypted characters while you introduce them.
    
    Parameters
    ----------
    `key : str` String with the hex code for th key.

    Returns
    -------
    `None`
    '''
    key: list = processKey(key)

    S = [i for i in range(256)]
    T = [key[i % len(key)] for i in range(256)]

    # Initial permutation
    S = ksa(S,T)

    # Keystream generation
    rc4gen = prga(S)

    encrypted = ""

    while True:
        char = input(f"\n {bcolors.SYSTEM}[SYSTEM]{bcolors.ENDC} Please enter a character (Press <Enter> to halt):  ")

        if char == "":
            print(f"\n {bcolors.CONSOLE}[CONSOLE]{bcolors.ENDC} Execution ended.")
            break

        if not 0 < len(char) <= 1:
            print(f"\n {bcolors.ERROR}[ERROR]{bcolors.ENDC} Please enter a single character.")
            continue

        keystream = next(rc4gen)
        cypherchar = ord(char) ^ keystream

        encrypted += format(cypherchar, "02x")

        # Printing statements
        print(f"\n {bcolors.SYSTEM}[SYSTEM]{bcolors.ENDC} Introduced character in:\n\t• ASCII  : {ord(char)}\n\t• BINARY : {format(ord(char), '0b')}")
        print(f"\n {bcolors.SYSTEM}[SYSTEM]{bcolors.ENDC} Current S state:\n{S}\n")

        print(f"\n {bcolors.SYSTEM}[SYSTEM]{bcolors.ENDC} Current keystream in:\n\t• DECIMAL  : {keystream}\n\t• BINARY   : {format(keystream, '0b')}")
        print(f"\n {bcolors.SYSTEM}[SYSTEM]{bcolors.ENDC} Encrypted character in:\n\t• BINARY : {format(cypherchar, '0b')}\n\t• HEX    : {format(cypherchar, '0x')}")

    if encrypted == "":
        print(f"\n {bcolors.SYSTEM}[SYSTEM]{bcolors.ENDC} No text introduced.\n")
    else:
        print(f"\n {bcolors.SYSTEM}[SYSTEM]{bcolors.ENDC} Encrypted text in hexadecimal:\n\n\t{encrypted}\n")


def rc4Decrypt(text:str, key:str) -> None:
    '''
    Description
    -----------
    Prints the rc4-encrypted characters while you introduce them.
    
    Parameters
    ----------
    `key : str` String with the hex code for th key.

    Returns
    -------
    `None`
    '''
    key: list = processKey(key)

    S = [i for i in range(256)]
    T = [key[i % len(key)] for i in range(256)]

    # Initial permutation
    S = ksa(S,T)

    # Keystream generation
    rc4gen = prga(S)

    encrypted = ""

    while True:
        char = input(f"\n {bcolors.SYSTEM}[SYSTEM]{bcolors.ENDC} Please enter a character (Press <Enter> to halt):  ")

        if char == "":
            print(f"\n {bcolors.CONSOLE}[CONSOLE]{bcolors.ENDC} Program ended.\n")
            break

        if not 0 < len(char) <= 1:
            print(f"\n {bcolors.ERROR}[ERROR]{bcolors.ENDC} Please enter a single character.")
            continue

        keystream = next(rc4gen)
        cypherchar = ord(char) ^ keystream

        encrypted += format(cypherchar, "02x")

        # Printing statements
        print(f"\n {bcolors.SYSTEM}[SYSTEM]{bcolors.ENDC} Introduced character in:\n\t• ASCII  : {ord(char)}\n\t• BINARY : {format(ord(char), '0b')}")
        print(f"\n {bcolors.SYSTEM}[SYSTEM]{bcolors.ENDC} Current S state:\n{S}\n")

        print(f"\n {bcolors.SYSTEM}[SYSTEM]{bcolors.ENDC} Current keystream in:\n\t• DECIMAL  : {keystream}\n\t• BINARY   : {format(keystream, '0b')}")
        print(f"\n {bcolors.SYSTEM}[SYSTEM]{bcolors.ENDC} Encrypted character in:\n\t• BINARY : {format(cypherchar, '0b')}\n\t• HEX    : {format(cypherchar, '0x')}")

    print(f"\n {bcolors.SYSTEM}[SYSTEM]{bcolors.ENDC} Encrypted text in hexadecimal:\n\n\t{encrypted}\n")


if __name__ == "__main__":
    EM = EncryptionManager()
    EM.printResult({"ENCRYPT":rc4Encrypt,"DECRYPT":rc4Decrypt}, "HELP_rc4")
