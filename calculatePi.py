import random

x, y = [], []
n = 1000000  # create n random points; the higher the more accurate

# for i in range(n):
#     x.append(rd.uniform(0, 1))
#     # Xi is a set of n random numbers between 0 and 1
#     y.append(rd.uniform(0, 1))
#     # Yi is a set of n random numbers between 0 and 1

# A much faster way to generate large number of random numbers
y = [random.random() for i in range(n)]
x = [random.random() for i in range(n)]


# print(x[1:5])
# print(len(y))

count_circle = 0
for i in range(n):
    m = (x[i]-0.5)*(x[i]-0.5) + (y[i]-0.5)*(y[i]-0.5)
    if m <= 0.25:
        count_circle = count_circle + 1

pi = (count_circle/n) * 4
print(pi)
