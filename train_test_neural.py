import torch
from torch import nn, optim

from dataset import get_test_train
from network import Network


X_train, y_train, X_test, y_test = get_test_train()

model = Network()
model.train()
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

batches = list(torch.split(X_train, 64))
batches_of_labels = list(torch.split(y_train, 64))

def train_then_test():
    for epoch in range(20):
        for i in range (len(batches)):
            optimizer.zero_grad()
            outputs = model(batches[i])
            loss = loss_fn(outputs, batches_of_labels[i])
            loss.backward()
            optimizer.step()
            print(epoch, loss.item())

    model.eval()
    with torch.no_grad():
        outputs = model(torch.tensor(X_test))
        acc = (outputs == torch.tensor(y_test)).float().mean().item()

        print("\nAccuracy = ")
        print(acc * 100)
        return acc

train_then_test()