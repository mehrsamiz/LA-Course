import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import product, combinations


def check_if_span_space(vectors):
    matrix = np.array(vectors).T  # Vectors as columns
    rank = np.linalg.matrix_rank(matrix)
    return rank == 3  # rank == 3 => 3D space

# reachable points within the workspace 
def generate_reachable_points(vectors, step=1, workspace_limit=100):
    points = []
    for i in np.arange(0, workspace_limit + step, step):
        for j in np.arange(0, workspace_limit + step, step):
            for k in np.arange(0, workspace_limit + step, step):
                point = i * vectors[0] + j * vectors[1] + k * vectors[2]
                # inbound
                if np.all(point >= 0) and np.all(point <= workspace_limit):
                    points.append(point)
    return np.array(points)

def visualize_workspace(vectors, points, workspace_limit):
    # Create a 3D plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the robotic arm direction vectors
    ax.quiver(0, 0, 0, vectors[0][0], vectors[0][1], vectors[0][2], color='r', label='Arm 1')
    ax.quiver(0, 0, 0, vectors[1][0], vectors[1][1], vectors[1][2], color='g', label='Arm 2')
    ax.quiver(0, 0, 0, vectors[2][0], vectors[2][1], vectors[2][2], color='b', label='Arm 3')

    #reachable points
    if len(points) > 0:
        ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='black', s=1, alpha=0.6, label='Reachable Points')

    #workspace
    r = [0, workspace_limit]
    for s, e in combinations(np.array(list(product(r, r, r))), 2):
        if np.sum(np.abs(s - e)) == workspace_limit:
            ax.plot3D(*zip(s, e), color="gray", linestyle='dashed', alpha=0.7)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Reachable Points and Workspace Visualization')
    ax.legend()

    plt.show()

def get_input_vectors():
    v1 = list(map(float, input("vector 1 (x, y, z): ").split()))
    v2 = list(map(float, input("vector 2 (x, y, z): ").split()))
    v3 = list(map(float, input("vector 3 (x, y, z): ").split()))
    return np.array([v1, v2, v3])

def main():
    vectors = get_input_vectors()
    
    if check_if_span_space(vectors):
        print("span the entire 3D space.")
    else:
        print("do not span the entire 3D space.")

    workspace_limit = 100
    step = 1  
    points = generate_reachable_points(vectors, step=step, workspace_limit=workspace_limit)
    
    visualize_workspace(vectors, points, workspace_limit)

if __name__ == "__main__":
    main()
