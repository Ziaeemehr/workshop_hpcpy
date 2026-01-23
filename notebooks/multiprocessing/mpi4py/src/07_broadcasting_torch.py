#!/usr/bin/env python3
"""
Collective Communication: Broadcast PyTorch Tensor
Root process broadcasts a PyTorch tensor to all other processes.
PyTorch tensors are automatically converted by mpi4py.

Note: Requires PyTorch installation
  conda install pytorch -c pytorch
"""

from mpi4py import MPI
import numpy as np

try:
    import torch
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False
    print("WARNING: PyTorch not installed. Install with: conda install pytorch -c pytorch")

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if TORCH_AVAILABLE:
    if rank == 0:
        data = torch.arange(5, dtype=torch.float32)
        print(f"Rank {rank}: broadcasting torch tensor {data.tolist()}")
    else:
        data = None

    # Broadcast tensor from root to all processes
    x = comm.bcast(data, root=0)
    print(f"Rank {rank}: received tensor {x}")
else:
    print(f"Rank {rank}: torch not available, skipping test")

# execute: mpirun -np 2 python 07_broadcasting_torch.py
# output:
# Rank 0: broadcasting torch tensor [0.0, 1.0, 2.0, 3.0, 4.0]
# Rank 1: received tensor tensor([0., 1., 2., 3., 4.])

