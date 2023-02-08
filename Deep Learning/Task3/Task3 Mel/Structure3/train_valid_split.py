# -*- coding: utf-8 -*-
import os
import random
import shutil
from params3 import *

def make_dir(new_dir):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

random.seed(1)

split_dir = r'E:\Project\大数据实验室\大项目\Datasets\考核项目三数据集split'
make_dir(split_dir)
train_dir = os.path.join(split_dir, 'train')
valid_dir = os.path.join(split_dir, 'valid')
train_radio = 0.9
valid_radio = 0.1
for root, dirs, files in os.walk(Params.data_dir):
    for sub_dir in dirs:
        sounds = os.listdir(os.path.join(root, sub_dir))
        sounds = list(filter(lambda x: x.endswith('.wav'), sounds))
        random.shuffle(sounds)
        sound_count = len(sounds)
        train_point = int(sound_count * train_radio)
        valid_point = int(sound_count * valid_radio)

        for i in range(sound_count):

            if i < train_point:
                out_dir = os.path.join(train_dir, sub_dir)
            else:
                out_dir = os.path.join(valid_dir, sub_dir)

            make_dir(out_dir)
            target_path = os.path.join(out_dir, sounds[i])
            src_path = os.path.join(Params.data_dir, sub_dir, sounds[i])
            shutil.copy(src_path, target_path)

        print('Class:{}, train:{}, valid:{}'.format(sub_dir, train_point, valid_point))

