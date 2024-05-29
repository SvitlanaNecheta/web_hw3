import time
from multiprocessing import Pool, cpu_count
import os
 


#**************************************************
def factors(n):
        result = []
        for i in range(1, n + 1):
            if n % i == 0:
                result.append(i)
        return result



def factorize_sync(*number):
    arg=[*number]
    return [factors(num) for num in arg]
    raise NotImplementedError()


#*******synchronous**************

if __name__ == "__main__":
    start_time = time.time()
    a, b, c, d = factorize_sync(128, 255, 99999, 10651060)
    sync_duration=time.time() - start_time
    print(f"Synchronous result: {a}, {b}, {c}, {d}")
    print(f"Synchronous duration: {sync_duration} seconds")

#************************************************
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

#**********parrallel**************************
    cpu_count  = os.cpu_count()
    print("Number of CPUs in the system:", cpu_count )
    start_time = time.time()
    with Pool(cpu_count) as pool:
        a, b, c, d =pool.map(factors,(128, 255, 99999, 10651060))
    print(f"Parallel result: {a}, {b}, {c}, {d}")
    parallel_duration = time.time() - start_time
    print(f"Parallel duration: {parallel_duration} seconds")


   