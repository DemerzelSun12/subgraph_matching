文件说明：

1.  Medium 中，由于 GSI 的方法要求 .g 文件的第三行输入为 “nodeNum edgeNum maxNodeLabel maxEdgeLabel”，且其默认不会有比 nodeNum 大的点编号，也就是说，假如 nodeNum = 3000，则不允许出现 “v 3001 label”这样的点。由于 Patents 的点的编号不连续，点的数量为 3,774,768，但是编号范围是从 1 到 6,009,554 ，且中间不连续，所以我生成了两个 .g 文件，一个是原始文件；一个是填补了 1 到 6,009,554 所有的点，边不变。两种文件我都在 gpumine 上和 gpumineSV 上跑了，GSI上只能跑增补的点的情况。

   - [Medium_GSI_Patents.csv](./Medium_GSI_Patents.csv)  为 GSI 的 Patents 运行结果
   - [Medium_Patents.csv](./Medium_Patents.csv) 是增补的 Patents 在 gpumine 上运行结果

   - [Medium_origin_Patents.csv](./Medium_origin_Patents.csv) 是未增补的 Patents 在 gpumine 上运行结果
   - [Medium_SingleV_origin_Patents.csv](./Medium_SingleV_origin_Patents.csv) 是未增补的 Patents 在 gpumineSV 上运行结果
   - [Medium_SingleV_Patents.csv](./Medium_SingleV_Patents.csv) 是增补的 Patents 在 gpumineSV 上运行结果

   

