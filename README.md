## Sensor Network Project

This project simulates a sensor network where nodes collect data and a mobile robot collects this data for analysis. The goal is to optimize the energy consumption of both the sensors and the robot. 

### Program Compilation and Execution

1. Compilation: This Python program does not require explicit compilation. It can be run directly using a Python interpreter (version 3.x recommended).

2. Execution: Run the program from your terminal or command prompt using the following command:

   sensor_network_tsp_solver.py

   You will be prompted to provide the following inputs:

   - Width and height of the sensor network area
   - Number of sensor nodes
   - Transmission range
   - Range of data packets per node
   - Graph structure ('a' for adjacency matrix, 'b' for adjacency list)
   - Traversal method ('a' for BFS, 'b' for DFS) - This part seems not implemented in the code yet.


### Energy Consumption Analysis

- Robot vs. Algorithms: In general, the MST approximation algorithm is likely to consume less energy for the robot than the greedy algorithm. This is because the MST approximation aims to minimize the total distance traveled, while the greedy algorithm may make locally optimal choices that lead to longer overall paths.

- Sensor vs. Robot: The energy consumption of the sensors is typically much lower than the robot's. Sensors primarily consume energy during data transmission, while the robot consumes energy for movement and data collection. However, this can vary depending on the network size, the number of data packets, and the distances between nodes.

## Test Case
The program has been tested with the following test cases:

# Test Case 1:

$ python sensor_network_tsp_solver.py
Enter the width of the sensor network (e.g., 100): 100
Enter the height of the sensor network (e.g., 100): 100
Enter the number of sensor nodes (e.g., 50): 50
Enter the transmission range in Meters (e.g., 15): 15
Enter the range of number of data packets at sensor node (min, max) (e.g., 1,5): 2,4
Enter the graph structure ('a' for adjacency matrix, 'b' for adjacency list): a
Enter the traversal method ('a' for BFS, 'b' for DFS): b
Components: [{0, 33, 2, 3, 4, 35, 16, 21, 31}, {1, 34, 42, 12, 44, 27}, {8, 18, 5, 23}, {36, 38, 6, 9, 10, 11, 45, 49, 20, 30}, {37, 7, 40, 13, 14, 46, 48, 28}, {32, 43, 47, 15, 22, 24}, {17, 19, 39}, {25}, {26, 29}, {41}]
Representative nodes for each component: [3, 42, 18, 10, 40, 22, 19, 25, 26, 41]
Greedy TSP Path for representative nodes: [3, 41, 10, 22, 18, 40, 19, 42, 26, 25, 3]
MST Approximation TSP Path for representative nodes: [3, 41, 10, 40, 18, 22, 25, 26, 42, 19, 3]


# Test Case 2:

$ python sensor_network_tsp_solver.py
Enter the width of the sensor network (e.g., 100): 100
Enter the height of the sensor network (e.g., 100): 100
Enter the number of sensor nodes (e.g., 50): 50
Enter the transmission range in Meters (e.g., 15): 15
Enter the range of number of data packets at sensor node (min, max) (e.g., 1,5): 2,4
Enter the graph structure ('a' for adjacency matrix, 'b' for adjacency list): b
Enter the traversal method ('a' for BFS, 'b' for DFS): b
Components: [{0, 39, 43, 21, 23}, {1, 4, 6, 8, 9, 10, 12, 13, 14, 16, 18, 22, 24, 26, 28, 29, 31, 34, 35, 37, 38, 40, 45, 46, 47, 48, 49}, {33, 3, 36, 5, 7, 41, 42, 11, 19, 27}, {17, 20, 30, 15}, {32, 44}]
Representative nodes for each component: [0, 9, 36, 20, 32]
Greedy TSP Path for representative nodes: [0, 9, 36, 32, 20, 0]
MST Approximation TSP Path for representative nodes: [0, 9, 36, 32, 20, 0]


# Test Case 3:

