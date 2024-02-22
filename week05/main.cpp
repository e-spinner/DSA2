//  main.cpp
//  DijkstraCode
//
//  Created by Stephany Coffman-Wolph on 2/14/24.
/

#include <iostream> 
#include <vector>   
#include <queue>   
#include <climits>  

using namespace std;

// Structure to represent a vertex and its distance from the source vertex
struct Node {
    int vertex;     // Vertex number
    int distance;   // Distance from the source

    // Constructor for Node struct
    Node(int v, int d) : vertex(v), distance(d) {}
};

// Comparison function for priority queue
struct CompareDistance {
    // Custom comparison for priority queue
    bool operator()(const Node& a, const Node& b) {
        // Compares the distances for priority queue
        return a.distance > b.distance;
    }
};

// Dijkstra's algorithm to find shortest path from source to destination
vector<int> dijkstra(vector<vector<pair<int, int>>>& graph, int source, int destination) {
    int V = (int)graph.size(); // Number of vertices in the graph
    vector<int> dist(V, INT_MAX); // Initialize distances to infinity
    vector<int> prev(V, -1); // Previous vertex in shortest path
    priority_queue<Node, vector<Node>, CompareDistance> pq; // Priority queue for Dijkstra's algorithm

    dist[source] = 0; // Distance from source to itself is 0
    pq.push(Node(source, 0)); // Pushes the source node into priority queue with a distance of 0

    while (!pq.empty()) { // While priority queue is not empty
        int u = pq.top().vertex; // Get the vertex with minimum distance
        pq.pop(); // Remove the vertex from priority queue

        // Iterate through the neighbors of the current vertex
        for (auto& neighbor : graph[u]) {
            int v = neighbor.first; // Neighbor vertex
            int weight = neighbor.second; // Weight of edge between current and neighbor vertex

            // Relaxation
            if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) {
                // If relaxation condition is true, update distance of neighbor vertex
                dist[v] = dist[u] + weight;
                // store previous vertex in shortest path
                prev[v] = u;
                // Push updated vertex into priority queue
                pq.push(Node(v, dist[v]));
            }
        }
    }

    // Construct shortest path
    vector<int> path; // Vector to store the shortest path
    // Trace back from destination to source
    for (int v = destination; v != -1; v = prev[v])
        path.push_back(v); // Add vertex to the path

    // Reverse the path to get it from source to destination
    reverse(path.begin(), path.end());
    // Return the shortest path
    return path;
}

int main() {
    int V, E; // Number of vertices and edges in the graph
    cout << "Enter the number of vertices and edges: ";
    cin >> V >> E; // Input number of vertices and edges

    vector<vector<pair<int, int>>> graph(V); // Adjacency list representation of the graph

    cout << "Enter the edges (source, destination, weight):" << endl;
    for (int i = 0; i < E; ++i) { // Input edges and their weights
        int u, v, w;
        cin >> u >> v >> w; // Input edge (u,v) with weight w
        graph[u].push_back({v, w}); // Add edge to graph
        //graph[v].push_back({u, w}); // For undirected graph, include this line as well
    }

    int source, destination; // Source and destination vertices for shortest path
    cout << "Enter source and destination vertices: ";
    cin >> source >> destination; // Input source and destination vertices

    vector<int> shortestPath = dijkstra(graph, source, destination); // Find shortest path

    cout << "Shortest path from " << source << " to " << destination << " is: ";
    for (int vertex : shortestPath) // Output the shortest path
        cout << vertex << " ";
    cout << endl;

    return 0; // Exit main function
}
