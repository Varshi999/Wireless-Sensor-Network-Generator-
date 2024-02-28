import numpy as np
import sys
import queue
import networkx as nx
import matplotlib.pyplot as plt

def create_sensor_network(x, y, N, Tr):
    # Generate random sensor nodes
    nodes = np.random.rand(N, 2) * np.array([x, y])
    
    # Create adjacency matrix or adjacency list
    adjacency = np.zeros((N, N))
    for i in range(N):
        for j in range(i+1, N):
            dist = np.linalg.norm(nodes[i] - nodes[j])
            if dist <= Tr:
                adjacency[i, j] = 1
                adjacency[j, i] = 1
                
    return nodes, adjacency

def bfs(adjacency):
    visited = set()
    connected_components = []
    for node in range(len(adjacency)):
        if node not in visited:
            component = []
            q = queue.Queue()
            q.put(node)
            visited.add(node)
            while not q.empty():
                current = q.get()
                component.append(current)
                for neighbor, connected in enumerate(adjacency[current]):
                    if connected == 1 and neighbor not in visited:
                        q.put(neighbor)
                        visited.add(neighbor)
            connected_components.append(component)
    return connected_components

def dfs(adjacency):
    visited = set()
    connected_components = []
    for node in range(len(adjacency)):
        if node not in visited:
            component = []
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in visited:
                    component.append(current)
                    visited.add(current)
                    for neighbor, connected in enumerate(adjacency[current]):
                        if connected == 1 and neighbor not in visited:
                            stack.append(neighbor)
            connected_components.append(component)
    return connected_components

def print_connected_components(connected_components):
    print("Connected Components:")
    for i, component in enumerate(connected_components):
        print(f"Component {i+1}: {component}")

def main():
    if len(sys.argv) == 7:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        N = int(sys.argv[3])
        Tr = float(sys.argv[4])
        graph_structure = sys.argv[5]
        traversal_method = sys.argv[6]
    else:
        print("Welcome to Wireless Sensor Network Generator and Connected Component Finder!")
        x = int(input("Enter width (x) of the sensor network (e.g., 50): "))
        y = int(input("Enter length (y) of the sensor network (e.g., 50): "))
        N = int(input("Enter number of sensor nodes (e.g., 50): "))
        Tr = float(input("Enter transmission range in meters (e.g., 15): "))
        while True:
            graph_structure = input("Enter graph structure ('a' for adjacency matrix, 'b' for adjacency list): ")
            if graph_structure in ['a', 'b']:
                break
            else:
                print("Invalid input. Please enter 'a' or 'b'.")

        while True:
            traversal_method = input("Enter traversal method ('a' for BFS, 'b' for DFS): ")
            if traversal_method in ['a', 'b']:
                break
            else:
                print("Invalid input. Please enter 'a' or 'b'.")

    nodes, adjacency = create_sensor_network(x, y, N, Tr)
    
    if graph_structure == 'a':
        print("Adjacency Matrix:")
        print(adjacency)
    elif graph_structure == 'b':
        print("Adjacency List:")
        for i, row in enumerate(adjacency):
            neighbors = [j for j, val in enumerate(row) if val == 1]
            print(f"Node {i+1}: {neighbors}")
    
    if traversal_method == 'a':
        connected_components = bfs(adjacency)
    elif traversal_method == 'b':
        connected_components = dfs(adjacency)
    
    print_connected_components(connected_components)

    # Create a graph from adjacency matrix
    G = nx.Graph()
    for i in range(len(nodes)):
        G.add_node(i, pos=(nodes[i][0], nodes[i][1]))
    for i in range(len(adjacency)):
        for j in range(i+1, len(adjacency)):
            if adjacency[i][j] == 1:
                G.add_edge(i, j)

    # Draw the graph
    pos = nx.get_node_attributes(G, 'pos')
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, with_labels=True, node_size=300, node_color='skyblue', font_size=8, font_weight='bold')
    plt.title("Sensor Network with IDs")
    plt.show()  # Display the plot interactively
    plt.savefig("sensor_network.png")  # Save the plot as an image
    plt.close()

if __name__ == "__main__":
    main()
