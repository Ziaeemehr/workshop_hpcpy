/* File: hello.h */

#include <string>
#include <iostream>

// Simple function that returns a greeting
std::string greet(const std::string& name) {
    return "Hello, " + name + "!";
}

// Simple function that adds two numbers
int add(int a, int b) {
    return a + b;
}

// Simple function that multiplies two numbers
double multiply(double x, double y) {
    return x * y;
}

// Simple class example
class Calculator {
private:
    int result;
    
public:
    Calculator() : result(0) {}
    
    void set_value(int val) {
        result = val;
    }
    
    int get_value() {
        return result;
    }
    
    void add_to(int val) {
        result += val;
    }
    
    std::string get_message() {
        return "Current value is: " + std::to_string(result);
    }
};
