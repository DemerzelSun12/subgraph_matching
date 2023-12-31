import re
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


class ReadData:

    datasetScale = {"Enron": "Tiny",
                    "FIRSTMM-DB": "Tiny",
                    "DD": "Small",
                    "Gowalla": "Small",
                    "Patents": "Medium",
                    "REDDIT-MULTI-12K": "Medium",
                    "Orkut": "Large",
                    "sinaweibo": "Large"}

    def __init__(self):
        super().__init__()
        self.queryTime = [[[0 for i in range(3)] for j in range(9)] for k in range(8)]
        self.querySize = [["1 2" for i in range(9)] for j in range(8)]
        self.datasetName = ["Enron", "FIRSTMM-DB", "DD", "Gowalla", "Patents", "REDDIT-MULTI-12K", "Orkut", "sinaweibo"]
        self.queryIndex = {"4 4":0,"4 6":1,"5 5":2,"5 7":3,"6 6":4,"6 9":5,"7 7":6,"7 10":7,"8 8":8,"8 12":9,"9 9":10,"9 13":11,"10 10":12,"10 15":13,"11 11":14,"11 16":15,"12 12":16,"12 18":17}
        self.phaseNum = [[0 for i in range(9)] for j in range(8)]

    def readPhase(self):
        with open('./DVPhaseCal.csv', 'r') as rf:
            lines = rf.readlines()
            index = -1
            for i in range(len(lines)):
                line = lines[i]
                infos = re.split(r'[, \s]', line)
                infos = [item for item in filter(lambda x:x != '', infos)]
                if len(infos) == 1:
                    index += 1
                    continue
                vnum = int(infos[0])
                enum = int(infos[1])
                if enum>vnum :
                    self.phaseNum[index][vnum-4] = int(infos[2].strip())

    
    def readCsv(self):
        for dataset in self.datasetName:
            # print(dataset)
            scale = self.datasetScale[dataset]
            index = self.datasetName.index(dataset)
            with open("{}_{}.csv".format(scale, dataset), 'r') as rf:
                lines = rf.readlines()
                for i in range(1,len(lines)):
                    line = lines[i]
                    infos = re.split(r'[, \s]', line)
                    infos = [item for item in filter(lambda x:x != '', infos)]
                    vnum = int(infos[0])
                    enum = int(infos[1])
                    if enum>vnum and self.queryTime[index][vnum-4][0]==0:
                        self.queryTime[index][vnum-4][0] = float(infos[2].strip())

            with open("{}_SingleV_{}.csv".format(scale, dataset), 'r') as rf:
                lines = rf.readlines()
                for i in range(1,len(lines)):
                    line = lines[i]
                    infos = re.split(r'[, \s]', line)
                    infos = [item for item in filter(lambda x:x != '', infos)]
                    vnum = int(infos[0])
                    enum = int(infos[1])
                    if enum>vnum and self.queryTime[index][vnum-4][1]==0:
                        self.queryTime[index][vnum-4][1] = float(infos[2].strip())

            with open("{}_GSI_{}.csv".format(scale, dataset), 'r') as rf:
                lines = rf.readlines()
                for i in range(1,len(lines)):
                    line = lines[i]
                    infos = re.split(r'[, \s]', line)
                    infos = [item for item in filter(lambda x:x != '', infos)]
                    vnum = int(infos[0])
                    enum = int(infos[1])
                    if enum>vnum and self.queryTime[index][vnum-4][2]==0:
                        if len(infos)<3:
                            self.queryTime[index][vnum-4][2] = 0
                        else:
                            self.queryTime[index][vnum-4][2] = int(infos[2].strip())

    def getList(self):
        self.readCsv()
        return self.queryTime, self.querySize, self.datasetName
    
    def getPhaseNum(self):
        self.readPhase()
        return self.phaseNum, self.datasetName
            
