# -*- coding: utf-8 -*-
import torch
import torch.utils.data as Data
import torchaudio
import glob
from params3 import *
param = Params()

class Read_datasets(Data.Dataset):
    def __init__(self, Params, target_samples, target_sr, isTrain=True):
        super().__init__()
        if isTrain:
            path = Params.train_dir
        else:
            path = Params.valid_dir

        files = []
        labels = []
        self.cache = []
        for class_label, class_dir in enumerate(glob.glob(path + '/*')):
            for audio_file in glob.glob(class_dir + '/*'):
                files.append(audio_file)
                labels.append(class_label)
                self.cache.append(False)
        self.files = files
        self.labels = labels
        self.target_samples = target_samples
        self.target_sr = target_sr

    def __getitem__(self, index):
        if self.cache[index] is False:
            audio = self.files[index]
            waveform, sr = torchaudio.load(audio)
            waveform = reshape_if_necessary(waveform, self.target_samples)
            waveform = resample_if_necessary(waveform, sr, self.target_sr)
            waveform = mix_down_if_necessary(waveform)
            waveform_MFCC = transform_MFCC(waveform)
            self.cache[index] = waveform_MFCC, self.labels[index]
        return self.cache[index]

    def __len__(self):
        return len(self.files)

transform_MFCC = torchaudio.transforms.MFCC(
    sample_rate=16000,
    n_mfcc=40,
    melkwargs={"n_fft": 512, "n_mels": 40, "center": False},
)

def reshape_if_necessary(waveform, target_samples):
    if waveform.shape[1] > target_samples:
        waveform = waveform[:, 0:target_samples]
    elif waveform.shape[1] < target_samples:
        num_padding = target_samples - waveform.shape[1]
        waveform = torch.nn.functional.pad(waveform, pad=(0, num_padding))
    return waveform

def resample_if_necessary(waveform, sr, target_sr):
    if sr != target_sr:
        waveform = torchaudio.functional.resample(waveform, orig_freq=sr, new_freq=target_sr)
    return waveform

def mix_down_if_necessary(waveform):
    if waveform.shape[0] > 1:
        waveform = torch.mean(waveform, dim=0, keepdim=True)
    return waveform