$ python sensor_network_tsp_solver.py
Enter the width of the sensor network (e.g., 100): 100
Enter the height of the sensor network (e.g., 100): 100
Enter the number of sensor nodes (e.g., 50): 50
Enter the transmission range in Meters (e.g., 15): 15
Enter the range of number of data packets at sensor node (min, max) (e.g., 1,5): 2,4
Enter the graph structure ('a' for adjacency matrix, 'b' for adjacency list): a
Enter the traversal method ('a' for BFS, 'b' for DFS): b
Components: [{0, 32, 36, 40, 8, 12, 45, 19}, {1, 2, 33, 35, 37, 6, 34, 42, 47, 16, 17, 18, 21, 22, 23, 25, 26, 31}, {3, 39}, {24, 4}, {5, 10, 13, 14, 15, 49, 27, 28}, {44, 29, 46, 7}, {9}, {48, 11}, {20}, {30}, {41, 38}, {43}]
Representative nodes for each component: [32, 33, 3, 24, 13, 29, 9, 48, 20, 30, 41, 43]
Greedy TSP Path for representative nodes: [32, 9, 48, 33, 3, 43, 24, 20, 29, 13, 41, 30, 32]
MST Approximation TSP Path for representative nodes: [32, 9, 41, 13, 29, 43, 24, 20, 3, 33, 48, 30, 32]


# Test Case 4:

$ python sensor_network_tsp_solver.py
Enter the width of the sensor network (e.g., 100): 100
Enter the height of the sensor network (e.g., 100): 100
Enter the number of sensor nodes (e.g., 50): 50
Enter the transmission range in Meters (e.g., 15): 15
Enter the range of number of data packets at sensor node (min, max) (e.g., 1,5): 2,4
Enter the graph structure ('a' for adjacency matrix, 'b' for adjacency list): b
Enter the traversal method ('a' for BFS, 'b' for DFS): a
Components: [{0, 2, 4, 5, 6, 7, 10, 14, 15, 17, 18, 21, 22, 24, 25, 26, 28, 29, 30, 31, 33, 35, 36, 39, 44, 47, 48}, {1, 3, 37, 40, 43, 11, 13, 49, 23}, {8, 41}, {9, 38}, {16, 32, 12}, {42, 20}]
Representative nodes for each component: [21, 3, 8, 38, 32, 42]
Greedy TSP Path for representative nodes: [21, 8, 38, 42, 3, 32, 21]
MST Approximation TSP Path for representative nodes: [21, 8, 38, 42, 3, 32, 21]


# Test Case 5:

$ python sensor_network_tsp_solver.py
Enter the width of the sensor network (e.g., 100): 100
Enter the height of the sensor network (e.g., 100): 100
Enter the number of sensor nodes (e.g., 50): 20
Enter the transmission range in Meters (e.g., 15): 5
Enter the range of number of data packets at sensor node (min, max) (e.g., 1,5): 2,3
Enter the graph structure ('a' for adjacency matrix, 'b' for adjacency list): a
Enter the traversal method ('a' for BFS, 'b' for DFS): b
Components: [{0}, {16, 1}, {2}, {3}, {18, 4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {17}, {19}]
Representative nodes for each component: [0, 1, 2, 3, 18, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 19]
Greedy TSP Path for representative nodes: [0, 9, 13, 12, 11, 6, 3, 5, 18, 10, 17, 7, 19, 1, 8, 2, 14, 15, 0]
MST Approximation TSP Path for representative nodes: [0, 9, 13, 11, 6, 3, 5, 8, 2, 14, 15, 1, 19, 18, 10, 7, 17, 12, 0]



### Extra Credit

The extra credit task of visualizing the data-collecting routes for both the greedy and approximation algorithms has been completed. The visualization is included in the screenshots section of this README.

## Contributions
- Varshith Kumar Reddy Kalakota & Naushik Beladiya: All code implementation.
- Varshith Kumar Reddy Kalakota & Naushik Beladiya: README and documentation.
