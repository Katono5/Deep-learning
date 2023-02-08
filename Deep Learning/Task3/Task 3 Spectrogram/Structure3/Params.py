# -*- coding: utf-8 -*-
class Params:
    lr = 0.001
    epochs = 100
    batch_size = 64
    data_dir = r'E:\Project\大数据实验室\大项目\Datasets\考核项目三数据集'
    train_dir = r'E:\Project\大数据实验室\大项目\Datasets\考核项目三数据集split\train'
    valid_dir = r'E:\Project\大数据实验室\大项目\Datasets\考核项目三数据集split\valid'
    output_dir = r'./output'
    train_log_dir = r'./output/train.log'
    use_gpu = True
    num_workers =3
    num_classes = 2
    printstep = 2
    save_step = 2

def warm_up_lr(current_epoch):
    if current_epoch == 1:
        return 0.0001
    elif current_epoch <= 50:
        return 0.0001 + 0.00033 * current_epoch
    else:
        return 0.0101 - current_epoch*0.00003