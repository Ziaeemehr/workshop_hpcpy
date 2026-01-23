#!/usr/bin/env python3
"""
Collective Communication: Gather 3D Numpy Arrays
Each process creates a 2D array (2x3) filled with its rank number.
All 2D arrays are gathered to root, forming a 3D array (size x 2 x 3).
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

row = 2
col = 3
# Each process creates 2D array filled with its rank
sendbuf = np.zeros((row, col), dtype=np.float32) + rank
recvbuf = None 

if rank == 0:
    # Root allocates 3D receive buffer
    recvbuf = np.empty((size, row, col), dtype=np.float32)

print(f"Rank {rank}: sending (2,3) array filled with {rank}")

# Gather all 2D arrays to root (forming 3D array)
comm.Gather(sendbuf, recvbuf, root=0)

if rank == 0:
    # Verify all data
    for i in range(size):
        assert(np.allclose(recvbuf[i, :, :], i)), f"Slice {i} mismatch"
    print(f"\n✓ All 3D arrays gathered (shape {recvbuf.shape}):")
    print(recvbuf)

# execute: mpirun -np 4 python 12_gathering_3D_np_array.py

