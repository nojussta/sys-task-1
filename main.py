import sys
import os
import stat


def main():
    print(sys.argv)
    checkArgs()
    chosenBiggest = biggestFiles()
    print("1 Didziausias failas: {0}\nFailo dydis: {1}KB".format(
        chosenBiggest[0], chosenBiggest[1]))
    print("2 Didziausias failas: {0}\nFailo dydis: {1}KB".format(
        chosenBiggest[2], chosenBiggest[3]))


def checkArgs():
    if len(sys.argv) < 2:
        print("Reikia bent vieno argumento")
        sys.exit(1)
    else:
        for i in range(1, len(sys.argv)):
            if (os.path.isdir(sys.argv[i])):
                print("Tai yra direktorija")
                print(sys.argv[i] + '\n')
            else:
                print("Tai nera direktorija, CLI priima tik direktorijas")


def biggestFiles():
    directories = sys.argv[1:]
    numDirectories = len(directories)

    largestFile1 = ""
    largestFile2 = ""
    largestSize1 = 0
    largestSize2 = 0

    for i in range(numDirectories):
        directory = directories[i]

        try:
            entries = os.scandir(directory)
        except OSError as e:
            print("Nepavyko atidaryti direktorijos:", e)
            sys.exit(1)

        for entry in entries:
            if entry.name == "." or entry.name == "..":
                continue

            filePath = os.path.join(directory, entry.name)

            try:
                fileStat = os.stat(filePath)
            except OSError as e:
                print("Nepavyko nuskaityti informacijos:", e)
                sys.exit(1)

            if stat.S_ISREG(fileStat.st_mode):
                fileSize = fileStat.st_size

                if fileSize > largestSize1:
                    largestSize2 = largestSize1
                    largestFile2 = largestFile1
                    largestSize1 = fileSize
                    largestFile1 = entry.name
                elif fileSize > largestSize2:
                    largestSize2 = fileSize
                    largestFile2 = entry.name

    return largestFile1, largestSize1, largestFile2, largestSize2


main()
