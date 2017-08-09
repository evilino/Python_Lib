# coding=utf-8

import mmap

with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

with open("hello.txt", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    print(mm.readline())
    print(mm[:5])
    mm[6:] = b" world!\n"
    mm.seek(0)
    print(mm.readline())
    mm.close()
