x = [0, 1, 2, 3]
y = [9, 7, 7, 7]
z = [5, 7, 4, 2]


getmin = [min(i) for i in zip(x, y)]
print(getmin)

LtoD = {i[0]: (i[1], i[2]) for i in zip(x, y, z)}
print(LtoD)

# sorting nested list
nestedL = []
for i in zip(x, y, z):
    nestedL.append(list(i))
print(nestedL)

nestedL.sort(key=lambda m: (m[1], m[2]))
print(nestedL)

# sort dictionary
newDict = {k: v for k, v in sorted(LtoD.items(), key=lambda m: m[1])}
print(newDict)
