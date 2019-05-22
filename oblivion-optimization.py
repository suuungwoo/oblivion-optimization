import numpy as np
import matplotlib.pyplot as plt

num = 10000
alpha = 0.8
beta = 0.01
w1 = np.zeros(num)
w2 = np.zeros(num)

w1[0] = 0
w2[0] = -2

for i in range(num-1):
    Jw1 = w1[i] - w2[i]+1
    Jw2 = - w1[i] + w2[i]-1
    w1[i+1] = w1[i] + (-alpha * Jw1 - beta * w1[i])
    w2[i+1] = w2[i] + (-alpha * Jw2 - beta * w2[i])

plt.plot(w1, w2)
plt.annotate("start", (w1[0], w2[0]))
plt.annotate("end", (w1[-1], w2[-1]))
plt.xlabel("w1")
plt.ylabel("w2")
plt.show()
