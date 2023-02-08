# -*- coding: utf-8 -*-
import torch
import torch.nn as nn

num_classes = 6

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



class Task1Net(nn.Module):
    def __init__(self, num_channels):
        super(Task1Net, self).__init__()
        self.Conv1 = nn.Sequential(
            nn.Conv2d(in_channels=num_channels, out_channels=64, kernel_size=5, stride=2, padding=2),
            # out = (112 + 2 * 2 - 5) / 2 + 1 = 56
            nn.BatchNorm2d(64),
            nn.ReLU(),
        )
        self.Maxpooling1 = nn.Sequential(
            nn.MaxPool2d((3, 3), stride=2, padding=1)
            # out = 56 / 2 = 28
        )
        self.layer1 = Repeated_block(64, 128, 3, 2, 1)
        # out = (28 + 2 * 1 - 3) / 2 + 1 = 14
        self.layer2 = Repeated_block(128, 128, 3, 1, 1)
        # out = (14 + 2 * 1 - 3) / 1 + 1 = 14


        self.Conv2 = nn.Sequential(
            nn.Conv2d(128, 512, 3, 2, 1),
            # out = (14 + 2 * 1 - 3) / 2 + 1 = 7
            nn.BatchNorm2d(512),
            nn.ReLU(),
        )
        self.GlobalAvgPool = nn.AvgPool2d(7)
        # out = 7 / 7 = 1

        # 定义全连接层
        self.FC = nn.Sequential(
            nn.Linear(512, 256),
            nn.ReLU(),
            # 定义dropout比例，即丢弃20%的连接
            nn.Dropout(0.2),
            nn.Linear(256, num_classes),
        )

    def forward(self, x):
        x = self.Conv1(x)
        x = self.Maxpooling1(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.Conv2(x)
        x = self.GlobalAvgPool(x)
        # 把x铺平，不铺平会因为维度不相同报错 32768维深长度是1 -> 1维长度32768
        x = x.view(x.size(0), -1)
        x = self.FC(x)
        x = nn.Softmax(x, dim=1)
        return x

# import torch
# import torch.nn as nn
# from torch.nn import functional as F
#
#
# class RestNetBasicBlock(nn.Module):
#     def __init__(self, in_channels, out_channels, stride):
#         super(RestNetBasicBlock, self).__init__()
#         self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1)
#         self.bn1 = nn.BatchNorm2d(out_channels)
#         self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=stride, padding=1)
#         self.bn2 = nn.BatchNorm2d(out_channels)
#
#     def forward(self, x):
#         output = self.conv1(x)
#         output = F.relu(self.bn1(output))
#         output = self.conv2(output)
#         output = self.bn2(output)
#         return F.relu(x + output)
#
#
# class RestNetDownBlock(nn.Module):
#     def __init__(self, in_channels, out_channels, stride):
#         super(RestNetDownBlock, self).__init__()
#         self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride[0], padding=1)
#         self.bn1 = nn.BatchNorm2d(out_channels)
#         self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=stride[1], padding=1)
#         self.bn2 = nn.BatchNorm2d(out_channels)
#         self.extra = nn.Sequential(
#             nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride[0], padding=0),
#             nn.BatchNorm2d(out_channels)
#         )
#
#     def forward(self, x):
#         extra_x = self.extra(x)
#         output = self.conv1(x)
#         out = F.relu(self.bn1(output))
#
#         out = self.conv2(out)
#         out = self.bn2(out)
#         return F.relu(extra_x + out)
#
#
# class ResNet18(nn.Module):
#     def __init__(self):
#         super(ResNet18, self).__init__()
#         self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3)
#         self.bn1 = nn.BatchNorm2d(64)
#         self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
#
#         self.layer1 = nn.Sequential(RestNetBasicBlock(64, 64, 1),
#                                     RestNetBasicBlock(64, 64, 1))
#
#         self.layer2 = nn.Sequential(RestNetDownBlock(64, 128, [2, 1]),
#                                     RestNetBasicBlock(128, 128, 1))
#
#         self.layer3 = nn.Sequential(RestNetDownBlock(128, 256, [2, 1]),
#                                     RestNetBasicBlock(256, 256, 1))
#
#         self.layer4 = nn.Sequential(RestNetDownBlock(256, 512, [2, 1]),
#                                     RestNetBasicBlock(512, 512, 1))
#
#         self.avgpool = nn.AdaptiveAvgPool2d(output_size=(1, 1))
#
#         self.fc = nn.Linear(512, 6)
#
#     def forward(self, x):
#         out = self.conv1(x)
#         out = self.layer1(out)
#         out = self.layer2(out)
#         out = self.layer3(out)
#         out = self.layer4(out)
#         out = self.avgpool(out)
#         out = out.reshape(x.shape[0], -1)
#         out = self.fc(out)
#         return out
