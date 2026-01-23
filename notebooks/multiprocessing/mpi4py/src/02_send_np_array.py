#!/usr/bin/env python3
"""
Point-to-Point Communication: Non-Blocking Numpy Array Send/Receive
Demonstrates how to send and receive numpy arrays between two processes.
Uses Isend/Irecv (capital I) which work efficiently with typed data (numpy arrays).
Process 0 sends an integer array [0,1,2,3,4] to Process 1.
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
n = 5

if rank == 0:
    # Process 0: Send numpy array to Process 1
    data = np.arange(n, dtype='i')  # Integer array [0, 1, 2, 3, 4]
    req = comm.Isend([data, MPI.INT], dest=1, tag=77)
    print(f"Rank {rank}: Sent array {data}")
    req.wait()
    
elif rank == 1:
    # Process 1: Receive numpy array from Process 0
    data = np.empty(n, dtype='i')
    req = comm.Irecv([data, MPI.INT], source=0, tag=77)
    req.wait()
    print(f"Rank {rank}: Received array {data}")

# execute: mpirun -np 2 python 02_send_np_array.py
# output:
# Rank 0: Sent array [0 1 2 3 4]
# Rank 1: Received array [0 1 2 3 4]

