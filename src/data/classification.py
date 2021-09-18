"""
Datasets for classification tasks
"""
from torchvision.datasets import (
    mnist
)


def get_dataloader():
    pass


def get_mnist(train: bool = True, path: str = None):
    return mnist.MNIST(root=path, train=train)

