#!/usr/bin/env python3
"""
Advanced MPI Pattern: Scatter Array List + Process with Multiprocessing + Gather Results
Demonstrates a complex workflow combining MPI scatter/gather with local multiprocessing.

Workflow:
1. Root splits data into chunks and scatters to all MPI processes
2. Each MPI process uses local multiprocessing pool to process its chunk
3. Each process sends results back to root, which gathers and concatenates them
"""

import numpy as np
from mpi4py import MPI
import multiprocessing as mp

SEED = 42
np.random.seed(SEED)

def single_task(theta_i):
    """Local computation on one data item"""
    x = 2 * theta_i
    return x

def batch_run(theta_batch):
    """Process a batch of data using local multiprocessing pool"""
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    with mp.Pool(processes=2) as pool:
        results = pool.map(single_task, theta_batch)
    return np.array(results), rank

# Create random input data
theta = np.random.rand(10, 2)

# MPI setup
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
sendbuf = None

# Step 1: Root scatters data chunks to all processes
if rank == 0:
    print(f"Original data shape: {theta.shape}")
    # Split data into chunks for each process
    sendbuf = np.array_split(theta, size, axis=0)

data_chunk = comm.scatter(sendbuf, root=0)

# Step 2: Each process processes its chunk
result, rank_id = batch_run(data_chunk)
print(f"Rank {rank}: processed {data_chunk.shape} → {result.shape}")

# Step 3: Gather all results back to root
gathered = comm.gather(result, root=0)

# Step 4: Root concatenates and displays results
if rank == 0:
    gathered = np.concatenate(gathered, axis=0)
    print(f"\n✓ Final gathered result shape: {gathered.shape}")
    print(f"Data (first 3 rows):\n{gathered[:3]}")

# execute: mpirun -np 4 python 13_scatter_list_of_arry_gather_list_of_array.py

