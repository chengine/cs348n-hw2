import numpy as np
import matplotlib.pylab as plt
from plyfile import PlyData, PlyElement

def load_ply(fn):
    with open(fn, 'rb') as f:
        plydata = PlyData.read(f)
    pc = plydata['vertex'].data
    pc_array = np.array([[x, y, z] for x,y,z in pc])
    return pc_array

def viz_pc(pc, figsize=(4, 4), params=(20, 60)):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.view_init(elev=params[0], azim=params[1])
    x = pc[:, 0]
    y = pc[:, 2]
    z = pc[:, 1]
    ax.scatter(x, y, z, marker='.')
    miv = np.min([np.min(x), np.min(y), np.min(z)])
    mav = np.max([np.max(x), np.max(y), np.max(z)])
    ax.set_xlim(miv, mav)
    ax.set_ylim(miv, mav)
    ax.set_zlim(miv, mav)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    path = './training/deepsdf/scene0.ply'

    path2ba = './output/0.ply'
    path2bb = './output/1.ply'
    pc = load_ply(path2ba)
    viz_pc(pc)