import heapq

def prims(graph, start):
    mst = set()
    visited = {start}  # Corrected visited initialization
    heap = []
    
    # Push all edges from the start node into the heap
    for weight, neighbor in graph[start]:
        heapq.heappush(heap, (weight, start, neighbor))
    
    while heap:
        weight, parent, neighbor = heapq.heappop(heap)
        
        # If the neighbor is not visited, we add it to the MST
        if neighbor not in visited:
            visited.add(neighbor)
            mst.add((parent, neighbor, weight))
            
            # Add all edges from the new node into the heap
            for edge_weight, child in graph[neighbor]:
                if child not in visited:
                    heapq.heappush(heap, (edge_weight, neighbor, child))
    
    # Return the sorted MST based on first alphabetical edge
    return sorted(mst, key=lambda x: x[0])

# Example graph
graph = {
    'A': [(4, 'B'), (2, 'C')],
    'B': [(4, 'A'), (5, 'C'), (10, 'D')],
    'C': [(2, 'A'), (5, 'B'), (3, 'D')],
    'D': [(10, 'B'), (3, 'C')]
}

# Running Prim's algorithm starting from node 'A' and sorting by the edge weight
print(prims(graph, 'A'))

