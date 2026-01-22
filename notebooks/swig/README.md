# SWIG Examples

This folder contains examples of how to wrap C++ code to make it accessible from Python using **SWIG (Simplified Wrapper and Interface Generator)**.

## Examples

### 1. **Hello World** (Beginner) ⭐ START HERE
**Location:** `example_1_hello/`

Perfect for beginners! This example demonstrates:
- Simple function wrapping (greet, add, multiply)
- Basic C++ class with methods
- Easy to understand and modify

**Quick Start:**
```bash
cd example_1_hello
./build.sh
python test_hello.py
```

### 2. **Vector Operations** (Intermediate)
**Location:** `example_2_vector/`

Advanced example with:
- C++ `std::vector` template wrapping
- Multiple template instantiations
- In-place modifications of C++ objects

**Quick Start:**
```bash
cd example_2_vector
./build.sh
python runme.py
```

## Recommended Learning Path

1. **Start with `example_1_hello`** - Learn the basics
2. **Then move to `example_2_vector`** - Learn about templates
3. **Experiment** - Modify the examples and rebuild

## Advanced Examples

For more advanced SWIG projects with complete Python packages and professional structure, check out:

🔗 **[demo_swig](https://github.com/Ziaeemehr/demo_swig)** - A comprehensive repository showing:
- Professional Python package structure with SWIG-wrapped C++
- Complex C++ classes and inheritance
- Advanced template instantiations
- Best practices for production code
- Packaging and distribution

This is perfect after you've mastered the basics in the examples above.

## General SWIG Workflow

```
C++ Code (.h)  →  SWIG Interface (.i)  →  SWIG Generator  →  Python Module
hello.h        →  hello.i              →  swig command  →  hello.py + _hello.so
                                                              (usable from Python!)
```

## Resources

- [Official SWIG Documentation](http://www.swig.org/)
- [SWIG C++ Tutorial](http://www.swig.org/Doc3.0/SWIGPlus.html)
- [Python C API](https://docs.python.org/3/c-api/)
