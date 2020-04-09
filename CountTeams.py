rating1 = [2, 5, 3, 4, 1]
rating2 = [1, 2, 3, 4]
rating3 = [2, 1, 3]


def countTeam(num):
    c = 0
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            for k in range(j+1, len(num)):
                if num[i] > num[j] > num[k] or num[i] < num[j] < num[k]:
                    c = c+1
    return c


print(countTeam(rating1))
print(countTeam(rating2))
print(countTeam(rating3))
