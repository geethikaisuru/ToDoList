



from collections import defaultdict, deque
from itertools import combinations

def find_steiner_tree_sum(n, weights, edges):
    MOD = 10**9 + 99999
    
    # Build adjacency list representation of tree
    graph = defaultdict(list)
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    def getpathf(start, end, parent):
        if start == end:
            return {start}
        
        queue = deque([start])
        visited = {start}
        found = False
        
        while queue and not found:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = curr
                    queue.append(neighbor)
                    if neighbor == end:
                        found = True
                        break
        
        # econstruct path
        path_nodes = {end}
        curr = end
        while curr != start:
            curr = parent[curr]
            path_nodes.add(curr)
        
        return path_nodes
    
    result = []
    for k in range(1, n+1):
        total = 0
        for subset in combinations(range(n), k):
            steiner_nodes = set()
            for i in range(len(subset)):
                for j in range(i+1, len(subset)):
                    parent = {}
                    path_nodes = getpathf(subset[i], subset[j], parent)
                    steiner_nodes.update(path_nodes)
            
            if len(subset) == 1:
                steiner_nodes = {subset[0]}
            
            tree_weight = sum(weights[node] for node in steiner_nodes)
            total = (total + tree_weight) % MOD
            
        result.append(total)
    
    return result

def main():
    n = int(input())
    
    weights = list(map(int, input().split()))
    
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    result = find_steiner_tree_sum(n, weights, edges)
    for ans in result:
        print(ans)

if __name__ == "__main__":
    main()