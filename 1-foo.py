import torch

# Check if GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"

# Create a 3x3 matrix of random numbers
x = torch.rand(3, 3).to(device)

print(f"Tensor on {device}:\n{x}")
