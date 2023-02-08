# -*- coding: utf-8 -*-
class Params(object):
    lr = 0.001  # 学习率
    batch_size = 128
    data_dir = r'E:\Project\大数据实验室\大项目\Datasets\考核项目一、二数据集split'
    img_size = 112  # 决定裁剪图片尺寸的最终大小
    use_gpu = True  # 是否使用gpu
    # 并行数量
    num_workers = 3
    num_classes = 6  # 最终输出量，即结果的类别
    epoch = 100  # 训练轮数
    output_dir = './output'  # 模型存放目录
    printstep = 10  # 输出训练loss的间隔
    save_step = 2  # 存储模型的间隔
    train_dir = r'E:\Project\大数据实验室\大项目\Datasets\考核项目一、二数据集split/train'
    valid_dir = r'E:\Project\大数据实验室\大项目\Datasets\考核项目一、二数据集split/valid'
    train_log_dir = r'./output/train.log'