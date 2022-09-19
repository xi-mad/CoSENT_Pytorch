# CoSENT_Pytorch

比Sentence-BERT更有效的句向量方案

## 
- 参考: https://github.com/bojone/CoSENT
- 对应博客：https://kexue.fm/archives/8847
- 孟子预训练模型: https://github.com/Langboat/Mengzi


## 实验结果
实验效果来了。 预训练模型用的是孟子(换成其他模型同样可以。如google-bert、roberta等), 学习率2e-5,batch_size=64,等价苏神代码中的batch_size=32. 只用了训练集训练，然后在测试集上做测试。 分别训练了5个epoch，使用斯皮尔曼系数评价

指定不同数据集，只需在config.py文件中，修改下面两个参数:  
parser.add_argument('--train_data', default='./data/PAWSX/PAWSX.train.data', type=str, help='训练数据集')  
parser.add_argument('--test_data', default='./data/PAWSX/PAWSX.test.data', type=str, help='测试数据集')

**另外说明:** 本实验的句子编码向量是取embedding和最后一层池化后的结果。  也可以试试其他方式，如CLS, 最后一层池化等。 最近做了一些实现，发现cls更好一些。

<b>我的实验结果</b>
| | ATEC | BQ | LCQMC | PAWSX | STS-B | Avg |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| MengZi+CoSENT | **50.5270** | **72.2789** | **78.6981** | **60.1437** | **80.1544** | **68.3604** |
| Sentence-MengZi | 40.7809 | 70.6998 | 77.2590 | 46.31491 | 49.9348 | 56.9978 |
| Roberta+CoSENT | **50.5969** | **72.5191** | 79.3777 | **60.5475** | **80.4344** | **68.6951** | 
| Sentence-Roberta | 48.5157 | 67.8545 | **79.6023** | 60.1675 | 71.0148 | 65.4309 | 


<b>苏神的结果:</b>
train训练、test测试：
| | ATEC | BQ | LCQMC | PAWSX | STS-B | Avg |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| BERT+CoSENT | **49.74** | **72.38** | 78.69 | **60.00** | **80.14** | **68.19** |
| Sentence-BERT | 46.36 | 70.36 | **78.72** | 46.86 | 66.41 | 61.74 |
| RoBERTa+CoSENT | **50.81** | **71.45** | **79.31** | **61.56** | **81.13** | **68.85** |
| Sentence-RoBERTa | 48.29 | 69.99 | 79.22 | 44.10 | 72.42 | 62.80 |

## 使用
1. 运行CoSENT模型  

```
sh start.sh
```

2. 运行SentenceBert模型

```
首先，执行 python sentence_bert/data_helper.py  生成对应的数据
再执行 CUDA_VISIBLE_DEVICES=0 python sentence_bert/run_sentence_bert_transformers_reg_loss.py
```

## **更多句子表示学习的模型见: [链接](https://github.com/shawroad/Semantic-Textual-Similarity-Pytorch)**
