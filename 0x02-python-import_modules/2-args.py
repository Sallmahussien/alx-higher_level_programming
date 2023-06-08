#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    for i in range(len(sys.argv)):
        if i == 0:
            print("{} arguments".format(len(sys.argv) - 1), end="")

            if len(sys.argv) == 1:
                print(".")
                break
            else:
                print(":")
                continue

        print("{}: {}".format(i, sys.argv[i]))
