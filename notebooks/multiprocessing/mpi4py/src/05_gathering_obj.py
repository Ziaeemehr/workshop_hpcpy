#!/usr/bin/env python3
"""
Collective Communication: Gather Python Objects
Root process collects scalar values from all processes.
Each process computes (rank+1)^2 and sends it to root.
Root verifies all values and prints them.
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Each process computes (rank+1)^2
data = (rank+1)**2
print(f"Rank {rank}: computed value {data}")

# Gather all values to root
data = comm.gather(data, root=0)

if rank == 0:
    print(f"\nRoot received: {data}")
    # Verify correctness
    for i in range(size):
        expected = (i+1)**2
        assert(data[i] == expected), f"Error at rank {i}"
    print(f"✓ All values verified: {[(i+1)**2 for i in range(size)]}")
else:
    assert(data is None), f"Non-root rank {rank} should receive None"
    print(f"Rank {rank}: correctly received None after gather")

# execute: mpirun -np 4 python 05_gathering_obj.py
