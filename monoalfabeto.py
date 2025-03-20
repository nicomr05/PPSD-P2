#!/usr/bin/python3

from numpy import sin, cos, exp, log, log2, log10, sqrt, divide, power, Inf

from input_manager import printResult
from exceptions import NonExistentFunctionError


global FUNCS
FUNCS = {
    "sin":      sin,
    "cos":      cos,
    "inv":      lambda x: sin(divide(1,x)),
    "log":      lambda x: cos(10*log(x)),
    "log2":     lambda x: sin(10*log2(x)),
    "log10":    lambda x: cos(10*log10(x)),
    "sqrt":     lambda x: sin(x*sqrt(x)),
    "x^2":      lambda x: cos(power(x,2)),
    "x^3":      lambda x: sin(power(x,3)),
    "x^4":      lambda x: cos(power(x,4)),
    "exp":      lambda x: sin(exp(x))
}


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
    # Function availability checking
    if key not in FUNCS.keys():
        raise NonExistentFunctionError
    
    # Initialization
    shuffled = []
    encrypted = ""
    
    values = list(FUNCS[key](range(1,27))) # Function values from x=1 to x=26 (to avoid problems with 0 division and so on)
    
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
    if key not in FUNCS.keys():
        raise NonExistentFunctionError
    
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
