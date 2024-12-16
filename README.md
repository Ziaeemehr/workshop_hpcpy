# High-Performance Computing with Python, TNG

This repository demonstrates how to set up a Python environment for high-performance computing tasks. It leverages tools like **NumPy**, **Numba**, and **CuPy** for fast numerical computations and includes **SWIG** for integrating C++ code with Python. 

The package is optimized for both CPU and GPU-based systems, with seamless GPU acceleration provided by **CuPy** (if a CUDA-compatible GPU is available).

---

## Features
- **NumPy** for numerical computing.
- **Numba** for just-in-time compilation to speed up Python code.
- **CuPy** for GPU-accelerated numerical computations (optional).
- **scikit-learn** for machine learning and data analysis.
- **SWIG** for wrapping C++ code to be accessible in Python.

---

## Installation Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/Ziaeemehr/workshop_hpcpy.git
cd  workshop_hpcpy
```

### Step 2: Create a Conda Environment
1. Ensure that **conda** is installed on your system. If not, download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/).
2. Create a new environment named `hpc_env`:
   
   ```bash
   conda env create environment.yml
   ```
   or
   ```bash
   conda create -n hpc_env python=3.10 -y
   ```
3. Activate the environment:
   ```bash
   conda activate hpc_env
   ```

---

### Step 3: Install Dependencies
```bash
# no need for this step if used yml file.
conda install PACKAGE_NAME
conda install anaconda::scikit-learn 
conda install anaconda::networkx
conda install conda-forge::matplotlib
conda install conda-forge::numba  # install from specific channel
conda install conda-forge::swig # OPTIONAL, for C++ wrapping
conda install anaconda::ipykernel
```

For more details on installing CuPy with specific CUDA versions, see the [CuPy installation guide](https://docs.cupy.dev/en/stable/install.html).

---

### Step 4: Verify Installation
Run the following Python script to verify that the key libraries are installed and working:
```python
import numpy as np
from numba import jit
try:
    import cupy as cp
    gpu_available = True
except ImportError:
    gpu_available = False

print(f"NumPy version: {np.__version__}")
print(f"Numba JIT test: {jit(lambda x: x)(42)}")
print(f"CuPy available: {gpu_available}")
```

```bash
$ which swig # show the path if swig is available
```

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Related resources
- [PythonHPC, CSCS](https://github.com/eth-cscs/PythonHPC)
- [High-performance computing with Python, JSC](https://gitlab.jsc.fz-juelich.de/sdlbio-courses/hpc-python/-/tree/2022)

## Contributing
Feel free to submit issues, fork the repository, and send pull requests. All contributions are welcome!

---

## Contact
For any questions, please reach out at a.ziaeemrhr[AT]gmail[dot]com.