def drawFig(queryTime,datasetName):
    fig = plt.figure(figsize=(12,4.5))
    gs = fig.add_gridspec(4, 2, hspace=0, wspace=0.1)
    #axs = gs.subplots(sharex='col', sharey='row')
    axs = gs.subplots(sharex='col')
    labels=['Q'+str(i) for i in range(4,13)]
    width=0.26
    x = [i for i in range(len(labels))]
    x=np.array(x)
    #plt.text(-2,-7,"Query",fontsize=10,fontweight='bold')
    #plt.text(-12,5,"Execution Time (ms)",fontsize=10,fontweight='bold',rotation='vertical')
    fig.text(0.5, 0.02, 'Query', ha='center',fontsize=10,fontweight='bold')
    fig.text(0.005, 0.5, 'Execution Time (ms)', va='center', rotation='vertical',fontsize=10,fontweight='bold')
    for i in range(8):
        colindex = i%2
        rowindex = math.floor(i/2)
        #plt.text(-38+6.3*colindex,22.6-8*rowindex,datasetName[i],fontsize=12,fontweight="bold")
        axs[rowindex,colindex].annotate(datasetName[i],xy=(0.08+colindex*0.5,0.88-rowindex*0.21),xycoords='figure fraction',fontsize=12,fontweight="bold")
        axs[rowindex,colindex].bar(x-width/2,queryTime[i,:,0],color="orange",label="ours-DV",width=width)
        axs[rowindex,colindex].bar(x+width/2,queryTime[i,:,2],color="steelblue",label="GSI",width=width)
        yticks=np.zeros((3))
        maximum = np.max([np.max(queryTime[i,:,0]),np.max(queryTime[i,:,2])])
        ave = np.rint((maximum-0)/3)
        tickave = np.rint(ave/2)
        yticks[0] = 0+tickave
        yticks[1] = yticks[0]+ave
        yticks[2] = yticks[1]+ave
        axs[rowindex,colindex].set_yticks(yticks)
        axs[rowindex,colindex].set_xticks(range(9))
        fontdict={'fontsize':9}
        axs[rowindex,colindex].set_xticklabels(labels,fontdict=fontdict)
        axs[rowindex,colindex].grid(axis='y', linestyle='-.')
        axs[rowindex,colindex].set_axisbelow(True)
        handles, labelsx = axs[rowindex,colindex].get_legend_handles_labels()
    
    #axs[2,6].tick_params(axis='x',bottom=False,top=False,labelbottom=False)
    #axs[2,6].spines['right'].set_visible(False)
    #axs[2,6].spines['bottom'].set_visible(False)
    fig.legend(handles,labelsx,loc='lower left',ncol=2,bbox_to_anchor=(0.05,0.92,2,8),fontsize=10,labelspacing=0.58)
    fig.subplots_adjust(left=0.05, right=0.998,top=0.93, bottom=0.1,  hspace=0, wspace=0)
    fig.savefig("overperformance.eps",format='eps')
    plt.show()

def drawPhaseFig(phaseNum, datasetName):
    fig = plt.figure(figsize=(12,4.5))
    gs = fig.add_gridspec(4, 2, hspace=0.15, wspace=0.1)
    #axs = gs.subplots(sharex='col', sharey='row')
    axs = gs.subplots(sharex='col')
    labels=['Q'+str(i) for i in range(4,13)]
    width=0.26
    x = [i for i in range(len(labels))]
    x=np.array(x)
    #plt.text(-2,-7,"Query",fontsize=10,fontweight='bold')
    #plt.text(-12,5,"Execution Time (ms)",fontsize=10,fontweight='bold',rotation='vertical')
    
    for i in range(8):
        colindex = i%2
        rowindex = math.floor(i/2)
        #plt.text(-38+6.3*colindex,22.6-8*rowindex,datasetName[i],fontsize=12,fontweight="bold")
        axs[rowindex,colindex].annotate(datasetName[i],xy=(0.08+colindex*0.5,0.88-rowindex*0.21),xycoords='figure fraction',fontsize=12,fontweight="bold")
        axs[rowindex,colindex].bar(x-width/2,phaseNum[i,:],color="orange",label="DV Phase number",width=width)
        yticks=np.zeros((4))
        # maximum = np.max(phaseNum[i,:])
        # ave = np.rint((maximum-0)/3)
        # tickave = np.rint(ave/2)
        # print(tickave)
        # yticks[0] = 0 + tickave
        # yticks[1] = yticks[0]+ave
        # yticks[2] = yticks[1]+ave
        yticks = [0, 1, 2, 3, 4]
        axs[rowindex,colindex].set_yticks(yticks)
        axs[rowindex,colindex].set_xticks(range(9))
        fontdict={'fontsize':9}
        axs[rowindex,colindex].set_xticklabels(labels,fontdict=fontdict)
        axs[rowindex,colindex].grid(axis='y', linestyle='-.')
        axs[rowindex,colindex].set_axisbelow(True)
        handles, labelsx = axs[rowindex,colindex].get_legend_handles_labels()
    
    #axs[2,6].tick_params(axis='x',bottom=False,top=False,labelbottom=False)
    #axs[2,6].spines['right'].set_visible(False)
    #axs[2,6].spines['bottom'].set_visible(False)
    fig.legend(handles,labelsx,loc='lower left',ncol=2,bbox_to_anchor=(0.05,0.92,2,8),fontsize=10,labelspacing=0.58)
    fig.subplots_adjust(left=0.05, right=0.998,top=0.93, bottom=0.1)
    fig.savefig("overperformance.eps",format='eps')
    plt.show()

perfData = ReadData()
# queryTime, querySize, datasetName = perfData.getList()
# queryTime = np.array(queryTime)
# drawFig(queryTime,datasetName)

phaseNum, datasetName = perfData.getPhaseNum()
phaseNum = np.array(phaseNum)
drawPhaseFig(phaseNum, datasetName)