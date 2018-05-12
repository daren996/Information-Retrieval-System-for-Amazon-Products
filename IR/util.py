"""
Utilities
    1 Quick sort
    2 Data structure of position information
    3 Compress and Decompress program

@author: Darren
"""

import zlib


def partition(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)


class doc_position:
    def __init__(self, doc_id):
        self.doc_id = int(doc_id)  # document's id
        self.occur = 0  # the number of occurrences of this word
        self.pos = set()  # position of each occurrence

    def insert(self, p):
        self.occur += 1
        self.pos.add(p)


def compress(infile, dst, level=9):
    infile = open(infile, 'rb')
    dst = open(dst, 'wb')
    _compress = zlib.compressobj(level)
    data = infile.read(1024)
    while data:
        dst.write(_compress.compress(data))
        data = infile.read(1024)
    dst.write(_compress.flush())


def decompress(infile, dst):
    infile = open(infile, 'rb')
    dst = open(dst, 'wb')
    _decompress = zlib.decompressobj()
    data = infile.read(1024)
    while data:
        dst.write(_decompress.decompress(data))
        data = infile.read(1024)
    dst.write(_decompress.flush())
