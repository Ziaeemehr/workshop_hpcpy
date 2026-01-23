#!/usr/bin/env python3
"""
Gathering Dictionary Example - MPI4py
Demonstrates how to gather dictionaries from all MPI processes to the root process.
Each process creates a dictionary with process-specific data and sends it to root.
Root process collects all dictionaries.
"""

from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
root = 0

# Each process creates a dictionary with its own data
local_dict = {
    "rank": rank,
    "process_name": f"Process_{rank}",
    "data": [rank * i for i in range(3)],
    "value": rank * 10
}

print(f"Rank {rank}: {local_dict}")

# Gather all dictionaries from all processes to root
# comm.gather() collects data from all processes
gathered_dicts = comm.gather(local_dict, root=root)

# Only root process has the collected data
if rank == root:
    print("\n" + "="*50)
    print("GATHERED DICTIONARIES AT ROOT:")
    print("="*50)
    for i, d in enumerate(gathered_dicts):
        print(f"Dictionary from rank {i}: {d}")
    
    print("\n" + "="*50)
    print("SUMMARY:")
    print("="*50)
    print(f"Total processes: {size}")
    print(f"All ranks collected: {[d['rank'] for d in gathered_dicts]}")
    print(f"All values collected: {[d['value'] for d in gathered_dicts]}")
