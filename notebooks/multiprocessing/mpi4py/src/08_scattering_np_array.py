#!/usr/bin/env python3
"""
Collective Communication: Scatter Numpy Arrays
Root process scatters equal-sized rows of a 2D array to all processes.
Each process receives one row filled with its rank number.
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

sendbuf = None
if rank == 0:
    # Root creates a 2D array where each row is filled with its row index
    sendbuf = np.empty([size, 5], dtype='i')
    sendbuf.T[:,:] = range(size) 
    print(f"Rank {rank}: Scattering array:\n{sendbuf}")

# Each process receives one row (5 elements)
recvbuf = np.empty(5, dtype='i')
comm.Scatter(sendbuf, recvbuf, root=0)

# Verify each process received the correct row
assert(np.allclose(recvbuf, rank)), f"Rank {rank}: received {recvbuf}, expected all {rank}"
print(f"Rank {rank}: ✓ received row {recvbuf}")

# execute: mpirun -np 4 python 08_scattering_np_array.py
