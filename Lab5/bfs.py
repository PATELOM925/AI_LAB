def bfs(a,b,c):
    visited = set()
    queue = [(0,0)]
    
    max_iterations = 10
    
    while queue:
        current = queue.pop(0)
        jug_a , jug_b = current
        
        if jug_a == c or jug_b == c :
            return current
        
        fill_a = (a,jug_b)
        if fill_a not in visited:
            visited.add(fill_a)
            queue.append(fill_a)
            
            
        fill_b = (jug_a,b)    
        if fill_b not in visited:
            visited.add(fill_b)
            queue.append(fill_b)
            
        fill_a_to_b =  (max(0, jug_a - (b - jug_b)), min(b, jug_b + jug_a))
        if fill_a_to_b not in visited:
            visited.add(fill_a_to_b)
            queue.append(fill_a_to_b)
            
        fill_b_to_a = (min(a, jug_a + jug_b), max(0, jug_b - (a - jug_a)))
        if fill_b_to_a not in visited:
            visited.add(fill_b_to_a)
            queue.append(fill_b_to_a)

    return None


def main(a,b,c):
    result = bfs(a,b,c)
    if result:
        print(f"Jug A: {result[0]}, Jug B: {result[1]}")
    else:
        print("Error")    


main(3,5,4)