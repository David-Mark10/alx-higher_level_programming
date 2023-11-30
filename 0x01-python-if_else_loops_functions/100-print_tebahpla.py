#!/usr/bin/python3

for i in range(ord('Z'), ord('A') - 1, -1):
    if (ord('Z') - i) % 2 == 0:
    	print(f"{(chr(i).lower())}", end="")       
    else:
        print(f"{chr(i)}", end="")
