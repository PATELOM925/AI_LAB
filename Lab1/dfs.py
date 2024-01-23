def dfs(visited,graph,node):
    # Function to perform DFS traversal.
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
            
 
 
visited = [] # List to keep track of visited nodes.         
s = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

             
print("Performing DFS")
dfs(visited,s,'5')                    