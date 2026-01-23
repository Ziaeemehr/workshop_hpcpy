#!/usr/bin/env python3
"""
Collective Communication: Gather Variable-Sized Arrays
Demonstrates gathering arrays of different sizes from all processes to root.
Uses comm.gather() to collect sizes, then Gatherv() to gather variable-sized arrays.
Each process creates an array filled with its rank, with random length (2-5).
"""

import random
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
root = 0

# Create a random sized array filled with rank number
local_array = [rank] * random.randint(2, 5)
sendbuf = np.array(local_array)
print(f"Rank {rank}: local_array size={len(sendbuf)}, data={local_array}")

# Step 1: Gather array sizes to root
sendcounts = np.array(comm.gather(len(sendbuf), root))

if rank == root:
    print(f"\nRoot received sizes: {sendcounts}, total elements: {sum(sendcounts)}")
    # Allocate receive buffer on root based on collected sizes
    recvbuf = np.empty(sum(sendcounts), dtype=int)
else:
    recvbuf = None

# Step 2: Gather variable-sized arrays to root
comm.Gatherv(sendbuf=sendbuf, recvbuf=(recvbuf, sendcounts), root=root)

if rank == root:
    print(f"Gathered array: {recvbuf}")

# execute: mpirun -np 4 python 05_gathering_array.py