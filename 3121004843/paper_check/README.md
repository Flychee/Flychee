# Python实现简易论文查重

| 软件工程   | https://edu.cnblogs.com/campus/gdgy/CSGrade21-12                |
| ---------- |-----------------------------------------------------------------|
| 作业要求   | https://edu.cnblogs.com/campus/gdgy/CSGrade21-12/homework/13014 |
| 作业目标   | 学习使用Python建立工程项目，学会论文查重的具体实现步骤                                  |
| github链接 | https://github.com/Flychee/Flychee/tree/master/3121004843                            |

# PSP

| PSP2.1                                 | Personal Software Process Stages       | 预估耗时（分钟） | 实际耗时（分钟） |
| :------------------------------------- | :------------------------------------- | :--------------: | :--------------: |
| Planning                               | 计划                                   |        30        |        30        |
| -Estimate                              | -估计这个任务需要多少时间              |        30        |        30        |
| Development                            | 开发                                   |       430        |       370        |
| -Analysis                              | -需求分析 (包括学习新技术)             |       150        |        90        |
| -Design Spec                           | -生成设计文档                          |        60        |        0         |
| -Design Review                         | -设计复审                              |        20        |        20        |
| -Coding Standard                       | -代码规范 (为目前的开发制定合适的规范) |        30        |        10        |
| -Design                                | -具体设计                              |        30        |        30        |
| -Coding                                | -具体编码                              |       120        |       180        |
| -Code Review                           | -代码复审                              |        20        |        40        |
| Test                                   | 测试（自我测试，修改代码，提交修改）   |       220        |       260        |
| -Reporting                             | -报告                                  |       100        |       120        |
| -Test Report                           | -测试报告                              |        60        |        60        |
| -Size Measurement                      | -计算工作量                            |        40        |        40        |
| -Postmortem & Process Improvement Plan | -事后总结, 并提出过程改进计划          |        20        |        40        |
|                                        | 合计                                   |       560        |       660        |

# 模块接口的设计与实现过程

### 算法模块
| 函数                       | 功能            |
|:-------------------------|:--------------|
| clean(file) | 清除Html标签与标点符号 |
| read_file(file)             | 读取文件          |
| similarity(ori, ori_add)             | 计算两份文本的相似度    |

### 关键函数实现过程

#### similarity(ori, ori_add)
使用Simhash算法生成两个文本间的Simhash值。Simhash是一种用于计算文本相似度的算法。它将文本表示为一个固定位数的二进制数值，
其中相似的文本具有较高的汉明距离，而不相似的文本具有较低的汉明距离。 计算两个文本间的海明距离（Hamming Distance），即Simhash值
之间的汉明距离。海明距离表示两个Simhash值二进制表示中不同位的数量。 根据海明距离计算相似度， 公式为：1 - (海明距离 / 两个文本的文本的SimHash值中的较大值)。


# 四、模块接口部分的性能改进

## 1. 性能分析图

![](https://dingzhen-bucket.oss-cn-guangzhou.aliyuncs.com/cheese-xuebao/202309151236893.png)

## 2. 改进思路

由分析图可以看出：
bulid_by_text函数运行时间达到了总运行时间的94.2%，证明对分词的优化是整个程序改进的关键所在，本人积累尚浅，目前仍未有更好的方法。

# 五、模块部分单元测试展示

## 1. similarity(ori, ori_add)

代码示例

```Python
def similarity(ori, ori_add):
    ori_sh = sh(ori)
    ori_add_sh = sh(ori_add)
    max_sh = max(len(bin(ori_sh.value)), len(bin(ori_add_sh.value)))
    dst = ori_sh.distance(ori_add_sh)  # 汉明距离
    result = 1 - dst / max_sh
    return result
```


所有函数100%覆盖     
![](https://dingzhen-bucket.oss-cn-guangzhou.aliyuncs.com/cheese-xuebao/202309151247592.png)   
未覆盖部分为主程序if分支    
![](https://dingzhen-bucket.oss-cn-guangzhou.aliyuncs.com/cheese-xuebao/202309151248975.png)  
# 六、模块部分异常处理说明

项目仅在读写文件时可能出现异常   
![](https://dingzhen-bucket.oss-cn-guangzhou.aliyuncs.com/cheese-xuebao/202309151249098.png)
