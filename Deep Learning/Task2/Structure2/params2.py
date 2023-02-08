# -*- coding: utf-8 -*-
class Params(object):
    lr = 0.001
    batch_size = 64
    data_dir = r'E:\Project\大数据实验室\大项目\Datasets\考核项目一、二数据集split'
    img_size = 112
    use_gpu = True
    num_workers = 3
    num_classes = 6
    epoch = 200
    output_dir = './output'
    printstep = 10
    save_step = 2
    train_dir = "/root/autodl-tmp/考核项目一、二数据集split/train"
    valid_dir = "/root/autodl-tmp/考核项目一、二数据集split/valid"
    train_log_dir = r'./train.log'

def warm_up_lr(current_epoch):
    if current_epoch == 1:
        return 0.0001
    elif current_epoch <= 40:
        return 0.0001 + 0.003 * current_epoch
    else:
        return 0.0151 - current_epoch*0.00005

