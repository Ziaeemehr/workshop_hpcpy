#!/bin/bash
# Clean script for the hello example
# Removes all built files and intermediate objects

echo "Cleaning build artifacts..."

# Remove generated SWIG files
rm -f hello_wrap.cxx
rm -f hello_wrap.o
rm -f hello.py

# Remove compiled shared library
rm -f _hello.so

# Remove build directory if it exists
rm -rf build/

# Remove Python cache
rm -rf __pycache__/
rm -f *.pyc

# Remove any object files
rm -f *.o

echo "✓ Clean complete!"
echo "All build artifacts have been removed."
echo ""
echo "To rebuild, run: ./build.sh"
