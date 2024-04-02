from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pylab import plt
from matplotlib import animation, cm
import numpy as np
from scipy.signal import convolve, convolve2d


class Wave1D:
    K = np.array([1, -2, 1])

    def __init__(self):
        self.x = np.linspace(0, 100, 500)
        self.u_curr = np.zeros(self.x.size)

        r = np.abs(self.x - 20) / 10
        self.u_curr += np.where(r < 1, (np.cos(r * np.pi) + 1) / 2, 0)

        r = np.abs(self.x - 70) / 10
        self.u_curr -= np.where(r < 1, (np.cos(r * np.pi) + 1) / 2, 0)

        self.u_prev = np.array(self.u_curr)

        (self.fig, ax) = plt.subplots()
        ax.set_ylim(-2, 2)
        self.line, = plt.plot(self.x, self.u_curr)

    def update(self, _i):
        print(_i)
        uxx = convolve(self.u_curr, self.K, mode="same")
        u_next = 2 * self.u_curr - self.u_prev + 0.99 * uxx
        u_next[0] = u_next[1]
        u_next[-1] = u_next[-2]
        self.u_prev = self.u_curr
        self.u_curr = u_next
        self.line.set_data(self.x, u_next)
        return (self.line,)

    def make_animation(self):
        ani = animation.FuncAnimation(self.fig, self.update, frames=600, blit=True)
        ani.save("wave1d.mp4", writer="ffmpeg", fps=60)


Wave1D().make_animation()


class Wave2D:
    K = np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
    ])

    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.gca(projection="3d")
        self.ax.view_init(elev=50., azim=45)
        self.ax.set_zlim3d([-1, 1])
        self.x, self.y = np.meshgrid(
            np.arange(-2, 3, 0.025),
            np.arange(-2, 3, 0.025)
        )
        r = np.sqrt(self.x ** 2 + (self.y * 3) ** 2)
        self.u_curr = np.where(r < 1, (np.cos(r * np.pi) + 1) / 2, 0)
        self.u_prev = np.array(self.u_curr)
        self.surf = None

    def update(self, _i):
        print(_i)
        uxx = convolve2d(self.u_curr, self.K, mode="same")
        u_next = 2 * self.u_curr - self.u_prev + 0.7 * uxx
        u_next[0, :] = u_next[1, :]
        u_next[-1, :] = u_next[-2, :]
        u_next[:, 0] = u_next[:, 1]
        u_next[:, -1] = u_next[:, -2]
        self.u_prev = self.u_curr
        self.u_curr = u_next
        if self.surf:
            self.surf.remove()
        self.surf = self.ax.plot_surface(
            self.x, self.y, self.u_curr, cmap=cm.coolwarm,
            vmin=-0.25, vmax=0.25, linewidth=0, antialiased=False
        )
        return (self.surf,)

    def make_animation(self):
        ani = animation.FuncAnimation(self.fig, self.update, frames=600, blit=True)
        ani.save("wave2d.mp4", writer="ffmpeg", fps=60)


Wave2D().make_animation()