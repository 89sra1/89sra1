from timeit import timeit
from collections import deque
from assignment3 import SimpleQueue

SIZE = 0
QUEUE = None


def print_time(function):
    time = timeit(function, number=1)
    print(f"Time: {time:.7f} (SIZE: {SIZE}, {function.__name__})")


def measure(type, size):
    global SIZE
    SIZE = size
    if type == "list":
        print_time(create_list)
    elif type == "deque":
        print_time(create_deque)
    else:
        print_time(create_simple_queue)
    print_time(popleft)
    print_time(append)


def create_list():
    global QUEUE
    QUEUE = list(range(SIZE))


def create_deque():
    global QUEUE
    QUEUE = deque(range(SIZE))


def create_simple_queue():
    global QUEUE
    QUEUE = SimpleQueue(range(SIZE))


def popleft():
    try:
        while QUEUE:
            QUEUE.popleft()
    except AttributeError:
        while QUEUE:
            QUEUE.pop(0)


def append():
    for i in range(SIZE):
        QUEUE.append(i)


def main():
    measure("deque", 200000)
    measure("simple_queue", 200000)
    measure("list", 200000)
    measure("deque", 1000000)
    measure("simple_queue", 1000000)


if __name__ == "__main__":
    main()
