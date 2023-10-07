目前只有七个数据集测出了对比结果，Wiki-Vote、Enron、DD、FIRSTMM-DB、Gowalla、Patents、REDDIT-MULTI-12K  。

其中，LiveJouranl数据集只测了师兄的代码，GSI的代码运行无法得到结果，GSI在运行时会产生 an illegal memory access was encountered 的报错，经检查，是 Match.cu 代码的第 1346 行的 cudaMalloc 或 1343 行的 cudaMemcpy 运行出错，在较小的图上不会报错，在较大的图上会上述两种报错。

测试用例说明：
生成了 4~20 个点，每种数量的点生成了 n, n + n/2, 2n, 2n + n/2, 3n条边，每种情况又生成了
10个query，匹配后记录时间并取了平均值，记录在相应csv文件中，所用的单位均为ms。

目前问题：

1. GSI的代码在较大的图上运行会出现 an illegal memory access was encountered 的报错，在较小的图上没有问题。
2. 大图的 genQuery 过程较慢，有时会出现 Floating point exception (core dumped) 的报错，需要重新执行。

