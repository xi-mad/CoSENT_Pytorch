"""
@file   : config.py
@author : xiaolu
@email  : luxiaonlp@163.com
@time   : 2022-01-07
"""
import argparse

dataset = 'not_cross_node-not_shuffle'

def set_args():
    parser = argparse.ArgumentParser('--CoSENT进行相似性判断')
    
    
    parser.add_argument('--train_data', default='./data/{}/train.tsv'.format(dataset), type=str, help='训练数据集')
    parser.add_argument('--test_data', default='./data/{}/test.tsv'.format(dataset), type=str, help='测试数据集')

    parser.add_argument('--pretrained_model_path', default='./mengzi_pretrain/mengzi-bert-L6-H768', type=str, help='预训练模型的路径')
    parser.add_argument('--output_dir', default='./outputs', type=str, help='模型输出')
    parser.add_argument('--num_train_epochs', default=100, type=int, help='训练几轮')
    parser.add_argument('--train_batch_size', default=16, type=int, help='训练批次大小')
    parser.add_argument('--val_batch_size', default=32, type=int, help='验证批次大小')
    parser.add_argument('--gradient_accumulation_steps', default=1, type=int, help='梯度积累几次更新')
    parser.add_argument('--learning_rate', default=2e-5, type=float, help='学习率大小')
    parser.add_argument('--seed', default=43, type=int, help='随机种子')
    return parser.parse_args()
