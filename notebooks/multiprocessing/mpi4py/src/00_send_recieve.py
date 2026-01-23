#!/usr/bin/env python3
"""
Point-to-Point Communication: Blocking Send/Receive
Demonstrates basic blocking send and receive operations between two processes.
Process 0 sends a dictionary to Process 1, which receives and prints it.
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
root = 0

if rank == 0:
    # Process 0: Send a dictionary to Process 1
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1, tag=11)
    print(f"Rank {rank}: Sent data {data}")
    
elif rank == 1:
    # Process 1: Receive the dictionary from Process 0
    data = comm.recv(source=0, tag=11)
    print(f"Rank {rank}: Received data {data}")

# execute: mpirun -np 2 python 00_send_recieve.py
# output: 
# Rank 0: Sent data {'a': 7, 'b': 3.14}
# Rank 1: Received data {'a': 7, 'b': 3.14}
