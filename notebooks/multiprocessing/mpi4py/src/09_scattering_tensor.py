#!/usr/bin/env python3
"""
Collective Communication: Scatter and Receive PyTorch Tensors
Root process scatters PyTorch tensors to all processes by converting to numpy.
Each process receives a tensor, converts from numpy back to tensor.

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

if TORCH_AVAILABLE:
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    sendbuf = None
    if rank == 0:
        # Root creates tensor where each row has the row index value
        sendbuf = torch.empty([size, 5], dtype=torch.float32)
        sendbuf.T[:,:] = torch.arange(size, dtype=torch.float32) 
        sendbuf = sendbuf.numpy()
        print(f"Rank {rank}: Scattering tensors")

    # Each process receives one row as numpy array
    recvbuf = np.empty(5, dtype=np.float32)
    comm.Scatter(sendbuf, recvbuf, root=0)
    
    # Convert back to tensor
    recvbuf = torch.from_numpy(recvbuf)
    
    # Verify
    expected = torch.tensor(rank, dtype=torch.float32)
    assert(torch.allclose(recvbuf, expected)), f"Rank {rank}: mismatch"
    print(f"Rank {rank}: ✓ received tensor {recvbuf.tolist()}")
else:
    print("PyTorch not available, skipping test")

# execute: mpirun -np 4 python 09_scattering_tensor.py

