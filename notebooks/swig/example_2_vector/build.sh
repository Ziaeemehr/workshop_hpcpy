#!/bin/bash

# Get Python include and library paths dynamically
PYTHON_INCLUDE=$(python3-config --includes)
PYTHON_LIBS=$(python3-config --ldflags)

# Generate SWIG wrapper
swig -c++ -python example.i

# Compile the SWIG wrapper
g++ -O2 -fPIC -c example_wrap.cxx $PYTHON_INCLUDE

# Link to create the shared library
g++ -shared example_wrap.o -o _example.so $PYTHON_LIBS

echo "Build complete. Shared library '_example.so' created."
