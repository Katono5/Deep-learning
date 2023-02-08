# -*- coding: utf-8 -*-
import torch.utils.data as Data
import torchvision as tv
import glob
from PIL import Image
from params2 import *
# 定义数据集的读取
param = Params()
class Read_datasets(Data.Dataset):
    def __init__(self, PARAMS, isTrain=True):
        super().__init__()
        self.Trans = tv.transforms.Compose([
            tv.transforms.Resize([PARAMS.img_size, PARAMS.img_size]),
            tv.transforms.RandomHorizontalFlip(),
            tv.transforms.RandomRotation(10),
            tv.transforms.ToTensor(),
            tv.transforms.Normalize((0.5,), (0.5,)),
        ])

        # 判断是否是训练集还是测试机
        if isTrain:
            path = PARAMS.train_dir
        else:
            path = PARAMS.valid_dir

        files = []
        labels = []
        self.cache = []

        # 读取文件夹
        for class_label, class_dir in enumerate(glob.glob(path + '/*')):
            for img_file in glob.glob(class_dir + '/*'):
                files.append(img_file)
                labels.append(class_label)
                self.cache.append(False)
        self.files = files
        self.labels = labels
        self.size = len(self.files)

    # 把图片一个一个 读取出来并做出处理
    def __getitem__(self, index):
        if self.cache[index] is False:
            img_file = self.files[index]
            img = Image.open(img_file)
            # 调整图像通道
            if img.mode != 'RGB':
                img = img.convert('RGB')
            # 裁剪图片大小
            img = self.Trans(img)
            self.cache[index] = [img, self.labels[index]]
        return self.cache[index]

    def __len__(self):
        return self.size
