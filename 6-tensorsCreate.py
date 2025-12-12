import numpy
import torch
# Created from preexisting arrays
w = torch.tensor([1,2,3])
w = torch.tensor((1,2,3))
w = torch.tensor(numpy.array([1,2,3]))
# Initialized by size
w = torch.empty(100,200)
w = torch.zeros(100,200)
w = torch.ones(100,200)
