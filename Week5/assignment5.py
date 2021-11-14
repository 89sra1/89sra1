import queue
import time
import threading
from urllib.request import urlopen, Request
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

# Header with user agent is needed to allow access for scraping
HEADER = {'User-Agent': 'Mozilla/5.0'}
URLS = ['https://www.volvocars.com/se',
        # 'https://consid.se/',
        # 'https://stackoverflow.com/',
        'https://www.google.com/',
        'https://9gag.com/',
        'https://www.yahoo.com',
        'https://www.reddit.com',
        'https://www.youtube.com',
        'https://9gag.com/',
        'https://twitter.com/',
        'https://www.volvocars.com/se',
        # 'https://consid.se/',
        'https://www.reddit.com',
        'https://www.youtube.com',
        # 'https://stackoverflow.com',
        'https://www.aftonbladet.se/',
        'https://www.volvocars.com/se',
        'https://www.aftonbladet.se/',
        'https://www.volvocars.com/se',
        'https://www.yahoo.com',
        # 'https://consid.se/',
        'https://www.youtube.com',
        'https://9gag.com/',
        # 'https://stackoverflow.com/',
        'https://www.volvocars.com/se',
        'https://www.reddit.com/',
        # 'https://consid.se/',
        'https://9gag.com/',
        'https://twitter.com/',
        # 'https://stackoverflow.com/',
        'https://www.aftonbladet.se/',
        'https://twitter.com/']


def timer(func):
    def timer_wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        exec_time = end - start
        print(f"Execution time: {(exec_time):.7f} seconds ({func.__name__})")
        return exec_time

    return timer_wrapper


def request_and_open(URL):
    request = Request(URL, headers=HEADER)
    url_info_byte = urlopen(request, timeout=20).read()
    url_info_string = url_info_byte.decode("utf-8")
    return url_info_string


@timer
def request_single():
    for url in URLS:
        request_and_open(url)


@timer
def request_pool(num_threads):
    request_pool_list = []
    with ThreadPoolExecutor() as ex:
        for url in URLS:
            request_pool_list.append(ex.submit(request_and_open(url)))
            num_threads = request_pool_list
            result = ex.map(request_and_open, range(len(URLS)))
        print(result)
        return num_threads


@timer
def request_queue(num_threads):
    q = queue.Queue()

    def worker():
        while True:
            urls = q.get()
            request_and_open(urls)
            q.task_done()

    threading.Thread(target=worker, daemon=True).start()
    for url in URLS:
        q.put(url)
    q.join()
    print("everything is done")


def main():
    num_threads = [2, 4, 8, 16, 32, 8192]
    num_iterations = 3
    mean_times_pool = []
    mean_times_queue = []

    print(f"Number of threads: 1. Executing...")
    total_time_single = sum(request_single() for _ in range(num_iterations))
    mean_time_single = total_time_single / num_iterations

    for i in num_threads:
        print(f"Number of threads: {i}. Executing...")
        total_time_pool = sum(request_pool(i) for _ in range(num_iterations))
        total_time_queue = sum(request_queue(i) for _ in range(num_iterations))
        mean_times_pool.append(total_time_pool / num_iterations)
        mean_times_queue.append(total_time_queue / num_iterations)

    print(f"The mean time using single thread: {mean_time_single}")
    print(f"The mean times using thread pool executor are: {mean_times_pool}")
    print(f"The mean times using queue.Queue workers are: {mean_times_queue}")


if __name__ == "__main__":
    main()
