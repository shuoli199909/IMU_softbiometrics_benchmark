"""
Utils for the experiments of existing algorithms (benchmark).
"""

# Author: Shuo Li
# Date: 2024/01/29

import torch


class CNN1D(torch.nn.Module):
    """1D-CNN model for age and gender estimation.
    """

    def __init__(self, num_channel=6, num_target=2) -> None:
        """Groundtruth class initialization.

        References
        ----------
        [1] Sun, Y., Lo, F. P. W., & Lo, B. (2019, May). A deep learning approach on gender and age recognition using a single inertial sensor. In 2019 IEEE 16th international conference on wearable and implantable body sensor networks (BSN) (pp. 1-4). IEEE.

        Parameters
        ----------
        num_channel: Number of channels of the input data. size=[1].
        num_target: Number of output targets. size=[1].

        Returns
        -------

        """

        super().__init__()
        filterNum = 200
        self.layer_1 = torch.nn.Sequential(
            torch.nn.Conv1d(in_channels=num_channel, out_channels=filterNum, kernel_size=5, stride=2),
            torch.nn.BatchNorm1d(filterNum),
            torch.nn.GELU(),
            torch.nn.MaxPool1d(kernel_size=2, stride=2)
        )
        self.layer_block = torch.nn.Sequential(
            torch.nn.Conv1d(in_channels=filterNum, out_channels=filterNum, kernel_size=5, stride=2),
            torch.nn.BatchNorm1d(filterNum),
            torch.nn.GELU(),
            torch.nn.MaxPool1d(kernel_size=2, stride=2)
        )
        self.dropout = torch.nn.Dropout(0.25)
        self.fc1 = torch.nn.Linear(600, 1024)
        self.fc2 = torch.nn.Linear(1024, 1024)
        self.fc3 = torch.nn.Linear(1024, num_target)
    
    def forward(self, x):
        x = x.to(torch.float32)
        # 1D CNN.
        x = self.layer_1(x)
        x = self.layer_block(x)
        x = self.layer_block(x)
        # MLP.
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        x = self.dropout(x)
        x = self.fc2(x)
        x = self.fc3(x)

        return x
    
class CNN2D(torch.nn.Module):
    """2D-CNN model for age and gender estimation.
    """

    def __init__(self, num_channel=2, num_target=2) -> None:
        """Groundtruth class initialization.

        References
        ----------
        [1] Mostafa, A., Elsagheer, S. A., & Gomaa, W. (2021). BioDeep: A Deep Learning System for IMU-based Human Biometrics Recognition. In ICINCO (pp. 620-629).

        Parameters
        ----------
        num_channel: Number of channels of the input data. size=[1].
        num_target: Number of output targets. size=[1].

        Returns
        -------

        """

        super().__init__()
        self.layer_1 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=num_channel, out_channels=32, kernel_size=3, stride=1),
            #torch.nn.BatchNorm2d(32)
            torch.nn.GELU(),
            torch.nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.layer_2 = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=2),
            #torch.nn.BatchNorm2d(64),
            torch.nn.GELU()
        )
        self.layer_block = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=2),
            #torch.nn.BatchNorm2d(64),
            torch.nn.GELU(),
            torch.nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.dropout = torch.nn.Dropout(0.25)
        self.fc1 = torch.nn.Linear(256, 256)
        self.fc2 = torch.nn.Linear(256, num_target)
    
    def forward(self, x):
        x = x.to(torch.float32)
        # 2D CNN.
        x = self.layer_1(x)
        x = self.layer_2(x)
        x = self.layer_block(x)
        x = self.layer_block(x)
        # MLP.
        x = x.contiguous().view(x.size(0), -1)
        x = self.fc1(x)
        x = self.dropout(x)
        x = self.fc2(x)

        return x