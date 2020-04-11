import random
import time

# x = random.sample(range(0, 100), 20)
# print(x)

n = 10000000  # create n random points; the higher the more accurate

t1 = time.process_time()
y = [random.random() for i in range(n)]
x = [random.random() for i in range(n)]
t2 = time.process_time()

print(t2 - t1)


t3 = time.process_time()
a, b = [], []
for i in range(n):
    a.append(random.uniform(0, 1))
    # Xi is a set of n random numbers between 0 and 1
    b.append(random.uniform(0, 1))
t4 = time.process_time()

print(t4 - t3)

# 0.24419700000000003
# 0.7708470000000001
