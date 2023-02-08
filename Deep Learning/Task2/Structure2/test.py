# -*- coding: utf-8 -*-
import re

log_dir = r"E:\Project\大数据实验室\大项目\Task1\output\train.log"
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
        valid_acc_result = float(valid_acc_list[0])
        train_loss_list.append(valid_loss_result)
        train_acc_list.append(valid_acc_result)
