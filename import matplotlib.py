import matplotlib.pyplot as plt

points = []
fig, ax = plt.subplots()
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_aspect('equal')
ax.grid(True)
line_obj = None

def onclick(event):
    global points, line_obj
    if event.inaxes != ax:
        return
    if event.button == 1:  # Left click
        points.append([event.xdata, event.ydata])
        if len(points) > 1:
            xs = [p[0] for p in points]
            ys = [p[1] for p in points]
            if line_obj:
                line_obj.remove()
            line_obj, = ax.plot(xs, ys, 'r--')
        fig.canvas.draw()
    elif event.button == 3:  # Right click closes contour
        if len(points) < 3:
            print("Need 3 points minimum")
            return
        points.append(points[0])
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        ax.plot(xs, ys, 'r-', lw=2)
        fig.canvas.draw()
        fig.canvas.mpl_disconnect(cid)  # stop further clicks
        print("Contour finished!")

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
##fjdhksjfhlg
