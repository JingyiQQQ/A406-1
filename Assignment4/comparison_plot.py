import numpy as np
import csv
import matplotlib.pyplot as plt

'''
with open('timetester_numpy&list.csv', 'w', newline='') as file:
    fieldnames = ['input number', 'runtime_numpy', 'runtime_list']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'input number': '1', 'runtime_numpy': 7.48000000000415e-05, 'runtime_list': 7.500000000160156e-06})
    writer.writerow({'input number': '10', 'runtime_numpy': 8.790000000002962e-05, 'runtime_list': 4.4200000000049755e-05})
    writer.writerow({'input number': '100', 'runtime_numpy': 0.00021210000000004836, 'runtime_list': 0.002609899999999943})
    writer.writerow({'input number': '1000', 'runtime_numpy': 0.014974800000000066, 'runtime_list': 0.20359429999999978})
    writer.writerow({'input number': '10000', 'runtime_numpy': 1.3271888, 'runtime_list': 15.3854529})
'''
nms = [[1, 10, 100, 1000, 10000], [7.239999999997249e-05, 7.950000000001012e-05, 0.00021680000000001698, 0.01465749999999999, 1.4524404], [5.900000000114147e-06, 3.989999999998162e-05, 0.0013011999999998913, 0.1483654000000003, 19.8873138]]

for row in nms : 
    print(row) 
tran = [[nms[j][i] for j in range(len(nms))] for i in range(len(nms[0]))] 

for row in tran: 
    print(row) 

with open('runtime_numpy&list.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in tran:
        writer. writerow(row) 
        

x = []
y = []
z = []

with open('runtime_numpy&list.csv', newline='') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        print (row)
        x.append(int(row[0]))
        y.append(float(row[1])) 
        z.append(float(row[2]))


plt.title('Runtime Comparison: Numpy vs List')
plt.plot(x, y, marker='D', color='green', label='numpy')
plt.plot(x, z, marker="^", color='orange', label='list')

plt.xlabel('input number')
plt.ylabel('runtime/s')
plt.xscale('log')
plt.yscale('log')

plt.legend()
plt.show()

