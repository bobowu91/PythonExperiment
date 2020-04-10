import random as rd

x, y = [], []
n = 1000000
for i in range(n):
    x.append(rd.uniform(0, 1))
    y.append(rd.uniform(0, 1))

# print(x[1:5])
# print(len(y))

count_circle = 0
for i in range(n):
    m = (x[i]-0.5)*(x[i]-0.5) + (y[i]-0.5)*(y[i]-0.5)
    if m <= 0.25:
        count_circle = count_circle + 1

pi = (count_circle/n) * 4
print(pi)
