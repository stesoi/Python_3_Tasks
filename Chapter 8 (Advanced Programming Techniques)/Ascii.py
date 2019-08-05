import string

is_ascii = lambda str: not any(map(lambda char: ord(char) >= 127, str))
is_ascii.__doc__ = """\
    >>> is_ascii("ABRACADABRA")
    True
    >>> is_ascii("АБРАКАДАБРА")
    False
    """

is_ascii_punctuation = lambda str: not any(map(lambda char: char not in string.punctuation, str))
is_ascii_punctuation.__doc__ = """\
    >>> is_ascii_punctuation("ABRACADABRA")
    False
    >>> is_ascii_punctuation(".,:;")
    True
    """

is_ascii_printable = lambda str: not any(map(lambda char: char not in string.printable, str))
is_ascii_printable.__doc__ = """\
    >>> is_ascii_printable("ABRACADABRA")
    True
    >>> is_ascii_printable("\\t\\n")
    False
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()
