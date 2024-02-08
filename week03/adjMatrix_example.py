from adjacency import Matrix

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
