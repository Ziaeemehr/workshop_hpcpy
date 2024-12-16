# Variables
PYTHON_CONFIG := python3-config
PYTHON_INCLUDE := $(shell $(PYTHON_CONFIG) --includes)
PYTHON_LIBS := $(shell $(PYTHON_CONFIG) --ldflags)
SWIG := swig
CXX := g++
CXXFLAGS := -O2 -fPIC
LDFLAGS := -shared

# Targets
all: _example.so

example_wrap.cxx: example.i
	$(SWIG) -c++ -python example.i

example_wrap.o: example_wrap.cxx example.h
	$(CXX) $(CXXFLAGS) -c example_wrap.cxx -I. $(PYTHON_INCLUDE)

_example.so: example_wrap.o
	$(CXX) $(LDFLAGS) example_wrap.o -o $@ $(PYTHON_LIBS)

clean:
	rm -f *.o *.so example_wrap.cxx example.py
