class List( object ):
    def __init__( self, size, names ):
        self.size = size
        self.names = names
        self.list = {} 

        for i in range( self.size ):
            self.list[ self.names[i] ] = []
    
    # Method to add a connection between two cities
    def add( self, start, end, weight ):
        self.list[ self.names[ self.names.index( start ) ] ].append( [ end, weight ] )
        self.list[ self.names[ self.names.index( end ) ] ].append( [ start, weight ] )
    
    # Method to print the graph
    def print(self):        
        for city, connections in self.list.items():
            # Print vertex name with padding for alignment
            print( str( city ), end=" " )
            for i in range( 5 - len( str( city ) ) ):
                print(" ", end="")
            for connection in connections:
                # Print connection in format "vertex(weight)"
                print( '-> ', end=" ")
                out = f"{{}}({{}})".format( str( connection[0] ), str( connection[1] ) )
                print( out, end=" " )
                for i in range( 5 - len( str( out ) ) ):
                    print(" ", end="")
            print()
            
            # Elijah Spinner and Evan Dinan
             