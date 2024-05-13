#A* ALgorithm
# Logic:
# 1. Initialize open_list with the start node.
# 2. Initialize closed_list as an empty list.
# 3. Initialize dictionaries g, parent, and f for storing costs, parents, and total costs.
# 4. While the open_list is not empty:
#    a. Select the node with the lowest total cost from open_list.
#    b. If the selected node is the target or has no neighbors, continue.
#    c. For each neighbor of the selected node:
#       - If the neighbor is not in the open_list or closed_list, add it to open_list and update its cost.
#       - If the neighbor is in the open_list and the new cost is lower, update its cost.
#       - If the neighbor is in the closed_list, remove it from closed_list and add it to open_list.
# 5. Return the last node in the path.

def Astar(start, target):
    open_list = [start]
    closed_list = []
    g = {} 
    parent = {}  
    g[start] = 0 
    parent[start] = start
   

    while len(open_list) > 0:
        n = None
        for i in open_list:
            if n is None or g[i] + h[i] > g[n] + h[n]:
                n = i

        if n == target or all_nodes[i]:
            pass
        else:
            for next,w in neighbour(i):
                if neighbour(i) not in open_list and closed_list:
                    open_list.append(next)
                    parent[next] = i
                    g[next] = g[i] + w
                    
                else: #comparing
                    if g[next] > g[i] + w:
                        g[next] = g[i] + w
                        parent[next] = i
                        
                        #adding next in open list
                        if next in closed_list:
                            closed_list.remove(next)
                            open_list.append(next)
                            
        if n == None :
            print('Path Doesnt Exist')   
            return None
        
        if i == target:
            path = []
            
            while parent[n] != n:
                path.append(n)
                n = parent[n]
                
            path.append(start) 
            path.reverse()
            print('Path found: {}'.format(path))
            return path
                             
            open_list.remove(n)
            closed_list.append(n)  
    
    return None                        

            
            
def h(i): 
        h_n = {
            
            'A' : 2 ,
            'B' : 5 ,
            'C' : 0 ,
            'D' : 4 ,
            'E' : 7
            
        }
        return h_n(i) 
   
  
 
def neighbour(i):
    if i in all_nodes:
        return all_nodes[i]    
    else:
        return None   


all_nodes = {
    'A': [('B',1), ('C',10)],
    'B': [('C', 3), ('E', 6)],
    'C': [('D',9)],
    'D': [('E',5)],
    'E': None
}

Astar('A','C')