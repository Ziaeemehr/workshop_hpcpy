# MPI4py Examples - Complete Reference

This directory contains comprehensive MPI (Message Passing Interface) examples using mpi4py in Python. All scripts have been reviewed, documented, and tested for correctness.

## Quick Start

### Prerequisites
```bash
conda activate hpc
# Install OpenMPI (if not already installed)
conda install -c conda-forge openmpi mpi4py
```

### Running Examples
```bash
# Basic example with 2 processes
mpirun -np 2 python 00_send_recieve.py

# Advanced example with 4 processes  
mpirun -np 4 python 08_scattering_np_array.py
```

## Directory Structure

### Point-to-Point Communication (Rank-Specific)

#### **00_send_recieve.py** ✅
- **Topic**: Blocking Send/Receive
- **Description**: Process 0 sends a dictionary to Process 1
- **Key Concepts**: `send()`, `recv()`, blocking I/O
- **Usage**: `mpirun -np 2 python 00_send_recieve.py`

#### **01_send_recieve_nonblocking.py** ✅
- **Topic**: Non-Blocking (Asynchronous) Send/Receive  
- **Description**: Process 0 and 1 use `isend()`/`irecv()` with `wait()` for synchronization
- **Key Concepts**: `isend()`, `irecv()`, asynchronous communication, `wait()`
- **Usage**: `mpirun -np 2 python 01_send_recieve_nonblocking.py`

#### **02_send_np_array.py** ✅
- **Topic**: Send/Receive Numpy Arrays
- **Description**: Efficient transfer of numpy arrays between processes using typed buffers
- **Key Concepts**: `Isend()`, `Irecv()`, MPI type specification, numpy integration
- **Usage**: `mpirun -np 2 python 02_send_np_array.py`

---

### Collective Communication (All Processes)

#### **03_bcast.py** ✅
- **Topic**: Broadcast
- **Description**: Root process broadcasts complex data (dictionaries, lists) to all processes
- **Key Concepts**: `bcast()`, collective operations, shared data distribution
- **Usage**: `mpirun -np 4 python 03_bcast.py`
- **Output**: All processes receive identical data from root

#### **04_scattering_obj.py** ✅
- **Topic**: Scatter Objects
- **Description**: Root distributes different objects to each process
- **Key Concepts**: `scatter()`, one-to-all distribution, verification
- **Usage**: `mpirun -np 4 python 04_scattering_obj.py`
- **Output**: Each rank receives `(rank+1)^2`

#### **04_scattering_dictionary.py** ✅
- **Topic**: Scatter Dictionary of Arrays
- **Description**: Root scatters a list of dictionaries (each containing numpy arrays)
- **Key Concepts**: `scatter()`, complex data types, heterogeneous data
- **Usage**: `mpirun -np 2 python 04_scattering_dictionary.py`

#### **08_scattering_np_array.py** ✅
- **Topic**: Scatter 2D Numpy Arrays
- **Description**: Root scatters rows of a 2D array to each process
- **Key Concepts**: `Scatter()`, 2D arrays, row-wise distribution
- **Usage**: `mpirun -np 4 python 08_scattering_np_array.py`

#### **10_scattering_3D_np_array.py** ✅
- **Topic**: Scatter 3D Numpy Arrays
- **Description**: Root scatters 2D slices of a 3D array (first dimension used for distribution)
- **Key Concepts**: `Scatter()`, 3D arrays, multidimensional data handling
- **Usage**: `mpirun -np 4 python 10_scattering_3D_np_array.py`

#### **05_gathering_obj.py** ✅
- **Topic**: Gather Objects
- **Description**: Each process sends a scalar value to root, root collects all
- **Key Concepts**: `gather()`, many-to-one collection, list of results
- **Usage**: `mpirun -np 4 python 05_gathering_obj.py`
- **Output**: Root receives `[(1)^2, (2)^2, (3)^2, (4)^2] = [1, 4, 9, 16]`

#### **05_gathering_array.py** ✅
- **Topic**: Gather Variable-Sized Arrays
- **Description**: Each process creates arrays of different sizes; root collects all
- **Key Concepts**: `gather()`, `Gatherv()`, variable-length data, size negotiation
- **Usage**: `mpirun -np 4 python 05_gathering_array.py`
- **Workflow**: 
  1. Each process sends its array size to root
  2. Root allocates buffer based on total size
  3. Gatherv() collects variable-sized arrays

#### **05_gathering_list.py** ✅
- **Topic**: Gather Lists of Objects
- **Description**: Each process creates a list of strings; root collects all lists
- **Key Concepts**: `gather()`, list collection, structured data
- **Usage**: `mpirun -np 4 python 05_gathering_list.py`

#### **11_gathering_np_array.py** ✅
- **Topic**: Gather Equal-Sized Numpy Arrays
- **Description**: Each process sends same-sized array; root forms 2D array from rows
- **Key Concepts**: `Gather()`, row stacking, uniform data
- **Usage**: `mpirun -np 4 python 11_gathering_np_array.py`

