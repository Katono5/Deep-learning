# -*- coding: utf-8 -*-
import torch
import torch.nn as nn

num_classes = 2

# 每一个有残差的结构都相同，因此单独定义一个类方便后续不断引用
# 残差结构默认为True
class Repeated_block(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride, padding, short_cut=True):
        super(Repeated_block, self).__init__()
        self.Conv1 = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding),
            nn.BatchNorm2d(out_channels),
        )
        self.relu = nn.ReLU()
        if short_cut:
            self.Conv2 = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, 1, stride),
                nn.BatchNorm2d(out_channels),
            )
        else:
            self.Conv2 = None

    def forward(self, X):
        y = self.Conv1(X)
        # 如果有残差结构，则多卷积一次
        if self.Conv2:
            X = self.Conv2(X)
        # 在最终把初始的x和走过一边网络的x一起激活来避免训练不重要特征对模型的影响，保证模型不会走歪
        return self.relu(X + y)



class Task3Net(nn.Module):
    def __init__(self, num_channels):
        super(Task3Net, self).__init__()
        self.Conv1 = nn.Sequential(
            nn.Conv2d(in_channels=num_channels, out_channels=64, kernel_size=5, stride=2, padding=2),
            # out = (112 + 2 * 2 - 5) / 2 + 1 = 56
            nn.BatchNorm2d(64),
            nn.ReLU(),
        )
        self.Maxpooling = nn.Sequential(
            nn.MaxPool2d((3, 3), stride=2, padding=1)
            # out = 56 / 2 = 28
        )
        self.layer1 = Repeated_block(64, 128, 3, 2, 1)
        # out = (28 + 2 * 1 - 3) / 2 + 1 = 14
        self.layer2 = Repeated_block(128, 256, 3, 1, 1)
        # out = (14 + 2 * 1 - 3) / 1 + 1 = 14
        self.layer3 = Repeated_block(256, 128, 3, 1, 1)
        # out = (14 + 2 * 1 - 3) / 1 + 1 = 14

        self.Conv2 = nn.Sequential(
            nn.Conv2d(128, 256, 3, 2, 1),
            # out = (14 + 2 * 1 - 3) / 2 + 1 = 7
            nn.BatchNorm2d(256),
            nn.ReLU(),
        )
        self.GlobalAvgPool = nn.AvgPool2d(3)
        # out = 3 / 3 = 1

        # 定义全连接层
        self.FC = nn.Sequential(
            nn.Linear(256, 256),
            nn.ReLU(),
            # 定义dropout比例，即丢弃20%的连接
            nn.Dropout(0.2),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        x = self.Conv1(x)
        x = self.Maxpooling(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.Conv2(x)
        x = self.GlobalAvgPool(x)
        # 把x铺平，不铺平会因为维度不相同报错 32768维深长度是1 -> 1维长度32768
        x = x.view(x.size(0), -1)
        x = self.FC(x)
        return x