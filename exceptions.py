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


class NonExistentFunctionError(Exception):
    '''
    Callable object required wasn't found.
    '''
    pass
