import numpy as np
from pytimer import process_time


@process_time
def SumofTwo(a, b, v):
    sum = []
    for i in a:
        for j in b:
            sum.append(i+j)
    if v in sum:
        return True
    else:
        return False


@process_time
def SumofTwo_alternative(a, b, v):
    for i in a:
        for j in b:
            if v == i+j:
                return True
    else:
        return False


a, b = np.random.randint(1, 100, 2)
arr_a = list(np.random.choice(range(1, 10*a), a, False))
arr_b = list(np.random.choice(range(1, 10*b), b, False))
v = np.random.randint(0, 10*a+10*b)


print(SumofTwo(arr_a, arr_b, v))
print(SumofTwo_alternative(arr_a, arr_b, v))
