import os
import numpy as np

import matplotlib as mpl
mpl.use('Agg')
mpl.rc('text', hinting=False)
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

for font in ['Vera', 'cmr10']:

    prop = fm.FontProperties(fname=os.path.abspath('%s.ttf' % font), weight=0, stretch='normal', size=400)

    fig = plt.figure(figsize=(4,4))
    fig.text(0.5, 0.5, "a", fontproperties=prop, ha='center', va='center')
    fig.savefig('%s_nohint.png' % font, dpi=100)
    fig.savefig('%s_nohint.rgba' % font, dpi=100)
    fig.savefig('%s_nohint.eps' % font, dpi=100)

