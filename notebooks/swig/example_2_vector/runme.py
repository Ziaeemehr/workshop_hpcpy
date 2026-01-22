# file: runme.py

import example
from sys import exit

print("=" * 70)
print("SWIG Vector Example - Demonstrating C++ std::vector wrapping")
print("=" * 70)

# Call average with a Python list...
print("\n1. AVERAGE FUNCTION WITH PYTHON LIST")
print("-" * 70)
py_list = [1, 2, 3, 4]
print(f"   Input (Python list): {py_list}")
result = example.average(py_list)
print(f"   Result: {result}")

# ... or a wrapped std::vector<int>
print("\n2. AVERAGE FUNCTION WITH C++ IntVector")
print("-" * 70)
v = example.IntVector(4)
print(f"   Creating IntVector of size 4")
for i in range(len(v)):
    v[i] = i + 1
print(f"   Populated with: {[v[i] for i in range(len(v))]}")
result = example.average(v)
print(f"   Result: {result}")


# half will return a Python list.
# Call it with a Python tuple...
print("\n3. HALF FUNCTION WITH PYTHON TUPLE")
print("-" * 70)
py_tuple = (1.0, 1.5, 2.0, 2.5, 3.0)
print(f"   Input (Python tuple): {py_tuple}")
result = example.half(py_tuple)
print(f"   Result: {result}")
print(f"   Return type: {type(result).__name__}")

# ... or a wrapped std::vector<double>
print("\n4. HALF FUNCTION WITH C++ DoubleVector")
print("-" * 70)
v = example.DoubleVector()
print(f"   Creating empty DoubleVector")
for val in [1, 2, 3, 4]:
    v.append(val)
print(f"   Populated with: {[v[i] for i in range(len(v))]}")
result = example.half(v)
print(f"   Result: {result}")
print(f"   Return type: {type(result).__name__}")

# now halve a wrapped std::vector<double> in place
print("\n5. HALVE_IN_PLACE FUNCTION - MODIFYING VECTOR IN PLACE")
print("-" * 70)
print(f"   Original DoubleVector: {[v[i] for i in range(len(v))]}")
example.halve_in_place(v)
print(f"   After halve_in_place(): {[v[i] for i in range(len(v))]}")

print("\n" + "=" * 70)
print("All examples completed successfully!")
print("=" * 70)
