class NonValidCharError(Exception):
    '''
    Character not valid.
    '''
    pass


class KeyLengthError(Exception):
    '''
    Invalid key length.
    '''
    pass


class CommandError(Exception):
    '''
    Invalid command syntax.
    '''
    pass


class KeyIsNotDigitError(Exception):
    '''
    Key has a non-digit character.
    '''
    pass
