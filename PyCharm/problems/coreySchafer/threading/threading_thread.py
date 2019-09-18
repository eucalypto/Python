import time
import threading
import concurrent.futures


def run(sleep_time):
    print(f"Sleeping for {sleep_time} seconds")
    time.sleep(sleep_time)
    print("I'm awake again!")
    return "Return This!"


def without_threads():
    run(2)
    run(2)


def with_threads():
    print(threading.current_thread().getName())
    thread1 = threading.Thread(target=run, args=[2])
    thread2 = threading.Thread(target=run, args=[2])

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


def with_more_threads():
    threads = []

    for _ in range(12):
        t = threading.Thread(target=run, args=[3])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()


def with_thread_pool():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(run, 2)
        f2 = executor.submit(run, 3)

        f1.result()
        f2.result()


def with_more_thread_pool():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(run, 2) for _ in range(10)]

        # for result in results:
        #     print(result.result())

        for f in concurrent.futures.as_completed(results):
            print(f.result())


if __name__ == '__main__':
    start = time.perf_counter()

    # without_threads()
    # with_threads()
    # with_more_threads()
    # with_thread_pool()
    with_more_thread_pool()

    finish = time.perf_counter()

    print(f"Finished in {round(finish - start, 3)} seconds")
