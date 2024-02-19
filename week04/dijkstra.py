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
        current, _ = heapq.heappop( pq )
        
        
        for neighbor in graph.get_adjacency_list(current):
            compare = neighbor.first
            weight = neighbor.second
            
            if dist[current] != np.inf and dist[current] + weight < dist[compare] :
                
                dist[compare] = dist[current] + weight
                prev[compare] = current
                def dijkstra(graph, source, destination):
                    V = graph.size
                    dist = np.full(V, np.inf)
                    prev = np.full(V, -1)
                    pq = []

                    dist[source] =  0
                    heapq.heappush(pq, (0, source))

                    while len(pq) !=  0:
                        current, _ = heapq.heappop(pq)

                        for neighbor in graph.get_adjacency_list(current):
                            compare = neighbor[0]
                            weight = neighbor[1]

                            if dist[current] != np.inf and dist[current] + weight < dist[compare]:
                                dist[compare] = dist[current] + weight
                                prev[compare] = current
                                heapq.heappush(pq, (dist[compare], compare))

        
    print( dist )
    print ( prev )    
    
                
    path = []
    v = destination
    
    while v != -1 :
        path.append( v )        
        v = prev[v]
        
    return path.reverse()

from adjacency import List

# Create a List object with 7 vertexes and their names           
graph = List( 6, ['0', '1', '2', '3', '4', '5'] )
# Add edges with specified weights

graph.add('0', '1', 5, True)
graph.add('0', '4', 1, True)
graph.add('1', '2', 3, True)
graph.add('1', '3', 8, True)
graph.add('1', '5', 4, True)
graph.add('2', '3', 3, True)
graph.add('2', '5', 7, True)
graph.add('4', '5', 2, True)
graph.print()

print( dijkstra( graph, 5, 1))

print( graph.list)