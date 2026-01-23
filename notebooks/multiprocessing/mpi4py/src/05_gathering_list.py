#!/usr/bin/env python3
"""
Collective Communication: Gather Lists of Objects
Root process collects lists from all processes.
Each process creates a list of strings, all lists are gathered to root.
"""

from mpi4py import MPI

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Create a list of objects on each process
my_objects = [f"object_{rank}_{i}" for i in range(3)]
print(f"Rank {rank}: created list {my_objects}")

# Gather all lists onto the root process
all_objects = comm.gather(my_objects, root=0)

# Print the results on the root process
if rank == 0:
    print("\n" + "="*50)
    print("ALL OBJECTS GATHERED AT ROOT:")
    print("="*50)
    for i, obj_list in enumerate(all_objects):
        print(f"From rank {i}:")
        for obj in obj_list:
            print(f"  - {obj}")

