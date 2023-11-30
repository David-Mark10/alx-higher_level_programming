#!/usr/bin/python3
for fnumb in range(0, 10):
    for snumb in range(fnumb + 1, 10):
        if fnumb == 8 and snumb == 9:
            print("{}{}".format(fnumb, snumb))
        else:
            print("{}{}".format(fnumb,snumb), end=",")
