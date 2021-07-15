import base64
from pathlib import Path
import secrets
import random
import codecs
#mac
import os
#

from playsound import playsound


def play():
    #not mac
    #playsound(path_to_file.name)

    #mac
    os.system(f"afplay {path_to_file.name}")

def play_corrupt():
    #not mac
    #playsound(corrupted_child.name)

    # mac
    os.system(f"afplay {corrupted_child.name}")
WIDTH = 3
def corrupt(f: Path, num:int):
    b64 = base64.b64encode(f.read_bytes())
    bytes_len = len(b64)
    print(bytes_len)
    for x in range(num):
        addr = random.randint(10000, bytes_len - 1)
        addr2 = random.randint(addr, bytes_len - 1)
        new = b64[addr2:addr2+WIDTH]
        old = b64[addr:addr+WIDTH]
        print(f"{old} <-> {new}")
        b64 = b64[0:addr-1] + b64[addr2:addr2+WIDTH] + b64[addr+WIDTH:addr2-1] + b64[addr:addr+WIDTH] + b64[addr2+WIDTH:bytes_len-1]

    missing_padding = len(b64) % 4
    if missing_padding:
        b64 += b'='* (4 - missing_padding)

    return base64.b64decode(b64)

path_to_file = Path("./asdf.mp3")

corrupted_child = Path("./asdf-corrupt.mp3")
corrupted_child.write_bytes(path_to_file.read_bytes())
generations = 10
play()
for generation in range(generations):
    corrupted_child.write_bytes(corrupt(corrupted_child, 2*(1+generation)))
    play_corrupt()




