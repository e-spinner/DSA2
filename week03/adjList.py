class List( object ):
    # Constructor to initialize the graph with given size and city names
    def __init__( self, size, names ):
        self.size = size
        self.names = names
        self.list = {}  # Dictionary to store adjacency lists for each city
        # Populate the dictionary with empty lists for each city
        for i in range( self.size ):
            self.list[ self.names[i] ] = []
        
    # Method to add a connection between two cities
    def add( self, start, end, weight, isTwoWay=False ):
        # Add the end city and weight to the adjacency list of the start city
        self.list[ self.names[ self.names.index( start ) ] ].append( [ end, weight ] )
        if isTwoWay:
            # If two-way connection, also add a reciprocal connection
            self.list[ self.names[ self.names.index( end ) ] ].append( [ start, weight ] )
    
    # Method to remove a connection between two cities
    def remove( self, start, end ):
        # Get the adjacency list of the start city
        connections = self.list[ self.names[ self.names.index( start ) ] ]
        for connection in connections:
            if connection[0] == end:
                # Remove the connection if found
                connections.remove( connection )
                break
            
    # Method to print the graph
    def print(self):        
        for city, connections in self.list.items():
            # Print city name with padding for alignment
            print( city, end=" " )
            for i in range( 10 - len( city ) ):
                print(" ", end="")
            for connection in connections:
                # Print connection in format "city(weight)"
                print( '-> ', end=" ")
                out = f"{{}}({{}})".format( connection[0], connection[1] )
                print( out, end=" " )
                for i in range( 15 - len( out ) ):
                    print(" ", end="")
            print()
             
                
graph = List( 7, ['Atlanta', 'Austin', 'Chicago', 'Dallas', 'Denver', 'Houston', 'Washington'] )
# Add connections between cities with specified weights
graph.add( 'Atlanta', 'Washington', 600, True)
graph.add( 'Atlanta', 'Houston', 800, True)
graph.add( 'Austin', 'Dallas', 200, True)
graph.add( 'Austin', 'Houston', 160)
graph.add( 'Chicago', 'Denver', 1000, True)
graph.add( 'Dallas', 'Chicago', 900)
graph.add( 'Dallas', 'Denver', 780)
graph.add( 'Denver', 'Atlanta', 1400)
graph.add( 'Washington', 'Dallas', 1300)
# Print the graph
graph.print()
