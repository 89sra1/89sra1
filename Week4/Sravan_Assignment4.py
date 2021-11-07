import sys


FILENAME = "eng_vocab.txt"


def read_list():
    file = open(FILENAME, "r")
    return file.read().splitlines()


def main():
    try:
        text_list = read_list()
        print(sys.getsizeof(text_list), "Bytes are used by the list")
    except Exception:
        print("something is wrong")


if __name__ == "__main__":
    main()
