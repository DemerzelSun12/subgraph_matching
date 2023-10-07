import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.pyplot  import MultipleLocator
from matplotlib import gridspec
from matplotlib.ticker import FixedLocator
import matplotlib.patches as patches
import numpy as np
import pickle
import math


def drawAccessTime():
    datagraph=["EN","FD","GO","DD","OR","PA","RE"]
    accessTime=[[22.364,32.729,137.982,242.434,2417.91,6016.49,4567.93],
                [39.431,72.307,339.663,635.242,5892.58,15988.2,12241.2],
                [27.617,43.647,247.064,341.028,2708.84,7358.09,5734.56]]
    accessTime = np.array(accessTime)
    speedup = accessTime[1]/accessTime[0]
    avespeedup = np.mean(speedup)
    print(avespeedup)
    x = np.arange(len(datagraph))
    width = 0.2
    
    fig, ax = plt.subplots(figsize=(6,3))
    ax.bar(x - width, accessTime[0], width, color="orange",label='interval-PCSR')
    ax.bar(x, accessTime[2], width, color="blue", label='hash-PCSR without modulo operation')
    ax.bar(x+width, accessTime[1], width, color="mediumseagreen", label='hash-PCSR')
    ax.grid(axis='y', linestyle='-.')
    ax.set_axisbelow(True)
    ax.set_ylabel('Searching Time (ms)')
    plt.yscale('log')
    ax.set_xticks(x)
    ax.set_xticklabels(datagraph)
    #ax.set_ylim(0, 8)
    #ax.set_xlim(-0.6, 19.6)
    ax.legend()
    fig.tight_layout(pad=0) 
    fig.savefig("accesstime.eps",format='eps')
    plt.show()

drawAccessTime()