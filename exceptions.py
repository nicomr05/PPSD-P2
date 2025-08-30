class CommandError(Exception):
    '''
    Invalid command syntax.
    '''
    pass

class KeyMissingError(Exception):
    '''
    Key not introduced.
    '''
    pass

class KeyIsNotValidError(Exception):
    '''
    Key has a non-valid character.
    '''
    pass

class KeyLengthError(Exception):
    '''
    Invalid key length.
    '''
    pass

class NonValidCharError(Exception):
    '''
    Character not valid.
    '''
    pass
