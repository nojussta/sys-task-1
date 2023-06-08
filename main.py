import sys
import os


def main():
    print(sys.argv)
    checkArgs()


def checkArgs():
    if len(sys.argv) < 2:
        print("Reikia bent vieno argumento")
        sys.exit(1)
    else:
        for i in range(1, len(sys.argv)):
            if (os.path.isdir(sys.argv[i])):
                print("Tai yra direktorija")
                print(sys.argv[i])
            else:
                print("Tai nera direktorija, CLI priima tik direktorijas")


main()
