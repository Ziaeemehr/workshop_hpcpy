# SWIG C++ Vector Example

This example demonstrates how to use **SWIG (Simplified Wrapper and Interface Generator)** to wrap C++ `std::vector` templates and make them accessible from Python.

## Overview

This project shows how to:
- Wrap C++ functions that work with `std::vector<int>` and `std::vector<double>`
- Use SWIG templates to create Python-friendly vector classes
- Call C++ functions from Python with automatic type conversion
- Modify C++ vectors in-place from Python

## Files

### Source Files

- **`example.h`** - C++ header file containing the implementation
  - `double average(std::vector<int> v)` - Computes average of integers
  - `std::vector<double> half(const std::vector<double>& v)` - Returns halved values
  - `void halve_in_place(std::vector<double>& v)` - Halves values in-place

- **`example.i`** - SWIG interface file
  - Defines module name (`example`)
  - Includes `std_vector.i` for vector support
  - Instantiates templates for `IntVector` and `DoubleVector`

### Build Files

- **`makefile`** - Compilation rules for building the C++ extension
- **`build.sh`** - Shell script to compile using SWIG

### Generated Files (After Build)

- **`example_wrap.cxx`** - SWIG-generated C++ wrapper code
- **`example_wrap.o`** - Compiled wrapper object file
- **`_example.so`** - Shared library (Python extension module)
- **`example.py`** - SWIG-generated Python module wrapper

### Testing

- **`runme.py`** - Python script demonstrating usage of the wrapped C++ code

## How to Use

### 1. Build the Extension

Compile the C++ code into a Python extension module:

```bash
# Using the build script
./build.sh

# Or using make
make
```

This will generate `_example.so` (the compiled extension) and `example.py` (Python wrapper).

### 2. Run the Example

Execute the demo script:

```bash
python runme.py
```

**Expected Output:**
```
2.5                           # average([1, 2, 3, 4])
2.5                           # average(IntVector([1, 2, 3, 4]))
(0.5, 0.75, 1.0, 1.25, 1.5)  # half((1.0, 1.5, 2.0, 2.5, 3.0))
(0.5, 0.75, 1.0, 1.25, 1.5)  # half(DoubleVector([1, 2, 3, 4]))
<class 'tuple'>               # Type of returned value
0.5; 0.375; 0.5; 0.625;      # After halve_in_place(v)
```

## Usage Examples

### Working with Python Lists

```python
import example

# Use Python lists directly
result = example.average([1, 2, 3, 4])
print(result)  # Output: 2.5
```

### Working with C++ Vectors

```python
import example

# Create a C++ vector and populate it
v = example.IntVector(4)
for i in range(len(v)):
    v[i] = i + 1

# Pass to C++ function
result = example.average(v)
print(result)  # Output: 2.5
```

### Using DoubleVector

```python
import example

# Create and populate a double vector
v = example.DoubleVector()
for i in [1.0, 2.0, 3.0]:
    v.append(i)

# Call functions
result = example.half(v)  # Returns tuple
print(result)  # Output: (0.5, 1.0, 1.5)

# Modify in-place
example.halve_in_place(v)
for val in v:
    print(val)  # Output: 0.5, 1.0, 1.5
```

## Key Concepts

### SWIG Templates

The `.i` file uses template instantiation to create Python-accessible vector types:

```swig
%template(IntVector)    vector<int>;
%template(DoubleVector) vector<double>;
```

This creates `example.IntVector` and `example.DoubleVector` classes in Python.

### Automatic Type Conversion

- Python lists can be passed to C++ functions expecting `std::vector`
- C++ vectors return as Python tuples (or can be wrapped as objects)
- SWIG handles the conversion automatically

### Reference vs Copy

- `std::vector<double>& v` - References can be modified in-place
- `const std::vector<double>& v` - Const references create copies
- `std::vector<int> v` - Pass-by-value creates a copy

## Compilation Details

The makefile uses:
1. `swig` - To generate C++ wrapper from `.i` file
2. `g++` - To compile the C++ wrapper and link with Python

```bash
swig -c++ -python example.i
g++ -fPIC -c example_wrap.cxx -I/usr/include/python3.x
g++ -shared -o _example.so example_wrap.o
```

## Requirements

- Python development headers (`python-dev`)
- SWIG (`swig`)
- C++ compiler (`g++`)
- Standard C++ library with STL support

## Troubleshooting

**Issue:** `ImportError: cannot import name example`
- Ensure `_example.so` and `example.py` are in the same directory as `runme.py`
- Run `make` to rebuild if files are missing

**Issue:** `TypeError: in method 'average', argument 1 of type 'std::vector< int >'`
- Pass a Python list or `IntVector` object, not other types

**Issue:** Compilation fails
- Check that Python development headers are installed: `python3-dev`
- Verify SWIG is installed: `which swig`

## Further Reading

- [SWIG Documentation](http://www.swig.org/Doc3.0/Contents.html)
- [SWIG and C++ Vectors](http://www.swig.org/Doc3.0/Library.html#Library_stl_containers)
- [Python C API](https://docs.python.org/3/c-api/)
