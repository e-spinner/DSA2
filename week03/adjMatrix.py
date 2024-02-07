

class Matrix( object ) :
    
    def __init__( self, size):
        self.matrix = []
        for i in range( size ):
            self.matrix.append( [0 for i in range( size ) ] )
        
    def add( self, a, b ):
        self.matrix[a][b] = 1
    
    def remove( self, a, b ):
        self.matrix[a][b] = 0
    
    def print( self ):
        for row in self.matrix:
            for val in row:
                print( val )