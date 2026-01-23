#!/usr/bin/env python3
"""
Scattering Objects - MPI4py
Demonstrates how to scatter different objects to each process.
Root process creates a list where each element is (rank+1)^2.
Each process receives one element.
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    # Create data: [1, 4, 9, 16, ...] for 4 processes: [(0+1)^2, (1+1)^2, ...]
    data = [(i+1)**2 for i in range(size)]
else:
    data = None

# Scatter data: each rank gets one element
data = comm.scatter(data, root=0)

# Verify each process received the correct value
expected = (rank+1)**2
assert(data == expected), f"Rank {rank}: expected {expected}, got {data}"
print(f"Rank {rank}: received {data} (expected {expected}) ✓")

# execute: mpirun -np 4 python 04_scattering_obj.py
