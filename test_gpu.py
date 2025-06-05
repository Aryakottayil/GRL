import torch
print("PyTorch version:", torch.__version__)
print("CUDA version in torch:", torch.version.cuda)
print("CUDA available?", torch.cuda.is_available())
print("Device:", torch.device("cuda" if torch.cuda.is_available() else "cpu"))
