/* File: hello.i */
%module hello

%{
#include "hello.h"
%}

/* Include standard string handling */
%include "std_string.i"

/* Include the header */
%include "hello.h"
