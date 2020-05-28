x = [0, 1, 2, 3]
y = [9,7,2]

m = 'x'
print(m)
n = m.join('lkkl')
print(n)

def func(y, x=[]):
    m = x.copy()
    m.append(y)
    return m

a = func(6, x=x)

print(x+y)


