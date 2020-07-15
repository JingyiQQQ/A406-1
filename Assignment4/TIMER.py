import numpy as np

def times_table_numpy(number):
    
    n = int(number)
    a = np.ones((n+1)**2, dtype=int).reshape(n+1, n+1)
    b = np.arange(n+1)
    c = a
    a[0,:]= b
    d = c *(b[:,np.newaxis])
    a[1:,:]= d[1:,:]
    e = a[1:,:]*b
    
    f = np.vstack ((b,e))
    
    times_table = np.hstack ((b[:,np.newaxis],f[:,1:]))

    return times_table

def times_table_lists(number):
 
    times_table_list = []
    for k in range(1, int(number)):
            times_table_list.append(k)

    for i in range(1, int(number)):   
        times_table_list.append(i)
        for j in range(1, int(number)):
            times_table_list.append(i * j)
    
    return times_table_list

import timeit
print (timeit.timeit('[func(15) for func in (times_table_numpy,)]', number = 1500, globals=globals()))

print (timeit.timeit('[func(15) for func in (times_table_lists,)]', number = 1500, globals=globals()))
