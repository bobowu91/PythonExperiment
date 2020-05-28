# from matplotlib import pyplot as plt
import random
options = ['a', 'b', 'c', 'd']


# plt.hist(correct_answer)
# plt.show()
total = 100
diff = list()
for _ in range(1000):

    correct_answer = random.choices(options, k=total)
    myguess_2 = random.choices(options, k=total)
    hit = [1 for i, j in zip(correct_answer, myguess_2) if i == j]

    diff.append(sum(hit) - correct_answer.count('a'))

positive = [i for i in diff if i > 0]
negative = [i for i in diff if i < 0]

print(f"{len(positive)/1000: .2%} of the time random guess is better.")
print(f"{len(negative)/1000: .2%} of the time one-for-all guess is better.")
