import numpy as np

def times_table_numpy(number):
    
    n = int(number)
    a = np.ones((n+1)**2, dtype=int).reshape(n+1, n+1)
    b = np.arange(n+1)
    a[0,:]= b
    d = a *(b[:,np.newaxis])
    e = d[1:,:]*b
    
    f = np.vstack ((b,e))
    
    times_table = np.hstack ((b[:,np.newaxis],f[:,1:]))

    return times_table

def times_table_lists(number):
 
    n = int(number)
    times_table_list = []
    for k in range(n):
        times_table_list.append([k])
    
    for i in range(0, n):
        if i == 0: 
            for k in range(1, n):
                times_table_list[0].append(k)
        else:
            for j in range(1, n):
                times_table_list[i].append(i * j)
    
    return times_table_list


import timeit
print (timeit.timeit('[func(15) for func in (times_table_numpy,)]', number = 1500, globals=globals()))
# now it's inputting 15 into the function, and running this 1500 times
print ("let's have a test for numpy!")
print (timeit.timeit('[func(1) for func in (times_table_numpy,)]', number = 1, globals=globals()))
print (timeit.timeit('[func(10) for func in (times_table_numpy,)]', number = 1, globals=globals()))
print (timeit.timeit('[func(100) for func in (times_table_numpy,)]', number = 1, globals=globals()))
print (timeit.timeit('[func(1000) for func in (times_table_numpy,)]', number = 1, globals=globals()))
print (timeit.timeit('[func(10000) for func in (times_table_numpy,)]', number = 1, globals=globals()))
print ("how about lists?")
print (timeit.timeit('[func(1) for func in (times_table_lists,)]', number = 1, globals=globals()))
print (timeit.timeit('[func(10) for func in (times_table_lists,)]', number = 1, globals=globals()))
print (timeit.timeit('[func(100) for func in (times_table_lists,)]', number = 1, globals=globals()))
print (timeit.timeit('[func(1000) for func in (times_table_lists,)]', number = 1, globals=globals()))
print (timeit.timeit('[func(10000) for func in (times_table_lists,)]', number = 1, globals=globals()))


