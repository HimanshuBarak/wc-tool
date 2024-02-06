import os


def count_words(file):
    file.seek(0) 
    return sum(len(line.split()) for line in file)


def count_lines(file):
    file.seek(0)
    return sum(1 for line in file)  


def count_bytes(file):
    file.seek(0, os.SEEK_END)
    return file.tell()

def count_characters(file):
    """
    they are basically same as bytes
    """
    return count_bytes(file)