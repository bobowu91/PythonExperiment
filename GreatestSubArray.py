import random
import time

y = random.sample(range(-1000, 1000), 100)
# print(y)


def SubarrayMax(x):  # Brute force solution
    max = 0
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            sub_sum = sum(x[i:j])
            if sub_sum > max:
                max = sub_sum
                sub = x[i:j]
    return sub


def SubarrayKad(x):  # Kadane's algorithm (optimized for run time)
    globalmax = []
    localmax = []
    for j in range(len(x)):
        if x[j] < sum(localmax) + x[j]:
            localmax.append(x[j])
        else:
            localmax = [x[j]]
        if sum(globalmax) < sum(localmax):
            globalmax = localmax.copy()
    return globalmax


t1 = time.process_time()
print(SubarrayMax(y))
t2 = time.process_time()
print(SubarrayKad(y))
t3 = time.process_time()
print((t2-t1)*10000)
print((t3-t2)*10000)
