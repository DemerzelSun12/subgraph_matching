import re

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

    
    def readCsv(self):
        for dataset in self.datasetName:
            scale = self.datasetScale[dataset]
            index = self.datasetName.index(dataset)
            with open("{}_{}.csv".format(scale, dataset), 'r') as rf:
                rf.readline()
                for i in range(9):
                    line = rf.readline()
                    infos = re.split(r'[, \s]', line)
                    infos = [item for item in filter(lambda x:x != '', infos)]
                    self.querySize[index][i] = "{} {}".format(infos[0], infos[1])
                    self.queryTime[index][i][0] = float(infos[2].strip())

            with open("{}_SingleV_{}.csv".format(scale, dataset), 'r') as rf:
                rf.readline()
                for i in range(9):
                    line = rf.readline()
                    infos = re.split(r'[, \s]', line)
                    infos = [item for item in filter(lambda x:x != '', infos)]
                    self.querySize[index][i] = "{} {}".format(infos[0], infos[1])
                    self.queryTime[index][i][1] = float(infos[2].strip())

            with open("{}_GSI_{}.csv".format(scale, dataset), 'r') as rf:
                rf.readline()
                for i in range(9):
                    line = rf.readline()
                    infos = re.split(r'[, \s]', line)
                    infos = [item for item in filter(lambda x:x != '', infos)]
                    self.querySize[index][i] = "{} {}".format(infos[0], infos[1])
                    self.queryTime[index][i][2] = int(infos[2].strip())

    def getList(self):
        self.readCsv()
        return self.queryTime, self.querySize, self.datasetName
            


    