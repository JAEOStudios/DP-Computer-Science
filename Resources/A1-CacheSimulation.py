"""
Lesson A1-2: Primary Memory and the Cache
DP Computer Science, Topic A1: Computer Fundamentals

Shows what a cache actually buys you. Same workload, different hit rates.
Timings are the ones used in Q4 of your Guided Notes:
    cache access = 1 ns        RAM access = 100 ns
"""

CACHE_NS = 1
RAM_NS = 100
ACCESSES = 1_000_000


def average_access_time(hit_rate):
    """A hit costs cache time. A miss costs RAM time."""
    miss_rate = 1 - hit_rate
    return (hit_rate * CACHE_NS) + (miss_rate * RAM_NS)


print("=" * 66)
print(f"  cache = {CACHE_NS} ns per access     RAM = {RAM_NS} ns per access")
print("=" * 66)
print(f"{'hit rate':>10} | {'average access':>15} | {'time for 1M reads':>19}")
print("-" * 66)

for percent in [0, 25, 50, 75, 90, 95, 99, 100]:
    avg = average_access_time(percent / 100)
    total_ms = avg * ACCESSES / 1_000_000  # ns -> ms
    print(f"{percent:>9}% | {avg:>12.2f} ns | {total_ms:>16.2f} ms")

print("-" * 66)
print()
print("Notice the shape of that. Going from 0% to 50% saves you about half the")
print("time, which is what you'd expect. But going from 90% to 99% - only nine")
print("more percentage points - cuts the average from 10.9 ns to 1.99 ns.")
print("That is why chip designers will happily burn a third of the die area on")
print("cache: the last few percent of hit rate are worth the most.")
print()
print("The catch: bigger cache is slower cache, which is exactly why you get")
print("L1, L2 and L3 instead of one enormous one.")