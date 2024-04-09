import matplotlib.pyplot as plt
import numpy as np

def rand_points(points):
    """Plots random points in space"""
    # create axes - x, y, z
    ax = plt.axes(projection='3d')

    # randint(from, to, shape)
    x_data = np.random.randint(0, 100, (points, ))
    y_data = np.random.randint(0, 100, (points, ))
    z_data = np.random.randint(0, 100, (points, ))

    # scatter plot values, marker 'v' displays points as triangles
    ax.scatter(x_data, y_data, z_data, marker='v')
    plt.show()


def plot_in_3d():
    """Plots function in 3D"""
    ax = plt.axes(projection='3d')

    x_data = np.arange(0, 50, 0.1)
    y_data = np.arange(0, 50, 0.1)
    z_data = np.sin(x_data) * np.cos(y_data)

    print('shape of z_data:', z_data.shape)

    # create plot
    ax.plot(x_data, y_data, z_data)

    # add atributes - set labels
    ax.set_title('Function in 3D')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z = f(x, y)')
    plt.show()


def surface_plot():
    """Plots surface from meshgrid"""
    ax = plt.axes(projection='3d')

    x_data = np.arange(-5, 5, 0.1)
    y_data = np.arange(-5, 5, 0.1)

    # create meshgrid of arrays
    X, Y = np.meshgrid(x_data, y_data)
    #print(X.shape)

    Z = np.sin(X) * np.cos(Y)

    # cmap - color mapping
    ax.plot_surface(X, Y, Z, cmap='plasma')

    # starting view: rotate, angle 
    ax.view_init(azim=0, elev=50)

    plt.show()


surface_plot()