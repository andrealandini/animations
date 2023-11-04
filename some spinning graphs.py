import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def helicoid(rho, theta, alpha, beta):
    x = rho * np.cos(alpha * theta)
    y = rho * np.sin(beta * theta)
    z = theta
    return x, y, z


def mobius_strip(t):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(-1, 1, 100)
    U, V = np.meshgrid(u, v)

    x = (1 + 0.5 * V * np.cos(0.5 * U)) * np.cos(U + t)
    y = (1 + 0.5 * V * np.cos(0.5 * U)) * np.sin(U + t)
    z = 0.5 * V * np.sin(0.5 * U)

    return x, y, z


def generate_torus(R, r, alpha, beta, num_pts=100):
    u = np.linspace(0, 2 * np.pi, num_pts)
    v = np.linspace(0, 2 * np.pi, num_pts)
    U, V = np.meshgrid(u, v)
    x = (R**(1/alpha) + r**beta * np.cos(V)) * np.cos(U)
    y = (R**alpha + r**(1/beta) * np.cos(V)) * np.sin(U)
    z = r * np.sin(V)
    return x, y, z



def generate_surface(frame=1):
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    Z = np.sin(np.sqrt(X**2 + Y**2) + 0.1 * frame)
    return X,Y,Z

fig = plt.figure(figsize=(15, 6), facecolor='#22272e',dpi=200)


parameter_values = np.linspace(0.1, 2, 200)
additional_values = np.ones(100, dtype=parameter_values.dtype) * 2
extended_array = np.concatenate((parameter_values, additional_values))
alpha_values = extended_array
beta_values = extended_array
alpha = alpha_values[0]
beta = beta_values[0]

plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05, wspace=0.3, hspace=0.3)




ax1 = fig.add_subplot(131, projection='3d', facecolor='#22272e')
#ax1.set_title('Helicoid')




ax2 = fig.add_subplot(133, projection='3d', facecolor='#22272e')
#ax2.set_title('Mobius Strip')  


rho = np.linspace(-1, 1, 100)
theta = np.linspace(-np.pi, np.pi, 100)
rho, theta = np.meshgrid(rho, theta)

x, y, z = helicoid(rho, theta, alpha, beta)
helicoid_plot = ax1.plot_surface(x, y, z, cmap='viridis')


t = 0
x, y, z = mobius_strip(t)
mobius_strip_plot = ax2.plot_surface(x, y, z, cmap='viridis')



#ax3 = fig.add_subplot(133, projection='3d', facecolor='black')
#ax3.set_title('Torus')

#R = 2  # Major radius of the torus
#r = 1  # Minor radius of the torus
#x, y, z = generate_torus(R, r, alpha, beta)
#torus_plot = ax3.plot_surface(x, y, z, cmap='viridis')

ax3 = fig.add_subplot(132, projection='3d', facecolor='#22272e')
#ax3.set_title('Torus')
x,y, z = generate_surface()
generate_surface_plot = ax3.plot_surface(x, y, z, cmap='viridis')#rstride=1, cstride=1, linewidth=0, antialiased=False)
ax3.set_zlim(-1, 1)



def update(i):
    ax1.view_init(elev=30., azim=i)
    ax1.axis('off')
    ax1.grid(False)

    ax2.view_init(elev=30., azim=i)
    ax2.axis('off')
    ax2.grid(False)

    ax3.view_init(elev=30., azim=i)
    ax3.axis('off')
    ax3.grid(False)

    global helicoid_plot
    global mobius_strip_plot
    global generate_surface_plot

    alpha = alpha_values[i % len(alpha_values)]
    beta = beta_values[i % len(beta_values)]

    x, y, z = helicoid(rho, theta, alpha, beta)
    helicoid_plot.remove()
    helicoid_plot = ax1.plot_surface(x, y, z, cmap='viridis')

    # Update the Mobius strip plot with varying t
    t = i * 0.1
    x, y, z = mobius_strip(t)
    mobius_strip_plot.remove()
    mobius_strip_plot = ax2.plot_surface(x, y, z, cmap='viridis')

    x,y, z = generate_surface(i)
    generate_surface_plot.remove()
    generate_surface_plot = ax3.plot_surface(x, y, z, cmap='viridis')


ani = FuncAnimation(fig, update, frames=np.arange(0, len(extended_array), 1), interval=100)
ani.save('spinning_graphs.mp4', writer='ffmpeg')
#plt.show()


