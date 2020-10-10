from itertools import count

import matplotlib.pyplot as plt
import psutil
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')
fig = plt.figure()
ax = fig.add_subplot(111)

x = []
y = []

index = count()


def animate(i):
    temp = next(index)
    x.append(temp)

    y.append(psutil.cpu_percent())
    ax.cla()  # clear out the axis
    ax.plot(x, y)
    ax.set_xlim(left=max(0, temp - 50), right=temp + 50)  # this line set the x-axis limit


ani = FuncAnimation(plt.gcf(), animate, interval=100)
plt.show()
