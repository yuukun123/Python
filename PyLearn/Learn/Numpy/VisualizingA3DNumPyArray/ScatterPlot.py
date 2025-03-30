import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create sample 3D data (e.g., random points)
data = np.random.rand(100, 3) * 10  # 100 points, each with x, y, z coordinates

# Extract x, y, z from the array
x = data[:, 0]
y = data[:, 1]
z = data[:, 2]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the scatter points
ax.scatter(x, y, z, c='b', marker='o')  # c is color, marker is point shape

# Labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Scatter Plot')

# Show the plot
plt.show()