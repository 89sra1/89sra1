import sys
import time

FILENAME = "eng_vocab.txt"


def my_timer_decorator(func):
    def timed():
        time_before = time.time()
        result = func()
        time_after = time.time()
        execution_time = time_after - time_before
        print(f"execution time: {execution_time} taken")
        return result
    return timed


class MyFileContextManager():
    def __init__(self, filename, operation):
        self.filename = filename
        self.operation = operation

    def __enter__(self):
        try:
            self._file = open(self.filename, self.operation)
            return self._file
        except FileNotFoundError:
            print("No such file found in the directory")
            exit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()


def my_generator(file):
    for row in file:
        yield row


@my_timer_decorator
def read_list():
    file = open(FILENAME, "r")
    return file.read().splitlines()


@my_timer_decorator
def read_generator():
    with MyFileContextManager(FILENAME, "r") as f:
        generator = my_generator(f)
        for row in generator:
            pass
        return generator


def main():
    text_list = read_list()
    print(sys.getsizeof(text_list), "Bytes are used by the list")
    text_generator = read_generator()
    print(sys.getsizeof(text_generator), "Bytes are used by the generator")


if __name__ == "__main__":
    main()
