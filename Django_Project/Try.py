import pandas as pd

dataset = {'Mobile': ['LG', 'HP'], 'prize': [12000, 15000]}
df = pd.DataFrame(dataset)
print(pd.DataFrame(dataset))

import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 15, 7, 12]
plt.plot(x, y, marker='*')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()


import numpy as np
x = np.array([1, 2, 6, 8])
y = np.array([3, 8, 1, 10])
plt.plot(x, y)
plt.show()

y = np.array([3, 8, 1, 10])
plt.plot(y, marker = '*')
plt.show()


ypoints = np.array([3, 8, 1, 10])
plt.plot(y, '*:b')
plt.show()