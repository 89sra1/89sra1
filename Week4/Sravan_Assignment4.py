import sys


FILENAME = "eng_vocab.txt"


def read_list():
    file = open(FILENAME, "r")
    return file.read().splitlines()


def main():
    class MyFileContextManager():
        def __init__(self, filename, operation):
            self._file = open(filename, operation)

        def __enter__(self):
            print("file is opened and fetched")
            return self._file

        def __exit__(self):
            print("closing the file")
            self._file.close()

    with MyFileContextManager("FILENAME", "r") as f:
        text = f.read()
        print("file is done with the operation given by user")
    print(sys.getsizeof(text), "Bytes are used by the list")


if __name__ == "__main__":
    main()
