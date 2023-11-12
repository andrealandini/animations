import matplotlib.pyplot as plt
import numpy as np

# Set up the figure and axes
fig = plt.figure(figsize=(8, 6), facecolor='#22272e')#,dpi=200)

ax = fig.add_subplot(111, projection='3d', facecolor='#22272e')

# Fake data
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = x + y
bottom = np.zeros_like(top)
width = depth = 1

# Use 'inferno' colormap
cmap = plt.get_cmap('inferno')
colors = cmap(top / np.max(top))

# Remove background by setting facecolors to 'none'
ax.bar3d(x, y, bottom, width, depth, top, shade=True, color=colors, facecolors='none')
#ax.set_title('Shaded 3D Plot with Inferno Colormap (No Background)')
#ax.set_facecolor('black')
# Remove axis labels and ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_zlabel('')
ax.axis('off')
ax.grid(False)
plt.show()
