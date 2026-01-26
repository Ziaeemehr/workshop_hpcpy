/* File: benchmark.i */
%module benchmark

%{
#include "benchmark.h"
%}

%include "std_vector.i"

/* Instantiate vector templates */
namespace std {
    %template(DoubleVector) vector<double>;
    %template(VectorOfDoubles) vector<std::vector<double>>;
}

%include "benchmark.h"
