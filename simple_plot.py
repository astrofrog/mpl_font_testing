import os
import numpy as np

import matplotlib as mpl
mpl.use('Agg')
mpl.rcParams['font.serif'] = [os.path.abspath('Vera.ttf')]

import matplotlib.pyplot as plt

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(t, s, linewidth=1.0)
ax.set_xlabel('time (s)', size=12)
ax.set_ylabel('voltage (mV)', size=12)
ax.set_title('About as simple as it gets, folks', size=12)

fig.savefig('simple_plot_vera.png')
