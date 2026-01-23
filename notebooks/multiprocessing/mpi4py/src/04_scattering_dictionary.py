#!/usr/bin/env python3
"""
Collective Communication: Scatter Dictionary of Arrays
Root process creates a list of dictionaries (each containing numpy arrays).
Each dictionary is scattered to a different process.
For N processes: root has N dictionaries, each process gets 1.
"""

from collections import OrderedDict
from mpi4py import MPI
import numpy as np 

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    # Create a list of dictionaries on root
    # Each dictionary will go to one process
    data = [{"a": np.ones(5) * 2}, {"b": np.ones(5) * 3}]
else:
    data = None

# Scatter: each process gets one dictionary
data = comm.scatter(data, root=0)
print(f"Rank {rank}: {data}")

# execute: mpirun -np 2 python 04_scattering_dictionary.py
# output: 
# Rank 0: {'a': array([2., 2., 2., 2., 2.])}
# Rank 1: {'b': array([3., 3., 3., 3., 3.])}
