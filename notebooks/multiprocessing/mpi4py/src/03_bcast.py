#!/usr/bin/env python3
"""
Collective Communication: Broadcast
Root process (rank 0) broadcasts a complex dictionary to all other processes.
All processes end up with the same dictionary data.
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Only rank 0 initializes the data
if rank == 0:
    data = {'key1': [7, 2.72, 2+3j],
            'key2': ( 'abc', 'xyz')}
else:
    data = None

# Broadcast data from root (rank 0) to all other processes
data = comm.bcast(data, root=0)
print(f"Rank {rank}: {data}")

# execute: mpirun -np 4 python 03_bcast.py
# output: 
# Rank 0: {'key1': [7, 2.72, (2+3j)], 'key2': ('abc', 'xyz')}
# Rank 1: {'key1': [7, 2.72, (2+3j)], 'key2': ('abc', 'xyz')}
# Rank 2: {'key1': [7, 2.72, (2+3j)], 'key2': ('abc', 'xyz')}
# Rank 3: {'key1': [7, 2.72, (2+3j)], 'key2': ('abc', 'xyz')}