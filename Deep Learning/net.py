import torch
import torch.nn as nn
from torchinfo import summary
# 对深度可分离单独写方便后续调用
def depth_wise(in_channels, out_channels, stride, padding):
    depth_wise_model = nn.Sequential(
        # 卷积有两层，第一层为3*3卷积
        nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=3, stride=stride, padding=padding),
        nn.BatchNorm2d(in_channels),  # 归一化处理方便处理数据
        nn.ReLU6(inplace=True),  # in_place=True直接在原数据上改写，节约内存
        # 此处用ReLU6来防止weight无限制增大使一些设备无法运行

        # 第二层为1*1点积
        nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=1, stride=stride, padding=padding),
        nn.BatchNorm2d(out_channels),
        nn.ReLU6(inplace=True),
    )
    return depth_wise_model
def bottleneck(in_channels, out_channels, stride, padding=1):
    bottleneck = nn.Sequential(
        # 这一层负责升维
        nn.Conv2d(in_channels, in_channels * 6, kernel_size=1, stride=stride),  # 因为卷积核是1所以不用padding
        nn.BatchNorm2d(in_channels * 6),
        nn.ReLU6(inplace=True),

        # 这一层负责卷积, 维度不变为out_channels
        nn.Conv2d(in_channels * 6, in_channels * 6, kernel_size=3, stride=stride, padding=padding),
        nn.BatchNorm2d(in_channels * 6),
        nn.ReLU6(inplace=True),

        # 这一层负责降维
        nn.Conv2d(in_channels * 6, out_channels, kernel_size=1, stride=stride),
        nn.BatchNorm2d(out_channels)
    )
    return bottleneck

class MobileNet_v2(nn.Module):
    def __init__(self):
        super(MobileNet_v2, self).__init__()
        self.Conv1 = nn.Sequential(
            nn.Conv2d(3, 32, 3, 2, 1),
            nn.BatchNorm2d(32),
            nn.ReLU6(inplace=True)
        )
        self.Conv2 = nn.Sequential(
            nn.Conv2d(32, 32, kernel_size=1, stride=1),
            nn.BatchNorm2d(32),
            nn.ReLU6(inplace=True),

            nn.Conv2d(32, 32, kernel_size=3, stride=1),
            nn.BatchNorm2d(32),
            nn.ReLU6(inplace=True),

            nn.Conv2d(32, 16, kernel_size=1, stride=1),
            nn.BatchNorm2d(16)
        )
        self.layers = nn.Sequential(
            bottleneck(16, 24, 2),
            bottleneck(24, 24, 1),
            bottleneck(24, 32, 2),
            bottleneck(32, 32, 1),
            bottleneck(32, 32, 1),
            bottleneck(32, 64, 2),
            bottleneck(64, 64, 1),
            bottleneck(64, 64, 1),
            bottleneck(64, 64, 1),
            bottleneck(64, 64, 1),
            bottleneck(64, 96, 1),
            bottleneck(64, 96, 1),
            bottleneck(96, 96, 1),
            bottleneck(96, 96, 1),
            bottleneck(96, 160, 2),
            bottleneck(160, 160, 1),
            bottleneck(160, 160, 1),
            bottleneck(160, 320, 1),
            bottleneck(320, 320, 1),
            nn.AvgPool2d(7),
            nn.Conv2d(1280, 10, 1),
        )
        self.pooling = nn.AvgPool2d(7),
        self.classify = nn.Conv2d(1280, 10, 1)

    def forward(self, x):
        x = self.Conv1(x)
        x = self.Conv2(x)
        x = self.layers(x)
        x = self.pooling(x)
        x = self.classify(x)
        result = nn.functional.softmax(x)
        return result


net = MobileNet_v2()
print(net)