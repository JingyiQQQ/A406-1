# import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# determine the number of points that you want to plot
num_points = 10000
fraction = 0.5

# define the vertices for my polygon
verts = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])

# set up an array of random numbers to index the vertices
vert_ind = np.random.randint(0, len(verts), num_points)

# set up the first point
first_point = np.random.random(2)

# initialize an array to hold the scatter plot points and put the first point into the array
scatter_points = np.ma.masked_array(np.zeros((num_points, 2)), mask=np.ones((num_points, 2), dtype=bool))
scatter_points[0, :] = first_point
scatter_points.mask[0, :] = False

# loop through the scatter points and perform a mystery operation on them
for ii in range(1, num_points):
    scatter_points.data[ii, :] = fraction * verts[vert_ind[ii]] + (1 - fraction) * scatter_points.data[ii-1, :]

# set up a plot in matplotlib
fig, ax = plt.subplots()

# plot the points on a matplotlib scatter plot: you must write the scatterplot function yourself!
scatter = plt.scatter(scatter_points[:, 0],scatter_points[:, 1])
#fill in this line with a scatterplot on ax to plot scatter_points!

# change the scale and appearance of the axes
plt.xlim([0, 1.])
plt.ylim([-0.1, 0.9])
plt.axis('off')

# a function to update the plot over time
def update(num):
    scatter_points.mask = True
    scatter_points.mask[:num, :] = False
    scatter.set_offsets(scatter_points)
    return scatter,

# function for animating the mystery plot... what could it be?
ani = animation.FuncAnimation(fig, update, len(scatter_points), interval=15, blit=True)

# show the plot
plt.show()
