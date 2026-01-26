#!/bin/bash
# Build script for the hello example

# Detect Python configuration
PYTHON_INCLUDE=$(python3-config --includes)
PYTHON_LIBS=$(python3-config --libs)

echo "Python includes: $PYTHON_INCLUDE"
echo "Python libs: $PYTHON_LIBS"
echo ""

# Generate wrapper code
echo "Generating wrapper code with SWIG..."
swig -c++ -python hello.i

# Compile the wrapper
echo "Compiling wrapper..."
g++ -fPIC -c hello_wrap.cxx $PYTHON_INCLUDE

# Create the shared library
echo "Linking shared library..."
g++ -shared -o _hello.so hello_wrap.o $PYTHON_LIBS

echo ""
echo "✓ Build complete!"
echo "You can now run: python test_hello.py"
