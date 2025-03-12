#!/usr/bin/python3

from input_manager import printResult, textPreProcesser


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
    - `str`
    '''
    # Initialization
    txt = textPreProcesser(text)
    result = ""
    
    # Actual algorithm
    for i in range(len(txt) - 1):
        result += txt[i + 1]
        result += txt[i]
    
    return result


if __name__ == "__main__":
    printResult(monoAlphabet, "HELP_mono")
