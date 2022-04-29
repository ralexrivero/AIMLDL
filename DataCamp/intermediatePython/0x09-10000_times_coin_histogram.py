#!/usr/bin/env python3
""" distribution on 100 throw a coin """
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
final_tails = []

for x in range(10000):
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)
    # print(tails)
    final_tails.append(tails[-1])
# print(final_tails)

plt.hist(final_tails, bins=10)
plt.show()
