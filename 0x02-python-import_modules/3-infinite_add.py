#!/usr/bin/python3

if __name__ == "__main__":
    """ The function will print of all args."""
    import sys

    ttl = 0
    for a in range(len(sys.argv) - 1):
        ttl += int(sys.argv[a + 1])
    print("{}".format(ttl))
