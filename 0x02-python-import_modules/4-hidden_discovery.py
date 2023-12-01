#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    info = dir(hidden_4)
    for data in info:
        if data[:2] != "__":
            print(data)
