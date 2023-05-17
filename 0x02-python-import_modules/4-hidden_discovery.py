#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    mydirs = dir(hidden_4)
    for mydir in mydirs:
        if mydir[:2] != "__":
            print("{:s}".format(mydir))
