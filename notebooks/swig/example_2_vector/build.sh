#!/bin/bash

# Get Python include and library paths dynamically
PYTHON_INCLUDE=$(python3-config --includes)
PYTHON_LIBS=$(python3-config --ldflags)

echo "Python includes: $PYTHON_INCLUDE"
echo "Python libs: $PYTHON_LIBS"
echo ""

# Generate SWIG wrapper
echo "Generating wrapper code with SWIG..."
swig -c++ -python example.i

# Compile the SWIG wrapper
echo "Compiling wrapper..."
g++ -O2 -fPIC -c example_wrap.cxx $PYTHON_INCLUDE

# Link to create the shared library
echo "Linking shared library..."
g++ -shared example_wrap.o -o _example.so $PYTHON_LIBS

echo ""
echo "✓ Build complete!"
echo "Shared library '_example.so' created."
echo "You can now run: python runme.py"
