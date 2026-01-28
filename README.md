# High-Performance Computing with Python, TNG

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Ziaeemehr/workshop_hpcpy/main)

This repository demonstrates how to set up a Python environment for high-performance computing tasks. It leverages tools like **NumPy**, **Numba**, **JAX**, and **CuPy** for fast numerical computations and includes **SWIG** for integrating C++ code with Python. 

The package is optimized for both CPU and GPU-based systems, with seamless GPU acceleration provided by **CuPy** (if a CUDA-compatible GPU is available).

---

## Features
- **NumPy** for numerical computing.
- **Numba** for just-in-time compilation to speed up Python code.
- **JAX** for composable transformations of numerical code with automatic differentiation.
- **CuPy** for GPU-accelerated numerical computations (optional).
- **scikit-learn** for machine learning and data analysis.
- **SWIG** for wrapping C++ code to be accessible in Python.

## Notebooks

| Notebook | Description | Colab |
|----------|-------------|-------|
| Memory Profiling | Profiling memory usage with line profiler | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/profiling/mem_line_profiler.ipynb) |
| Multiprocessing | Using Python's multiprocessing module | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/multiprocessing/note_multiprocessing.ipynb) |
| Numba Euclidean | Computing Euclidean distance matrix with Numba | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/numba/euclidean-distance-matrix-numba.ipynb) |
| Numba Seed Fix | Fixing random seeds in Numba | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/numba/numba_fix_seed.ipynb) |
| Numba Vectorize | Vectorization with Numba | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/numba/numba_vectorize.ipynb) |
| Numba Primes | Generating prime numbers with Numba | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/numba/prime_numbers.ipynb) |
| Numba Vectorize Solution | Solution for Numba vectorization | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/numba/solutions/numba_vectorize.ipynb) |
| Numba CUDA Basics | Basics of CUDA programming with Numba | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/numba-cuda/1.numba-cuda-basics.ipynb) |
| Numba CUDA Performance | Performance analysis with Numba CUDA | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/numba-cuda/2.performance-analysis.ipynb) |
| Numba CUDA Memory | Memory optimization in Numba CUDA | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/numba-cuda/3.memory-optimization.ipynb) |
| CuPy Kuramoto model | Simulation of the Kuramoto model using CuPy for GPU acceleration | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/cupy/km_cupy.ipynb) |
| CuPy Introduction | Basics of CuPy for GPU computing | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/cupy/note.ipynb) |
| JAX Introduction | Introduction to JAX for numerical computing | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/jax/jax_intro.ipynb) |
| JAX Parallel | Parallel computing with JAX | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/jax/parallel_intro.ipynb) |
| JAX Vectorizing | Vectorization techniques in JAX | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/jax/vectorizing.ipynb) |
| JAX Random Generators | JAX's stateless random number generation | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/jax/random_generators.ipynb) |
| JAX Advanced Concepts | Advanced JAX features: PyTree, LAX, XLA, Scan | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/jax/advanced_concepts.ipynb) |
| SWIG Hello Example | SWIG example: Hello world | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/native-extentions/swig/example_1_hello/runme.ipynb) |
| SWIG Vector Example | SWIG example: Vector operations | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/native-extentions/swig/example_2_vector/runme.ipynb) |
| Pybind11 Intro | Introduction to Pybind11 for C++ bindings | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/native-extentions/pybind11/pybind11_intro.ipynb) |
| Cython Speedup | Speeding up Python code with Cython | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziaeemehr/workshop_hpcpy/blob/main/notebooks/native-extentions/cython/speeding_up__with_Cython.ipynb) |

---

## Installation Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/Ziaeemehr/workshop_hpcpy.git
cd  workshop_hpcpy
```

### Step 2: Create a Conda Environment
1. Ensure that **conda** is installed on your system. If not, download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/).
2. Create a new environment named `hpc`:
   
   ```bash
   conda create -n hpc python=3.11 -y
   ```
3. Activate the environment:
   ```bash
   conda activate hpc
   ```

---

### Step 3: Install Dependencies
```bash
conda install anaconda::scikit-learn anaconda::networkx conda-forge::matplotlib conda-forge::numba conda-forge::swig anaconda::ipykernel -y
#JAX
pip install jax==0.4.28 jaxlib==0.4.28 jax-cuda12-pjrt==0.4.28 jax-cuda12-plugin==0.4.28
# Note: JAX versions may vary depending on your machine and CUDA version.
```

For more details on installing CuPy with specific CUDA versions, see the [CuPy installation guide](https://docs.cupy.dev/en/stable/install.html).

---

### Step 4: Verify Installation
To verify that all dependencies are installed and working correctly, run the provided dependency check script:

```bash
python check_dependencies.py
```

This will display a comprehensive table showing:
- All installed packages and their versions
- CUDA support availability for GPU-accelerated packages (CuPy, JAX, Numba)
- A summary of the installation status

**Example Output:**
```
High-Performance Computing Python Dependencies Check

          ✓ Installed Packages           
┏━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ Package      ┃ Version ┃ CUDA Support ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━┩
│ NumPy        │ 2.3.5   │ -            │
│ Numba        │ 0.63.1  │ Yes          │
│ JAX          │ 0.4.28  │ Yes          │
│ CuPy         │ 13.3.0  │ Yes          │
│ scikit-learn │ 1.8.0   │ -            │
│ NetworkX     │ 3.6.1   │ -            │
│ Matplotlib   │ 3.10.8  │ -            │
└──────────────┴─────────┴──────────────┘

Summary: 7/7 packages installed

╭── GPU/CUDA Status ──╮
│   CuPy        : Yes │
│   JAX         : Yes │
│   Numba       : Yes │
╰─────────────────────╯
```

You can also check for SWIG availability:
```bash
which swig # show the path if swig is available
```

---

## Installation on Google Colab

Google Colab comes with most of the required scientific Python packages pre-installed, including JAX, CuPy, NumPy, Numba, and others with GPU support enabled by default.

To verify that all dependencies are properly installed and to check GPU/CUDA availability, simply download and run the dependency check script:

```python
# Download the check script
!wget -q https://raw.githubusercontent.com/Ziaeemehr/workshop_hpcpy/main/check_dependencies.py

# Run the dependency check
!python check_dependencies.py
```

This will display a table showing all installed packages, their versions, and CUDA support availability.

**Note:** Colab uses NVIDIA GPUs by default. To ensure GPU access, go to **Runtime** → **Change runtime type** and select **GPU** as the hardware accelerator.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Related resources
- [PythonHPC, CSCS](https://github.com/eth-cscs/PythonHPC)
- [High-performance computing with Python, JSC](https://gitlab.jsc.fz-juelich.de/sdlbio-courses/hpc-python/-/tree/2022)

*Note: Some of the notebooks in this repository are adapted from the above resources.*

## Contributing
Feel free to submit issues, fork the repository, and send pull requests. All contributions are welcome!

---

## Contact
For any questions, please reach out at a.ziaeemrhr[AT]gmail[dot]com.
