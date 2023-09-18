import torch
import torch.nn as nn
model_path = "./training_model/cifar_net.pth"


if __name__ == "__main__":
     
    class Net(nn.Module):
        # models a simple Convolutional Neural Network
        def __init__(self):
            # initalize the Network
            super(Net, self).__init__()
            # 3 input image channel, 12 output channels, 5x5 square convolution kernel
            self.conv1 = nn.Conv2d(3, 12, 5)
            # max pooling over a (2, 2) Window to give a 5X5 image
            self.pool = nn.MaxPool2d(2, 2)
            self.conv2 = nn.Conv2d(12, 16, 5)
            self.fc1 = nn.Linear(16 * 5 * 5, 120)# 5x5 from image dimension
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 10)

        def forward(self, x):
            # forward propagation algorithm
            x = self.pool(F.relu(self.conv1(x)))
            x = self.pool(F.relu(self.conv2(x)))
            x = x.view(-1, 16 * 5 * 5)
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.fc3(x)
            return x

    net = Net()
    net.load_state_dict(torch.load(model_path))
    net.eval()

    print(net)

    net.forward()
