import time
from ex02_factorize import factorize_sync 

start_time = time.time()
a, b, c, d = factorize_sync(128, 255, 99999, 10651060)
end_time = time.time()

print("Factorized lists:")
print("128:", a)
print("255:", b)
print("99999:", c)
print("10651060:", d)
print("Execution time (s):", end_time - start_time)
