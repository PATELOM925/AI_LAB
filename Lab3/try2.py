# A* Algorithm
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
            if n is None or g[i] + h(i) > g[n] + h(n):
                n = i

        if n == target or all_nodes[n] is None:
            break
        else:
            for next, w in neighbour(n):
                if next not in open_list and next not in closed_list:
                    open_list.append(next)
                    parent[next] = n
                    g[next] = g[n] + w
                elif g[next] > g[n] + w:
                    g[next] = g[n] + w
                    parent[next] = n
                    if next in closed_list:
                        closed_list.remove(next)
                        open_list.append(next)

            open_list.remove(n)
            closed_list.append(n)

    if n is None:
        print('Path Doesn\'t Exist')
        return None

    if n == target:
        path = [target]
        while parent[target] != target:
            path.append(parent[target])
            target = parent[target]
        path.reverse()
        print('Path found: {}'.format(path))
        return path
    

    print('No Path')
    return None


def h(i):
    h_n = {
        'A': 2,
        'B': 5,
        'C': 0,
        'D': 4,
        'E': 7
    }
    return h_n[i]


def neighbour(i):
    if i in all_nodes:
        return all_nodes[i]
    else:
        return None


all_nodes = {
    'A': [('B', 2), ('D', 6)],
    'B': [('C', 3), ('E', 6)],
    'C': [('D', 9)],
    'D': [('E', 5)],
    'E': None
    
}

Astar('E', 'D')
