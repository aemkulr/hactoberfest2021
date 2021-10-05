# Find the most cost effective path from A to G in the graph using A* Algorithm

# The numbers written on the edges represent the cost between the nodes.
# The numbers written on the nodes represent the heuristic values of the node.

# The function f(n) is defined as sum of g(n) and h(n)
# f(n) = g(n) + h(n)


# Define the Initial and Goal State
initial_node = 'A'
goal_node = 'G'

# Define the Graph structure:
graph_definition = {
                'A': {'B': 2, 'E': 3}, 
                'B': {'C': 1, 'G': 9}, 
                'C': {}, 
                'D': {'G': 1}, 
                'E': {'D': 6}, 
                'G': {}
                }

# Define the Heuritic Function h(n) for each node
heuristic_value = {'A': 11, 'B':6, 'C': 99, 'D': 1, 'E': 7, 'G': 0}


# Definition of find_neighbours function which is used to find the neighbours of the current node
def find_neighbours(current_node):
    if current_node in graph_definition and len(graph_definition[current_node]) > 0:
        return graph_definition[current_node]
    else:
        return None
        

# Definition of the function to perform A* Algorithm
def A_Star_Algorithm(initial_node, goal_node):
    # A Dictionary named Parents is used to keep track of parents of each node
    parents = {}

    # An open set and a closed set is used to keep track of visited and unvisted nodes
    # Open set initially contains the starting node , i.e. the initial_node
    # Close set is initially empty
    open = set(initial_node)
    closed = set()
    
    # A dictionary named g stores the distance or the cost of node n from the starting node
    g = {}
    
    # For initial_node
    # Since the initial_node is the root node, it has no parent
    # So the parent of initial_node is defined as itself.
    # g(initial_node) is defined as the distance of initial node from itself, i.e. 0
    parents[initial_node] = initial_node
    g[initial_node] = 0
    
    # Run a loop till the open set contains an element, as soon as it becomes empty set, the loop stops
    while(len(open) > 0):
        n = None
        
        # Find the node with the smallest f(n) value from the open set
        for i in open:
            if n == None or g[i]+heuristic_value[i] < g[n]+heuristic_value[n]:
                n = i
        
        # The smallest node is stored in n variable
        if n == goal_node or len(graph_definition[n]) == 0:
            pass
        
        else:
            for i in find_neighbours(n):
                # i is the neighbour of n and graph_definition[i] is the cost from n to i
                if i not in open and i not in closed:
                    open.add(i)
                    parents[i] = n
                    g[i] = g[n] + graph_definition[n][i]
                    
                else:
                    # For each neighbouring node of n,
                    # Compare the g() value and update the value if required
                    if g[i] > g[n] + graph_definition[n][i]:
                        g[i] = g[n] + graph_definition[n][i]
                        parents[i] = n
                
                        # Remove i from the closed set and add it to the open set
                        if i in closed:
                            closed.remove(i)
                            open.add(i)
                            
        
                
        # If none of the above operations is performed, and n = None
        if n == None:
            print('Path does not exist between the Initial and the Goal node')
            return
        
        # If the current node is the goal node, then,
        # construct the path from initial to the goal node
        if n == goal_node:
            path = []
            
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            
            path.append(initial_node)
        
            # The path has been constructed
            # Print the path from the start node to the goal node
            print('Path Found:')
            for i in range(len(path)-1,-1,-1):
                if i != 0:
                    print(path[i], '—>', end=" ")
                if i == 0:
                    print(path[i])
            
            # Print the cost of the path
            print('Cost of the Optimal Path:',g[goal_node] + heuristic_value[goal_node])
            return
        
        # Remove node n from the open list and add it to the closed lis
        open.remove(n)
        closed.add(n)
        
    # Path is not found
    print('Path does not exist')
    return
        
        

# Call the A* Algorithm Function on the given graph
A_Star_Algorithm(initial_node, goal_node)
        