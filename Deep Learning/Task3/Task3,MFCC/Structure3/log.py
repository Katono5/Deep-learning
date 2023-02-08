# -*- coding: utf-8 -*-
import logging
from params3 import *
import matplotlib.pyplot as plt
import re

def get_logger(filename, verbosity=1, name=None):

    level_dict = {0: logging.DEBUG, 1: logging.INFO, 2: logging.WARNING}
    # 定义log输出的样式
    formatter = logging.Formatter(
        "[%(asctime)s][%(filename)s][line:%(lineno)d][%(levelname)s] %(message)s"
    )
    logger = logging.getLogger(name)
    logger.setLevel(level_dict[verbosity])

    # 在文件中保存日志文件
    file_handler = logging.FileHandler(filename, "a")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # 在程序运行时在终端显示日志文件
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger

def draw_plot():
    log_dir = Params.train_log_dir
    train_loss_list = []
    train_acc_list = []
    valid_loss_list = []
    valid_acc_list = []
    f = open(log_dir, 'r')
    data = []

    for line in f:
        if (line.find('train_loss') >= 0):
            loss_pattern = re.compile(r"(?<=train_loss=)\d+\.\d+")
            acc_pattern = re.compile(r"(?<=train_acc=)\d+\.\d+")
            train_loss_result = loss_pattern.findall(line)
            train_acc_result = acc_pattern.findall(line)
            train_loss_result = float(train_loss_result[0])
            train_acc_result = float(train_acc_result[0])
            train_loss_list.append(train_loss_result)
            train_acc_list.append(train_acc_result)

        if (line.find('valid_loss') >= 0):
            loss_pattern = re.compile(r"(?<=valid_loss=)\d+\.\d+")
            acc_pattern = re.compile(r"(?<=valid_acc=)\d+\.\d+")
            valid_loss_result = loss_pattern.findall(line)
            valid_acc_result = acc_pattern.findall(line)
            valid_loss_result = float(valid_loss_result[0])
            valid_acc_result = float(valid_acc_result[0])
            valid_loss_list.append(valid_loss_result)
            valid_acc_list.append(valid_acc_result)
    plt.title('loss plot')
    plt.plot(train_loss_list, c='red', label='train_loss')
    plt.plot(valid_loss_list, c='green', label='valid_loss')
    plt.show()
    plt.title('acc plot')
    plt.plot(train_acc_list, c='red', label='train_acc')
    plt.plot(valid_acc_list, c='green', label='valid_acc')
    plt.show()
draw_plot()