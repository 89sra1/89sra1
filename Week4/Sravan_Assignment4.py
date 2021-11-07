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

        def __exit__(self, exc_type, exc_val, exc_tb):
            print("closing the file")
            self._file.close()

    try:
        with MyFileContextManager("eng_vocab.txt", "r") as f:
            text = f.read()
            print("final operation before close")
        print(sys.getsizeof(text), "Bytes are used by the list")
    except FileNotFoundError:
        print("No such file found in the directory")


if __name__ == "__main__":
    main()
