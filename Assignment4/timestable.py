import numpy as np
 
def times_table_lists(number):
    '''
    This function returns a list of lists containing the times table for the positive integer input 'number'
    It uses Python built-in operations in the standard library to calculate the times table
    '''
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


    
def times_table_numpy(number):
    '''
    This function returns a 2D numpy array containing the times table for the positive integer input 'number'
    It uses numpy functions to calculate the times table.
    '''
    n = int(number)
    a = np.ones(n**2, dtype=int).reshape(n, n)
    b = np.arange(n)
    a[0,:]= b
    d = a *(b[:,np.newaxis])
    e = d[1:,:]*b
    

    f = np.vstack ((b,e))
    
    times_table = np.hstack ((b[:,np.newaxis],f[:,1:]))

    h = np.logical_and(times_table % 7.5 == 0 , times_table != 0)
 
    #print (times_table[h].shape)
    
    return times_table

    














