import numpy as np
# rolls = list(np.random.randint(1, 7, 12000))
# stat = {k: rolls.count(k) for k in set(rolls)}
# print(stat)


n_sim = 500000  # repeat this experiment for 1000 times
stats = []
for _ in range(n_sim):
    count = 0
    num = 0
    while num != 6:
        num = np.random.randint(1, 7)  # randomly generate a number
        if num % 2 == 0:  # if it is an even number but not 6; keep rolling
            count = count + 1  # the number of rolls keep adding up
        else:
            # print(f"number{num} is odd, this round has to be discarded")
            break  # if the number is even then we break the while loop

    if num == 6:  # if while loop is done by hitting 6, then record counts
        stats.append(count)

# only 25% of the time dice hit six and all even before
print(
    f"The probability of rolling a until 6 given all previous rolls are even"
    f"is {len(stats)/n_sim: .0%}")

avg = sum(stats)/len(stats)
print(
    f"The expected value of rolling a dice until 6," +
    f" given that all previous rolls have to be even is: {avg: .2f}")
