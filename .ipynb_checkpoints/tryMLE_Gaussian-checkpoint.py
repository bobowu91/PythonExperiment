import numpy as np
import matplotlib.pyplot as plt
import math

# likelihood calculation for normal distribution 
def likelihood(a, mu, std):
    return math.exp( -(a - mu) ** 2 / (2 * std ** 2))/math.sqrt(2 * math.pi * std ** 2)

def MLE(data, start, end, mu=None, std=None):
    
    estimator = []
    xaxis = []
    
    if (mu == None) & (std != None):  # estimate max mu with a fixed std
        for i in range(10*start, 10*end, 2):
            mu = i/10
            xaxis.append(mu) # use for plot of x-axis 
            lh = [likelihood(x, mu, std) for x in data] # std can be set as 10
            product = np.prod(lh) * (10 ** 200) # use a scalar to make the number easier to interpret; no real meanings 
            estimator.append(product)
        
        
    elif (std == None) & (mu != None): # estimate max std with a fixed mu
        for i in range(10*start, 10*end, 2):
            std = i/10
            xaxis.append(std)      
            lh = [likelihood(x, mu, std) for x in data] # std can be set as 10
            product = np.prod(lh) * (10 ** 200) # use a scalar to make the number easier to interpret; no real meanings 
            estimator.append(product)
    else:
        return "Parameter setting for mu or std is not right."

    return xaxis, estimator



n = 100
mu = np.random.randint(30,50) # generate a random number as mean from 0 to 10
std = np.random.randint(3,25) # generate a random number as standard deviation from 5 to 15
x = np.random.normal(mu, std, n) #simulate 100 instances from the normal distribution


print(mu)
print(std)
print(x[0:10])

avg = np.mean(x)
sig = np.std(x)
print(avg, sig)

# histogram
count, bins, ignored = plt.hist(x, 30, density=True)
plt.show()

# 
a,b = MLE(x,3,25,mu = 30) # estimate std

plt.scatter(a, b)
plt.ylim(min(b), max(b)*1.1)
plt.show()

