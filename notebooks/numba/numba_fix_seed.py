import numpy as np
from numba import jit
from numba.extending import register_jitable

np.random.seed(42)


# This will run in JIT mode only if called from a JIT function
@register_jitable
def set_seed_compact(x):
    np.random.seed(x)


@jit(nopython=True)
def get_random():
    set_seed_compact(42)
    print(np.random.rand(3))


def get_random2():
    print(np.random.rand(3))


get_random()
get_random2()
