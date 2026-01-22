#!/usr/bin/env python
"""
Test script for the hello SWIG example
Demonstrates simple function calls and class usage
"""

import hello

print("=" * 50)
print("SWIG Hello World Example")
print("=" * 50)

# Test 1: Simple string function
print("\n1. String Function:")
result = hello.greet("Alice")
print(f"   Result: {result}")

# Test 2: Integer addition
print("\n2. Integer Addition:")
sum_result = hello.add(5, 3)
print(f"   5 + 3 = {sum_result}")

# Test 3: Float multiplication
print("\n3. Float Multiplication:")
product = hello.multiply(2.5, 4.0)
print(f"   2.5 * 4.0 = {product}")

# Test 4: Using a C++ class
print("\n4. Using Calculator Class:")
calc = hello.Calculator()
print(f"   Initial value: {calc.get_value()}")

calc.set_value(10)
print(f"   After set_value(10): {calc.get_value()}")

calc.add_to(5)
print(f"   After add_to(5): {calc.get_value()}")

print(f"   Message: {calc.get_message()}")

print("\n" + "=" * 50)
print("All tests completed successfully!")
print("=" * 50)
