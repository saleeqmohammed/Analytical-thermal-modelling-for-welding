from settings import Tmelting_rel
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np


def weld_plot(plot_type,data):
    point_x=[]
    point_y=[]
    point_z=[]
    point_temp=[]
    if plot_type == "time-temperature":
        plt.plot(data[1],data[0])
        plt.show()
    if plot_type == "space-temperature":
        for key,value in data.items():
            if key[0]==0 and value>Tmelting_rel:
                point_y.append(key[1]*0.1)
                point_z.append(key[2]*0.1)
                point_temp.append(value)
        plot1=plt.figure(1)
        plt.scatter(point_y,point_z,c=point_temp,cmap='plasma')
        plt.xlabel('Y - axis')
        plt.ylabel('Z - axis')
        plt.colorbar()
        plt.show()
        

    else:
        print("Err: No such plot")


def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])

def plot3D(data):
    point_x=[]
    point_y=[]
    point_z=[]
    point_temp=[]
    for key,value in data.items():
        point_x.append(key[0]*0.1)
        point_y.append(key[1]*0.1)
        point_z.append(key[2]*0.1)
        point_temp.append(value)
    fig = plt.figure()

    ax = plt.axes(projection='3d')
    pl=ax.scatter3D(point_x, point_y, point_z, c=point_temp, cmap='Spectral')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    set_axes_equal(ax)
    fig.colorbar(pl, ax=ax)
    plt.show()



