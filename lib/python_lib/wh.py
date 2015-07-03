# coding:utf-8
import readline
from os import SEEK_END, linesep

def wh(filename='history.py'):
    # write the history
    readline.write_history_file(filename)

    f = open(filename, 'r+')

    # move pointer to last and back one. then get the pos num
    pos = f.seek(0, SEEK_END)
    pos -= len(linesep) + 1
    f.seek(pos)

    # if pos == -1, never mind. that's impossible
    # return 2, go 1 -> -1
    while f.read(1) != linesep:
        pos -= 2

        # move pointer above
        f.seek(pos)

    f.seek(pos + 1)
    f.truncate()

    # when find '\n', delete from there to end
    f.close()
