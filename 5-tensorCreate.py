import torch
x = torch.tensor([[1,2,3],[4,5,6]])
y = torch.tensor([[7,8,9],[10,11,12]])
z = x + y
print(z)
# out:
# tensor([[ 8, 10, 12],
# [14, 16, 18]])
print(z.size())
