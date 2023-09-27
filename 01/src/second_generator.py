import re
import os
from io import TextIOBase


def gen(file: str or TextIOBase, words: list):
    if type(words) != list:
        raise TypeError
    if len(words) == 0:
        raise ValueError
    if any([type(word) != str for word in words]):
        raise ValueError
    if not (type(file) == str or isinstance(file, TextIOBase)):
        raise ValueError

    filename = file
    if isinstance(file, TextIOBase):
        filename = file.name
        file.close()

    if not os.path.isfile(filename):
        raise FileNotFoundError

    with open(filename, mode='r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if any([re.search(rf'\b{word.lower()}\b', line, flags=re.I)
                    for word in words]):
                yield line.replace('\n', '')
