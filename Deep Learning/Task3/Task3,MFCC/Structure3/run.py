# -*- coding: utf-8 -*-
import os
from params3 import *
from Model import *
from Datasets import *
from torch.utils.data import DataLoader
from log import *

PARAMS = Params()
if PARAMS.use_gpu:
    DEVICE = torch.device('cuda')
else:
    DEVICE = torch.device('cpu')

if not os.path.exists(PARAMS.output_dir):
    os.makedirs(PARAMS.output_dir)

# 调用logger类，对logger初始化
logger = get_logger(Params.train_log_dir)

def run_task():
    train_data = Read_datasets(PARAMS, 16000, 44100)
    valid_data = Read_datasets(PARAMS, 16000, 44100, False)

    train_data_size = len(train_data)
    valid_data_size = len(valid_data)

    print("训练训练集长度：%d" % (train_data_size))
    print("训练验证集长度：%d" % (valid_data_size))

    train_dataloader = DataLoader(
        dataset=train_data,
        batch_size=PARAMS.batch_size,
        num_workers=PARAMS.num_workers,
        shuffle=True,
    )
    valid_dataloader = DataLoader(
        dataset=valid_data,
        batch_size=PARAMS.batch_size,
        num_workers=PARAMS.num_workers,
        shuffle=True,
    )
    net = Task3Net(1).to(DEVICE)
    loss_fn = torch.nn.CrossEntropyLoss().to(DEVICE)

    for i in range(PARAMS.epochs):
        current_epoch = i + 1
        optimizer = torch.optim.Adam(params=net.parameters(), lr=warm_up_lr(current_epoch))
        print("---------现在在训练第%d轮---------" % (current_epoch))
        # 对准确率初始化
        train_acc = 0
        train_counter = 0
        # 开始训练模型
        net.train()
        for data in train_dataloader:  # 对每一个文件开始训练
            audios, labels = data  # 把label和feature分开
            audios = audios.to(DEVICE)
            labels = labels.to(DEVICE)
            optimizer.zero_grad()  # 梯度归零
            outputs = net(audios)  # 让features过一遍网络，得到输出
            loss = loss_fn(outputs, labels)  # 计算loss
            loss.backward()  # 梯度反向传播便于修改模型参数
            optimizer.step()  # 对参数进行更新，优化模型

            train_counter += 1  # 训练次数+1
            # 检验outputs的label是否和原label符合，如果相同则为1，否则为0
            accuracy = (outputs.argmax(1) == labels).sum()
            train_acc += accuracy
            if (train_counter % PARAMS.printstep) == 0:
                print(
                    "[第%d/%d轮] 第%d次训练, loss: %.4f"
                    % (current_epoch, PARAMS.epochs, train_counter, loss.item())
                )
        logger.info('Epoch:[{}/{}]\t train_loss={:.5f}\t train_acc={:.3f}'.format(i + 1, Params.epochs,
                                                                                  loss, ((train_acc / train_data_size) * 100)))
        print("当前训练集上准确率：%.2f%%" % ((train_acc / train_data_size) * 100))

        # 对训练集的准确率进行初始化
        valid_acc = 0
        # 开始测试模型
        net.eval()
        for data in valid_dataloader:
            audios, labels = data
            audios = audios.to(DEVICE)
            labels = labels.to(DEVICE)
            outputs = net(audios)
            loss = loss_fn(outputs, labels)
            accuracy = (outputs.argmax(1) == labels).sum()
            valid_acc += accuracy
        print("\033[0;32;40m当前测试集上方准确率: %.2f%%\033[0m"
              % ((valid_acc / valid_data_size) * 100))
        # 每两次训练保存一次训练模型
        if current_epoch % PARAMS.save_step == 0:
            torch.save(net, PARAMS.output_dir + "/net_{}.pth".format(i))
            print("第%d次训练模型已保存" % (i + 1))
        logger.info('Epoch:[{}/{}]\t valid_loss={:.5f}\t valid_acc={:.3f}'.format(i + 1, Params.epochs,
                                                                                  loss, ((valid_acc / valid_data_size) * 100)))

    draw_plot()