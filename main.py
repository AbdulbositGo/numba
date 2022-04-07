from numba import njit, prange
from time import time


before = time()
@njit(fastmath=True, cache=True)
def massive(nums):

    result = 0
    for num in range(nums):
        result += num
    print(num)    
    return result

natija = massive(1000000000)
print(natija)
after = time() - before
print(keyingi)