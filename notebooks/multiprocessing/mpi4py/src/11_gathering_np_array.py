#!/usr/bin/env python3
"""
Collective Communication: Gather Equal-Sized Numpy Arrays
Each process creates an array filled with its rank number.
All arrays are gathered to the root process, forming a 2D array.
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

n = 5
# Each process creates array filled with its rank
sendbuf = np.zeros(n, dtype=np.float32) + rank
recvbuf = None 

if rank == 0:
    # Root allocates receive buffer for all arrays
    recvbuf = np.empty((size, n), dtype=np.float32)

print(f"Rank {rank}: sending {sendbuf}")

# Gather all arrays to root
comm.Gather(sendbuf, recvbuf, root=0)

if rank == 0:
    # Verify all data
    for i in range(size):
        assert(np.allclose(recvbuf[i, :], i)), f"Row {i} mismatch"
    print(f"\n✓ All arrays gathered:")
    print(recvbuf)

# execute: mpirun -np 4 python 11_gathering_np_array.py
