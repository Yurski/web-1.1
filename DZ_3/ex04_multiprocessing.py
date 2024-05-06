import time
import multiprocessing


def worker(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def factorize_parallel(*numbers):
    with multiprocessing.Pool() as pool:
        result = pool.map(worker, numbers)
    return result



start_time = time.time()
a, b, c, d = factorize_parallel(128, 255, 99999, 10651060)
end_time = time.time()

print("Factorized lists (parallel):")
print("128:", a)
print("255:", b)
print("99999:", c)
print("10651060:", d)
print("Execution time (s):", end_time - start_time)