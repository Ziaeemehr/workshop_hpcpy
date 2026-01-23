#!/usr/bin/env python3
"""
Point-to-Point Communication: Non-Blocking Send/Receive
Demonstrates non-blocking (asynchronous) send and receive operations.
Process 0 uses isend() and Process 1 uses irecv() to allow computation to continue
while communication happens in the background. Both call wait() to synchronize.
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    # Process 0: Non-blocking send
    data = {'a': 7, 'b': 3.14}
    req = comm.isend(data, dest=1, tag=11)
    print(f"Rank {rank}: Started sending data {data}")
    req.wait()  # Wait for send to complete
    print(f"Rank {rank}: Send completed")
    
elif rank == 1:
    # Process 1: Non-blocking receive
    print(f"Rank {rank}: Started receiving...")
    req = comm.irecv(source=0, tag=11)
    data = req.wait()  # Wait and get the data
    print(f"Rank {rank}: Received data {data}")

# execute: mpirun -np 2 python 01_send_recieve_nonblocking.py
# output:
# Rank 0: Started sending data {'a': 7, 'b': 3.14}
# Rank 1: Started receiving...
# Rank 0: Send completed
# Rank 1: Received data {'a': 7, 'b': 3.14}