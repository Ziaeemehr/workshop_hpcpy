#!/usr/bin/env python3
"""
Collective Communication: Broadcast Numpy Array
Root process broadcasts a large numpy array (0-99) to all other processes.
Uses Bcast() (capital B) for efficient numpy array broadcasting.
All processes end up with the same array.
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = np.arange(100, dtype='i')
    print(f"Rank {rank}: broadcasting array [0..99]")
else:
    data = np.empty(100, dtype='i')

# Broadcast array from root to all processes
comm.Bcast(data, root=0)

# Verify all processes have correct data
for i in range(100):
    assert(data[i] == i), f"Rank {rank}: data[{i}]={data[i]}, expected {i}"

print(f"Rank {rank}: ✓ verified array [0..99]")

# execute: mpirun -np 4 python 06_broadcasting_np_array.py