import torch.nn
from torch import nn

class Network(nn.Module):
    def __init__(self):
        super(Network, self).__init__()
        self.layer1 = nn.Linear(150, 100)
        self.relu1 = nn.ReLU()

        self.layer2 = nn.Linear(100, 64)
        self.relu2 = nn.ReLU()

        self.layer3 = nn.Linear(64, 32)
        self.relu3 = nn.ReLU()

        self.layer4 = nn.Linear(32, 12)
        self.relu4 = nn.ReLU()

        self.layer_last = nn.Linear(12, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.relu1(self.layer1(x))  # Layer 1 with ReLU
        x = self.relu2(self.layer2(x))  # Layer 2 with ReLU
        x = self.relu3(self.layer3(x))  # Layer 3 with ReLU
        x = self.relu4(self.layer4(x))  # Layer 4 with ReLU
        x = self.sigmoid(self.layer_last(x))  # Final output with Sigmoid

        return x
