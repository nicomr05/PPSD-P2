#!/usr/bin/python3

from sys import argv

ORDEDED_ES = [
    "E", "A", "O", "S", "N", "R", "I", "L", "D", "T", "U", "C", "M",
    "P", "B", "H", "Q", "Y", "V", "G", "F", "J", "Z", "X", "K", "W"
]

def readFile(file_name:str) -> str:
    '''
    Description
    -----------
     Searches for a text file with name `file_name` in the directory of `input_manager.py` and tries to read it.
    Parameters
    ----------
    - `file_name : str` Name of the file from which to read.
    Returns
    -------
    - `str` Raw text from the *.txt* file.
    '''
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    try:
        with open(file_name) as f:
            content = f.read()

    except FileNotFoundError:
        print(f"\n \033[31m[ERROR]\033[0m File named '{file_name}' not found.")
        return ""

    return content.upper()


def substitute(text:str, cypher:list, precission=26):
    decrypted = ""

    for i in text:
        if i == "\n":
            break

        if cypher.index(i) < precission:
            decrypted += ORDEDED_ES[cypher.index(i)]
        else:
            decrypted += "_"

    return decrypted


def cypherBreaker() -> dict:
    text = readFile(argv[1])[:-1]
    distribution = []
    cypher = []
    
    for i in range(26):
        letter = chr(i + ord("A"))
        distribution.append( (letter, text.count(letter)/len(text)) )

    probabilities = sorted(distribution, key=lambda x: x[1], reverse=True)

    for element in probabilities:
        print(f"{element[0]} : {element[1]*100:.10f} %")
    print()

    for tup in probabilities:
        cypher.append(tup[0])

    if len(argv) == 3:
        cracked = substitute(text, cypher, int(argv[2]))
    else:
        cracked = substitute(text, cypher)

    assert len(text) == len(cracked)

    return cracked


if __name__ == "__main__":
    print(f"{cypherBreaker()}\n")
