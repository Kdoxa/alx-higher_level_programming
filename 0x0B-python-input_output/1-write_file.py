#!/usr/bin/python3
""" function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """ function write_file(filename="", text="")
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)

        return len(text)
