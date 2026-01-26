# SWIG Beginner Example: Hello World

This is a **simple toy example** to get started with SWIG. Perfect for learning the basics!

## What This Example Shows

This is the simplest possible SWIG example with:
- ✅ Simple functions (greet, add, multiply)
- ✅ Basic class with methods
- ✅ Easy to understand and modify
- ✅ Great for learning SWIG fundamentals

## Files

- **`hello.h`** - C++ header with simple functions and a basic Calculator class
- **`hello.i`** - SWIG interface file (very simple!)
- **`build.sh`** - Compilation script
- **`test_hello.py`** - Python script demonstrating usage

## Quick Start

### 1. Build

```bash
chmod +x build.sh
./build.sh
```

### 2. Run

```bash
python test_hello.py
```

### Expected Output

```
==================================================
SWIG Hello World Example
==================================================

1. String Function:
   Result: Hello, Alice!

2. Integer Addition:
   5 + 3 = 8

3. Float Multiplication:
   2.5 * 4.0 = 10.0

4. Using Calculator Class:
   Initial value: 0
   After set_value(10): 10
   After add_to(5): 15
   Message: Current value is: 15

==================================================
All tests completed successfully!
==================================================
```

## Usage Examples

### Call Simple Functions from Python

```python
import hello

# String function
greeting = hello.greet("Bob")
print(greeting)  # Output: Hello, Bob!

# Math functions
result = hello.add(10, 20)
print(result)  # Output: 30

result = hello.multiply(3.5, 2.0)
print(result)  # Output: 7.0
```

### Use C++ Classes from Python

```python
import hello

# Create a Calculator object
calc = hello.Calculator()

# Call methods
calc.set_value(100)
print(calc.get_value())  # Output: 100

calc.add_to(50)
print(calc.get_value())  # Output: 150

print(calc.get_message())  # Output: Current value is: 150
```

## How SWIG Works (Simple Explanation)

1. **`hello.h`** - Original C++ code
2. **`hello.i`** - Tell SWIG what to wrap
3. **`swig hello.i`** - SWIG generates `hello_wrap.cxx` (C++ code that bridges C++ and Python)
4. **`g++`** - Compile wrapper into `_hello.so` (shared library)
5. **`hello.py`** - SWIG generates this Python module wrapper automatically
6. **`import hello`** - Python can now use C++ functions!

## Step-by-Step: Modifying the Example

Want to add a new function? It's easy!

### 1. Add to `hello.h`:
```cpp
double divide(double a, double b) {
    return a / b;
}
```

### 2. Rebuild:
```bash
./build.sh
```

### 3. Use in Python:
```python
import hello
result = hello.divide(10.0, 2.0)
print(result)  # Output: 5.0
```

That's it! No other changes needed.

## Learning Path

After understanding this example:
1. ✅ Look at `example_2_vector` for more advanced features (std::vector, templates)
2. ✅ Explore SWIG documentation for:
   - Custom type conversions
   - Object ownership
   - Exception handling
   - Advanced features

## Requirements

- Python development headers: `sudo apt-get install python3-dev`
- SWIG: `sudo apt-get install swig`
- C++ compiler: `sudo apt-get install g++`

## Troubleshooting

**Error: `ImportError: cannot import name hello`**
- Did you run `./build.sh`? 
- Check that `_hello.so` exists in the directory

**Error: `command not found: swig`**
- Install SWIG: `sudo apt-get install swig`

**Error: `python3-dev not installed`**
- Install it: `sudo apt-get install python3-dev`

## Next Steps

Once you understand this example:
- Modify the `Calculator` class to add more methods
- Add a new class (e.g., `StringManipulator`)
- Try wrapping more complex C++ code
- Check out `example_2_vector` for std::vector usage

---

**Happy learning!** 🚀
