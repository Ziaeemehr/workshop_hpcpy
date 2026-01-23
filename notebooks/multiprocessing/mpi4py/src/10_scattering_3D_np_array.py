#!/usr/bin/env python3
"""
Collective Communication: Scatter 3D Numpy Arrays
Root process scatters slices of a 3D array to all processes.
The scatter operation uses the first dimension to distribute data.
Each process receives a (2x3) sub-array filled with its rank number.
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

sendbuf = None
if rank == 0:
    # Root creates 3D array where each (2,3) slice is filled with its index
    sendbuf = np.empty((size, 2, 3), dtype=np.float32)
    for i in range(size):
        sendbuf[i, :, :] = i
    print(f"Rank {rank}: Scattering 3D array shape {sendbuf.shape}")

# Each process receives one 2D slice (2, 3)
recvbuf = np.empty((2, 3), dtype=np.float32)
comm.Scatter(sendbuf, recvbuf, root=0)

# Verify correctness
expected = rank * np.ones((2, 3), dtype=np.float32)
assert(np.allclose(recvbuf, expected)), f"Rank {rank}: mismatch"
print(f"Rank {rank}: ✓ received (2,3) array filled with {rank}")

# execute: mpirun -np 4 python 10_scattering_3D_np_array.py
