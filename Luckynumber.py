num1 = [2, 3, 4, 5, 6, 7, 8, 2, 3, 3]
num2 = [1]
num3 = [6, 6, 6, 6, 6, 6, 5, 5, 5, 3, 2, 1, ]
num4 = [2, 3, 4, 5]


def luckyNumber(num):

    num_dict = {}
    for i in num:
        num_dict[i] = num.count(i)

    luck = []
    for i in num_dict:
        if i == num_dict[i]:
            luck.append(i)

    if len(luck) > 0:
        print("Luck Number is {}".format(luck))
    else:
        print("there is no lucky number.")


luckyNumber(num1)
luckyNumber(num2)
luckyNumber(num3)
luckyNumber(num4)
