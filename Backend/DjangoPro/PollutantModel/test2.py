#-*- encoding: utf-8 -*-
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y = [1, 4, 9, 16, 20]

fig = plt.figure()

fig.add_subplot(111)

plt.scatter(x, y)

plt.show()
