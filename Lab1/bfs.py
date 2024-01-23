def bfs(visited,graph,node):
    # Function to perform BFS traversal.
    queue = []
    visited.append(node)
    queue.append(node)
    
    while queue:
        i = queue.pop(0)
        print(i)
        
        for node in graph[i]:
            if node not in visited:
                visited.append(node)
                queue.append(node)
  
 
                 
visited= []              
# Define another graph using an adjacency list
s = {
    '1': ['2', '4'],
    '2': ['3', '7'],
    '3': ['5'],
    '4': [],
    '5': ['9'],
    '6': ['8'],
    '7': ['6'],
    '8': []
}

# The 's_another' variable represents the graph with the following structure:
# 1 -- 2 -- 3
# |    |    |
# 4    7 -- 5 -- 9
#      |
#      6 -- 8

             
print("Performing BFS")
bfs(visited,s,'1')        