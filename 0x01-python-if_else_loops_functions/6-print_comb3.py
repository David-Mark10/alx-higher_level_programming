#!/usr/bin/python3
for fnum in range(0, 10):
    for snum in range(fnum + 1, 10):
        if fnum == 8 and snum == 9:
            print(f"{fnum}{snum}")
        else:
            print(f"{fnum}{snum}", end=",")
