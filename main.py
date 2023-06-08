import sys
import os


def main():
    print(sys.argv)
    checkArgs()


def checkArgs():
    if len(sys.argv) < 2:
        print("Reikia bent vieno argumento")
        sys.exit(1)

main()
