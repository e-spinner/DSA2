import numpy as np
import heapq
       
def dijkstra( graph, source, destination ) :
    V = graph.size
    
    dist = np.full( V, np.inf )
    prev = np.full( V, -1 )
    
    pq = []
    
    dist[source] = 0
    heapq.heappush( pq, ( 0, source ) )
    
    while len( pq ) != 0 :
        current = pq.get().vertex
        heapq.heappop( pq )
        
        for neighbor in graph[current] :
            compare = neighbor.vertex
            weight = neighbor.distance
            
            if dist[current] != np.inf and dist[current] + weight < dist[compare] :
                
                dist[compare] = dist[current] + weight
                prev[compare] = current
                heapq.heappush( pq, weight, compare )
            
    path = []
    v = destination
    
    while v != -1 :
        path.append( v )        
        v = prev[v]
        
    return path.reverse()

from adjacency import List

