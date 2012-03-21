import os
import numpy as np

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

prop = fm.FontProperties(fname=os.path.abspath('Vera.ttf'), weight=0, stretch='normal', size=400)

fig = plt.figure(figsize=(4,4))
fig.text(0.5, 0.5, "a", fontproperties=prop, ha='center', va='center')
fig.savefig('hello.png', dpi=100)
fig.savefig('hello.rgba', dpi=100)
fig.savefig('hello.eps', dpi=100)
