import numpy as np
from pytimer import process_time


@process_time
def firstDuplicate(array):  #
    freq_dict = dict()
    for num in set(array):
        freq_dict[num] = array.count(num)

    min = len(array)
    fd = -1
    for k, v in freq_dict.items():
        if v >= 2:
            fp = array.index(k)
            sp = array.index(k, fp+1)
            if min > sp:
                min = sp  # update the new min value
                fd = k  # update the first duplicate value
    return fd


@process_time
def firstDuplicate_alternative(array):
    freq_dict = dict()
    for num in set(array):
        freq_dict[num] = array.count(num)

    firstDuplicate = dict()
    for k, v in freq_dict.items():
        if v >= 2:
            fp = array.index(k)
            firstDuplicate[k] = array.index(k, fp+1)

    fd = [k for k, v in sorted(firstDuplicate.items(), key=lambda m: m[1])]
    if not fd:
        return -1
    else:
        return fd[0]


@process_time
def fast_FD(array):
    for index, num in enumerate(array):
        subarrary = array[0:index]
        if num in subarrary:
            return num
    return -1


array = np.random.randint(1, 2000, 3000)
array = list(array)
# array = [1, 2, 3, 4, 5]
x = firstDuplicate(array)
y = firstDuplicate_alternative(array)
z = fast_FD(array)
print(x, y, z)
