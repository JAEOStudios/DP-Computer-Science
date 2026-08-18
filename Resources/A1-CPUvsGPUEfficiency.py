import numpy as np
import time

N = 10_000_000
#initializes list full of numbers from 1 to 10,000,000
data = list(range(N))

#cpu style, one thing at a time
#multiplies every item in the original list one by one using a for loop (note the for keyword)
start = time.time()
result_serial = []
for x in data:
    result_serial.append(x * 2)
print(f"Serial (CPU-style): {time.time() - start:.3f} sec")

#gpu style, applies the multiplication to every item at once
arr = np.array(data)
start = time.time()
result_parallel = arr * 2
print(f"Vectorized (GPU-style): {time.time() - start:.3f} sec")