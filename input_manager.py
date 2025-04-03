#!/usr/bin/python3

from sys import argv
from string import ascii_uppercase
from collections.abc import Callable

from exceptions import (
    CommandError,
    NonValidCharError,
    KeyLengthError,
    KeyIsNotValidError,
    KeyMissingError
)


class bcolors:
    ERROR = "\033[31m"
    SYSTEM = "\033[34m"
    CONSOLE = "\033[33m"
    ENDC = "\033[0m"


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
            print(f"\n {bcolors.ERROR}[ERROR]{bcolors.ENDC} File named '{file_name}' not found.")
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
        validChars = {*ascii_uppercase}
        processed = ""

        # Text processing
        for word in txt:
            for char in word:
                if char not in validChars:
                    raise NonValidCharError(char)

            processed += word

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
        helpStrings = {"-h", "--help"}
        decryptFlags = {"-d", "--decrypt"}

        if l==1 or ( argv[l-1] in helpStrings ):
                return None

        elif argv[0][2:5] == "RC4":
            self.key = argv[1]

            return "ENCRYPT"

        elif argv[0][2:5] == "RC4" and argv[1] in decryptFlags:
            self.key = argv[2]

            return "DECRYPT"

        elif argv[1] in decryptFlags and (l==2 or l==3):

            raise KeyMissingError()

        elif l==3:
            self.text = self.processText(self.readFile(argv[1]))
            self.key  = argv[2].upper()

            return "ENCRYPT"

        elif l==4 and argv[1] in decryptFlags:
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

            elif alg[result].__name__[:3] == "rc4":
                alg[result](self.key)

            else:
                print(alg[result](self.text, self.key))

        except CommandError:
            print(f"\n {bcolors.ERROR}[ERROR]{bcolors.ENDC} Invalid command syntax.\n")

        except (TypeError, KeyMissingError):
            print(f"\n {bcolors.ERROR}[ERROR]{bcolors.ENDC} There was no key introduced.\n")

        except NonValidCharError as character:
            print(f"\n {bcolors.ERROR}[ERROR]{bcolors.ENDC} '{character}' is not an accepted character.\n")

        except KeyLengthError:
            if alg[result].__name__[:8] == "vigenere":
                print(f"\n {bcolors.ERROR}[ERROR]{bcolors.ENDC} The key must be between 1 and 7 characters long.\n")
            if alg[result].__name__[:10] == "coslynomicEncryption":
                print(f"\n {bcolors.ERROR}[ERROR]{bcolors.ENDC} The key must be between 1 and 26 characters long.\n")
            if alg[result].__name__[:3] == "rc4":
                print(f"\n {bcolors.ERROR}[ERROR]{bcolors.ENDC} The key must be between 1 and 512 hex digits (255 bytes) long.\n")

        except KeyIsNotValidError:
            if alg[result].__name__[:3] == "rc4":
                print(f"\n {bcolors.ERROR}[ERROR]{bcolors.ENDC} The key must be a valid hex number (starting with '0x').\n")
            else:
                print(f"\n {bcolors.ERROR}[ERROR]{bcolors.ENDC} The key must contain alphabetic characters only.\n")

        except AssertionError:
            print(f"\n {bcolors.ERROR}[ERROR]{bcolors.ENDC} The encrypted text's length does not match the original text's length.\n")

        except KeyboardInterrupt:
            print(f"\n\n {bcolors.CONSOLE}[CONSOLE]{bcolors.ENDC} Program halted.\n")
