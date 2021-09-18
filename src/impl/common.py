import typing as t

import torch


def generate_noise(size: t.Tuple, device: str = 'cpu'):
    """
    Given the size and device to create tensor on,
    generate a random noise tensor which serves as the input
    to the generator
    Args:
        size: The dimensions of the random noise tensor
        device: The device to create the random noise tensor
    Returns:
        A random noise tensor created on the target device
    """
    return torch.randn(size, device=device)