#### **12_gathering_3D_np_array.py** ✅
- **Topic**: Gather 3D Numpy Arrays
- **Description**: Each process sends 2D array; root stacks into 3D array
- **Key Concepts**: `Gather()`, 3D stacking, multidimensional collection
- **Usage**: `mpirun -np 4 python 12_gathering_3D_np_array.py`

#### **06_broadcasting_np_array.py** ✅
- **Topic**: Broadcast Numpy Arrays (Typed)
- **Description**: Root broadcasts large numpy array using typed buffer `Bcast()`
- **Key Concepts**: `Bcast()`, typed buffers, efficient numpy broadcasting
- **Usage**: `mpirun -np 4 python 06_broadcasting_np_array.py`
- **Difference**: `Bcast()` (capital B) vs `bcast()` - typed vs pickle-based

---

### PyTorch Integration (Optional)

#### **07_broadcasting_torch.py** ⚠️
- **Topic**: Broadcast PyTorch Tensors
- **Description**: Root broadcasts torch tensor to all processes
- **Requirements**: `conda install pytorch -c pytorch`
- **Key Concepts**: `bcast()`, torch tensor handling, automatic conversion
- **Usage**: `mpirun -np 2 python 07_broadcasting_torch.py`
- **Status**: Graceful fallback if torch not installed

#### **09_scattering_tensor.py** ⚠️
- **Topic**: Scatter PyTorch Tensors
- **Description**: Root scatters tensor rows to processes, converted via numpy
- **Requirements**: `conda install pytorch -c pytorch`
- **Key Concepts**: `Scatter()`, tensor↔numpy conversion, GPU-aware MPI
- **Usage**: `mpirun -np 4 python 09_scattering_tensor.py`
- **Status**: Graceful fallback if torch not installed

---

### Advanced Patterns

#### **13_scatter_list_of_arry_gather_list_of_array.py** ✅
- **Topic**: MPI + Local Multiprocessing Hybrid
- **Description**: Combines MPI scatter/gather with local multiprocessing pools
- **Workflow**:
  1. Root scatters data chunks to MPI processes
  2. Each MPI process uses local multiprocessing pool for parallel processing
  3. Each process gathers results back to root
- **Key Concepts**: MPI collective ops, local parallelism, hybrid parallelism
- **Usage**: `mpirun -np 4 python 13_scatter_list_of_arry_gather_list_of_array.py`

---

## MPI Concepts Summary

### Communication Patterns

| Pattern | Function | Direction | Blocking |
|---------|----------|-----------|----------|
| Send | `send()` / `Send()` | One→One | Yes |
| Send Async | `isend()` / `Isend()` | One→One | No |
| Receive | `recv()` / `Recv()` | One→One | Yes |
| Receive Async | `irecv()` / `Irecv()` | One→One | No |
| Broadcast | `bcast()` / `Bcast()` | One→All | Yes |
| Scatter | `scatter()` / `Scatter()` | One→All (different) | Yes |
| Gather | `gather()` / `Gather()` | All→One | Yes |
| Gatherv | `Gatherv()` | All→One (variable-sized) | Yes |

### Function Naming Convention

- **Lowercase** (`send()`, `bcast()`): Pickle-based, works with any Python object
- **Uppercase** (`Send()`, `Bcast()`): Typed, works with numpy arrays, faster
- **Async variants**: `i` prefix (`isend()`, `irecv()`, `Isend()`, `Irecv()`)
- **Variable-length**: `v` suffix (`Gatherv()`, `Scatterv()`)

### Data Types

```python
from mpi4py import MPI

# Common MPI types for numpy
MPI.INT      # int32
MPI.LONG     # int64  
MPI.FLOAT    # float32
MPI.DOUBLE   # float64
MPI.CHAR     # byte
```

---

## Testing

All scripts have been tested and verified to:
- ✅ Run without errors
- ✅ Produce correct output
- ✅ Include clear documentation
- ✅ Have inline comments explaining key operations
- ✅ Display verification messages (✓)

### Run All Tests
```bash
for script in *.py; do
    echo "Testing $script..."
    mpirun -np 2 python "$script"
done
```

---

## Best Practices

### Do's ✅
- Always use communicators: `comm = MPI.COMM_WORLD`
- Get rank and size: `rank = comm.Get_rank()`, `size = comm.Get_size()`
- Use `wait()` after async operations
- Check rank before printing (rank 0 usually prints)
- Use capital letter versions with numpy arrays
- Handle torch import gracefully with try/except

### Don'ts ❌
- Don't use bare `print()` - rank 0 gets cluttered with output
- Don't forget `wait()` after `isend()` or `irecv()`
- Don't mix send/recv in ways that cause deadlock
- Don't assume data types (be explicit with MPI types)

---

## Running with Different Process Counts

```bash
# 2 processes (good for point-to-point examples)
mpirun -np 2 python 00_send_recieve.py

# 4 processes (good for collective communication)
mpirun -np 4 python 03_bcast.py

# 8 processes (stress test)
mpirun -np 8 python 08_scattering_np_array.py
```

---
