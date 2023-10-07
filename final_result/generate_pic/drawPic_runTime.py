import matplotlib
#matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.patches as patches
import pickle
import math
from ReadData import ReadData
from matplotlib.pyplot  import MultipleLocator
from matplotlib import gridspec
from matplotlib.ticker import FixedLocator
from pylab import *

def generate_picture():
    data = ReadData()
    time, query, name = data.getList()
    time = np.array(time)

    subplots_adjust(left=0.1,bottom=0.1,top=0.9,right=0.9,hspace=0.5,wspace=0.5)
    x = np.arange(len(query[0]))
    width = 0.2
    # plt.figure(figsize=(20,40))
    fig = plt.subplot(4,2,1)
    # plt.plot(t,s,'b--')
    fig.bar(x=x - width, height=(time[0].T)[0], width=width, color='red', label="DV")
    fig.bar(x=x, height=(time[0].T)[1], width=width, color='blue', label="SV")
    fig.bar(x=x + width, height=(time[0].T)[2], width=width, color='green', label="GSI")
    fig.grid(axis='y', linestyle='-.')
    fig.set_axisbelow(True)
    fig.set_xticks(x)
    fig.set_xlabel(name[0], color='black')
    fig.set_xticklabels(query[0])
    fig.set_ylabel('Time (ms)')
    # fig.legend()
    
    plt.legend(loc=2)

    fig = plt.subplot(4,2,2)
    # plt.plot(t,s,'b--')
    fig.bar(x=x - width, height=(time[1].T)[0], width=width, color='red', label="DV")
    fig.bar(x=x, height=(time[1].T)[1], width=width, color='blue', label="SV")
    fig.bar(x=x + width, height=(time[1].T)[2], width=width, color='green', label="GSI")
    fig.grid(axis='y', linestyle='-.')
    fig.set_axisbelow(True)
    fig.set_xticks(x)
    fig.set_xlabel(name[1], color='black')
    fig.set_xticklabels(query[1])
    fig.set_ylabel('Time (ms)')
    # fig.legend()

    fig = plt.subplot(4,2,3)
    # plt.plot(t,s,'b--')
    fig.bar(x=x - width, height=(time[2].T)[0], width=width, color='red', label="DV")
    fig.bar(x=x, height=(time[2].T)[1], width=width, color='blue', label="SV")
    fig.bar(x=x + width, height=(time[2].T)[2], width=width, color='green', label="GSI")
    fig.grid(axis='y', linestyle='-.')
    fig.set_axisbelow(True)
    fig.set_xticks(x)
    fig.set_xlabel(name[2], color='black')
    fig.set_xticklabels(query[2])
    fig.set_ylabel('Time (ms)')
    # fig.legend()


    fig = plt.subplot(4,2,4)
    # plt.plot(t,s,'b--')
    fig.bar(x=x - width, height=(time[3].T)[0], width=width, color='red', label="DV")
    fig.bar(x=x, height=(time[3].T)[1], width=width, color='blue', label="SV")
    fig.bar(x=x + width, height=(time[3].T)[2], width=width, color='green', label="GSI")
    fig.grid(axis='y', linestyle='-.')
    fig.set_axisbelow(True)
    fig.set_xticks(x)
    fig.set_xlabel(name[3], color='black')
    fig.set_xticklabels(query[3])
    fig.set_ylabel('Time (ms)',rotation='vertical')
    # fig.legend()

    fig = plt.subplot(4,2,5)
    # plt.plot(t,s,'b--')
    fig.bar(x=x - width, height=(time[4].T)[0], width=width, color='red', label="DV")
    fig.bar(x=x, height=(time[4].T)[1], width=width, color='blue', label="SV")
    fig.bar(x=x + width, height=(time[4].T)[2], width=width, color='green', label="GSI")
    fig.grid(axis='y', linestyle='-.')
    fig.set_axisbelow(True)
    fig.set_xticks(x)
    fig.set_xlabel(name[4], color='black')
    fig.set_xticklabels(query[4])
    fig.set_ylabel('Time (ms)')
    # fig.legend()

    fig = plt.subplot(4,2,6)
    # plt.plot(t,s,'b--')
    fig.bar(x=x - width, height=(time[5].T)[0], width=width, color='red', label="DV")
    fig.bar(x=x, height=(time[5].T)[1], width=width, color='blue', label="SV")
    fig.bar(x=x + width, height=(time[5].T)[2], width=width, color='green', label="GSI")
    fig.grid(axis='y', linestyle='-.')
    fig.set_axisbelow(True)
    fig.set_xticks(x)
    fig.set_xlabel(name[5], color='black')
    fig.set_xticklabels(query[5])
    fig.set_ylabel('Time (ms)')
    # fig.legend()

    fig = plt.subplot(4,2,7)
    # plt.plot(t,s,'b--')
    fig.bar(x=x - width, height=(time[6].T)[0], width=width, color='red', label="DV")
    fig.bar(x=x, height=(time[6].T)[1], width=width, color='blue', label="SV")
    fig.bar(x=x + width, height=(time[6].T)[2], width=width, color='green', label="GSI")
    fig.grid(axis='y', linestyle='-.')
    fig.set_axisbelow(True)
    fig.set_xticks(x)
    fig.set_xlabel(name[6], color='black')
    fig.set_xticklabels(query[6])
    fig.set_ylabel('Time (ms)')
    # fig.legend()


    fig = plt.subplot(4,2,8)
    # plt.plot(t,s,'b--')
    fig.bar(x=x - width, height=(time[7].T)[0], width=width, color='red', label="DV")
    fig.bar(x=x, height=(time[7].T)[1], width=width, color='blue', label="SV")
    fig.bar(x=x + width, height=(time[7].T)[2], width=width, color='green', label="GSI")
    fig.grid(axis='y', linestyle='-.')
    fig.set_axisbelow(True)
    fig.set_xticks(x)
    fig.set_xlabel(name[7], color='black')
    fig.set_xticklabels(query[7])
    fig.set_ylabel('Time (ms)')
    # fig.legend()


    plt.show()

generate_picture()