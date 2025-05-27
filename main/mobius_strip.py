
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MobiusStrip:
    def __init__(self, R, w, n):
        self.R = R
        self.w = w
        self.n = n
        self.u_vals = np.linspace(0, 2 * np.pi, n)
        self.v_vals = np.linspace(-w/2, w/2, n)
        self.X, self.Y, self.Z = self.generate_surface()

    def generate_surface(self):
        u, v = np.meshgrid(self.u_vals, self.v_vals)
        x = (self.R + v * np.cos(u / 2)) * np.cos(u)
        y = (self.R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)
        return x, y, z

    def compute_surface_area(self):
        area = 0
        for i in range(self.n - 1):
            for j in range(self.n - 1):
                p1 = np.array([self.X[i,j], self.Y[i,j], self.Z[i,j]])
                p2 = np.array([self.X[i+1,j], self.Y[i+1,j], self.Z[i+1,j]])
                p3 = np.array([self.X[i,j+1], self.Y[i,j+1], self.Z[i,j+1]])
                vec1 = p2 - p1
                vec2 = p3 - p1
                patch_area = 0.5 * np.linalg.norm(np.cross(vec1, vec2))
                area += patch_area
        return area

    def compute_edge_length(self):
        edge_u = self.u_vals
        edge_v = np.full_like(edge_u, self.w / 2)
        x = (self.R + edge_v * np.cos(edge_u / 2)) * np.cos(edge_u)
        y = (self.R + edge_v * np.cos(edge_u / 2)) * np.sin(edge_u)
        z = edge_v * np.sin(edge_u / 2)
        length = np.sum(np.sqrt(np.diff(x)**2 + np.diff(y)**2 + np.diff(z)**2))
        return length

    def plot(self):
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, cmap='viridis', edgecolor='none')
        ax.set_title("Mobius Strip")
        plt.show()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print("Usage: python mobius_strip.py <R> <w> <n>")
    else:
        R = float(sys.argv[1])
        w = float(sys.argv[2])
        n = int(sys.argv[3])
        strip = MobiusStrip(R, w, n)
        print("Surface Area:", strip.compute_surface_area())
        print("Edge Length:", strip.compute_edge_length())
        strip.plot()
