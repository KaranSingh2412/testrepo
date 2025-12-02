import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Constants
mu0 = 4 * np.pi * 1e-7  # Permeability of free space (T·m/A)
I = 1.0  # Current in Amperes

# Lists to store points
circum_points = []
center = None

def onclick(event):
    global center
    if event.xdata is None or event.ydata is None:
        return

    if center is None:
        # First click sets the center (wire location)
        center = (event.xdata, event.ydata)
        print(f"Center set at: {center}")
        ax.scatter(center[0], center[1], c='blue', label='Wire (Center)')
        ax.legend()
        plt.draw()
    else:
        # Subsequent clicks are points on circumference
        x, y = event.xdata, event.ydata
        circum_points.append((x, y))
        ax.scatter(x, y, c='red')
        
        # Draw circle through this point
        radius = np.sqrt((x - center[0])**2 + (y - center[1])**2)
        circle = plt.Circle(center, radius, color='green', fill=False, linestyle='--')
        ax.add_patch(circle)
        plt.draw()
        print(f"Point added on circumference: ({x:.2f}, {y:.2f}) with radius {radius:.2f}")

# Create figure
fig, ax = plt.subplots()
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_aspect('equal')
ax.set_title("Click to set wire center and circle points")
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# Grid for magnetic field
x = np.linspace(0, 20, 50)
y = np.linspace(0, 20, 50)
X, Y = np.meshgrid(x, y)
quiver = None  # Placeholder for quiver plot

def animate(frame):
    global quiver
    if center is None:
        return

    # Magnetic field magnitude (Biot-Savart for long straight wire)
    dx = X - center[0]
    dy = Y - center[1]
    r = np.sqrt(dx**2 + dy**2)
    r[r == 0] = 1e-9  # Avoid division by zero

    B = mu0 * I / (2 * np.pi * r)

    # Tangential direction around wire
    Bx = -B * dy / r
    By = B * dx / r

    # Rotate field slightly for animation
    angle = np.radians(frame)
    Bx_rot = Bx * np.cos(angle) - By * np.sin(angle)
    By_rot = Bx * np.sin(angle) + By * np.cos(angle)

    if quiver:
        quiver.remove()

    quiver = ax.quiver(X, Y, Bx_rot, By_rot, color='purple', pivot='middle', scale=20)

# Animate
ani = FuncAnimation(fig, animate, frames=360, interval=50, repeat=True)

plt.show()
