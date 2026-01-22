# Using the line and memory profilers


## `line_profiler`
The `line_profiler` demonstration is inside the notebook `01_line_profiler.ipynb`.
The scripts `lineprofiler_euclidean_trick.py` and `lineprofiler_euclidean_broadcast.py` are standalone versions that can be run without the notebook (they use the `LineProfiler` API instead of the `%lprun` magic command). 


## `memory_profiler`
Here we use `memory_profiler` by decorating the function we want to profile with `@profile`.
Then, running it normally:
```bash
python memprofiler_euclidean_trick.py
python memprofiler_euclidean_broadcast.py
```
will print the line-by-line memory usage of each function.
