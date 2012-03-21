import os
import numpy as np

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

for font in ['Vera', 'cmr10']:

    prop = fm.FontProperties(fname=os.path.abspath('%s.ttf' % font), weight=0, stretch='normal', size=20)

    fig = plt.figure(figsize=(5,5))
    fig.text(0.5, 0.5, "abcdefghijklmnopqrstuvwxyz", fontproperties=prop, ha='center', va='center')
    fig.savefig('%s_small.png' % font, dpi=100)
    fig.savefig('%s_small.rgba' % font, dpi=100)
    fig.savefig('%s_small.eps' % font, dpi=100)

