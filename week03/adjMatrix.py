class Matrix( object ):
    # Constructor to initialize the matrix with given size and city names
    def __init__( self, size, names):
        # Initialize the matrix with all elements set to 0
        self.matrix = []
        for i in range( size ):
            self.matrix.append( [ 0 for i in range( size ) ] )
        self.names = names
        self.size = size
        
    # Method to add a connection between two cities
    def add( self, start, end, weight, isTwoWay=False ):
        # Set the weight at the corresponding position in the matrix
        self.matrix[ self.names.index( start )][ self.names.index( end ) ] = weight
        if isTwoWay:
            # If two-way connection, also set the weight in the opposite direction
            self.matrix[ self.names.index( end ) ][ self.names.index( start ) ] = weight
    
    # Method to remove a connection between two cities
    def remove( self, start, end ):
        # Set the weight at the corresponding position to 0 to indicate no connection
        self.matrix[ self.names.index( start ) ][ self.names.index( end ) ] = 0
    
    # Method to print the adjacency matrix
    def print( self ):
        # Print column headers
        print( '               ', end="" )
        for name in self.names:
            print( name, end="" )
            # Add padding to maintain alignment
            for i in range( 12 - len( name ) ):
                print( ' ', end="" )
        print()
        # Print rows
        for name in self.names:
            print( name, end="" )
            # Add padding to maintain alignment
            for i in range( 11 - len( name ) ):
                print( ' ', end="" )
            print( '->  ', end="" )
            # Print weights for each connection
            for i in range( self.size ):
                out = self.matrix[ self.names.index( name ) ][i]
                print( out, end="" )
                # Add padding to maintain alignment
                for j in range( 12 - len( str( out ) ) ):
                    print( ' ', end="" )
            print()               

# Create a Matrix object with 7 cities and their names
graph = Matrix( 7, ['Atlanta', 'Austin', 'Chicago', 'Dallas', 'Denver', 'Houston', 'Washington'] )
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
# Print the adjacency matrix
graph.print()
