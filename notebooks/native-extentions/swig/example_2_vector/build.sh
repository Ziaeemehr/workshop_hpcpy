#!/bin/bash

# Get Python include and library paths dynamically
PYTHON_INCLUDE=$(python3-config --includes)
PYTHON_LIBS=$(python3-config --ldflags)

echo "Python includes: $PYTHON_INCLUDE"
echo "Python libs: $PYTHON_LIBS"
echo ""

# Generate SWIG wrappers
echo "Generating wrapper code with SWIG..."
swig -c++ -python example.i
swig -c++ -python benchmark.i

# Compile the SWIG wrappers
echo "Compiling wrappers..."
g++ -O2 -fPIC -c example_wrap.cxx $PYTHON_INCLUDE
g++ -O2 -fPIC -c benchmark_wrap.cxx $PYTHON_INCLUDE

# Link to create the shared libraries
echo "Linking shared libraries..."
g++ -shared example_wrap.o -o _example.so $PYTHON_LIBS
g++ -shared benchmark_wrap.o -o _benchmark.so $PYTHON_LIBS

echo ""
echo "✓ Build complete!"
echo "Shared libraries created:"
echo "  - _example.so"
echo "  - _benchmark.so"
echo "You can now run: python runme.ipynb"
