#!/usr/bin/python3

from sys import argv
from string import ascii_uppercase
from collections.abc import Callable

from exceptions import (
    CommandError,
    NonValidCharError,
    KeyLengthError,
    KeyIsNotValidError
)

class EncryptionManager:
    '''
    Description
    -----------
    Manages all the actions related with parsing the input commands, reading files and catching exceptions.

    Attributes
    ----------
    - `text : str` Text read from a *.txt* file.
    - `key : str` Key introduced in the command line.
    '''
    def __init__(self):
        '''
        Description
        -----------
        Attribute initializer for the EM.

        Returns
        -------
        `None`
        '''
        self.text: str
        self.key: str


    def readFile(self, file_name:str) -> str:
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

        return content


    def processText(self, text:str) -> str:
        '''
        Description
        -----------
        Digests text to make it suitable for encryption/decryption.

        Parameters
        ----------
        - `text : str` Text to process.

        Returns
        -------
        - `str` Processed text.
        '''
        # Initialization
        txt = text.upper().split()
        valid_chars = {*ascii_uppercase}
        processed = ""

        # Text processing
        for word in txt:
            processed += word

            for char in word:
                if char not in valid_chars:
                    raise NonValidCharError(char)

        return processed


    def manageInput(self) -> str|None:
        '''
        Description
        -----------
         Manages the input written in the command line and raises possibles errors within the command.
         If the command is followed by `--help`, `-h` or nothing, it will print the help for that algorithm.
         Else, it will either return a flag (string) depending if there was a `-d` or `--decrypt` flag introduced
         or `None` or raise a `CommandError`.

        Returns
        -------
        - `str | NoneType` If it is a string it is either the flag "ENCRYPT" or the flag "DECRYPT".
        '''
        l = len(argv)
        help_strings = {"-h", "--help"}
        decrypt_flags = {"-d", "--decrypt"}

        if l==1 or (l==2 and argv[1] in help_strings):
                return None

        elif l==3:
            self.text = self.processText(self.readFile(argv[1]))
            self.key  = argv[2].upper()

            return "ENCRYPT"

        elif l==4 and argv[1] in decrypt_flags:
            self.text = self.processText(self.readFile(argv[2]))
            self.key  = argv[3].upper()

            return "DECRYPT"

        else:
            raise CommandError


    def printResult(self, alg:dict[str,Callable], help_name:str) -> None:
        '''
        Description
        -----------
         Runs the `manageInput` function, excepts possible misspellings, executes the algorithm and prints the output.

        Parameters
        ----------
        - `alg : tuple[function]` encryption and decryption algorithms to use.
        - `help_name : str` name of the help text file for that algorithm.

        Returns
        -------
        - `NoneType`
        '''
        try:
            result = self.manageInput()

            if result is None:
                print(self.readFile(help_name))

            elif result == "ENCRYPT":
                print(alg["E"](self.text, self.key))

            elif result == "DECRYPT":
                print(alg["D"](self.text, self.key))

        except CommandError:
            print("\n \033[31m[ERROR]\033[0m Invalid command syntax.\n")

        #! Descomentar al acabar de implementar RC4:
        #except TypeError:
        #    print(f"\n \033[31m[ERROR]\033[0m There was no key introduced for the '{alg.__name__}' algorithm.\n")

        except NonValidCharError as character:
            print(f"\n \033[31m[ERROR]\033[0m '{character}' is not an accepted character.\n")

        except KeyLengthError:
            if alg.__name__ == "vigenere":
                print("\n \033[31m[ERROR]\033[0m The key must be between 1 and 7 characters long.\n")
            if alg.__name__ == "coslynomicEncryption":
                print("\n \033[31m[ERROR]\033[0m The key must be between 1 and 26 characters long.\n")
            if alg.__name__ == "rc4":
                print("\n \033[31m[ERROR]\033[0m The key must be between 1 and 255 bytes long.\n")

        except KeyIsNotValidError:
            if alg.__name__ == "rc4":
                print("\n \033[31m[ERROR]\033[0m The key must be a hex number of 512 digits (255 bytes) maximum.\n")
            else:
                print("\n \033[31m[ERROR]\033[0m The key must contain alphabetic characters only.\n")

        except AssertionError:
            print("\n \033[31m[ERROR]\033[0m The encrypted text's length does not match the original text's length.\n")

        except KeyboardInterrupt:
            print("\n\n \033[33m[CONSOLE]\033[0m Program halted.\n")


if __name__ == "__main__":
    EM = EncryptionManager()
    test_string = EM.readFile("test")
    print(test_string)
