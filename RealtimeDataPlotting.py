from itertools import count

import matplotlib.pyplot as plt
import psutil
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x = []
y = []

index = count()


def animate(i):
    x.append(next(index))
    temp = psutil.cpu_percent()
    y.append(temp)
    plt.plot(x, y)


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()

plt.show()
