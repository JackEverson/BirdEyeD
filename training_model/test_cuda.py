import torch


if torch.cuda.is_available():
    print('cuda available')
else:
    print('cuda not available')