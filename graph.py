from edge import Edge
from node import Node

class Graph:
    def __init__(self):
        self.nodes = {}  # Maps node id to Node object
        self.edges = []  # List of all Edge objects

    def add_node(self, node_id):
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id)

    def add_edge(self, from_id, to_id, capacity):
        # Ensure both nodes exist
        self.add_node(from_id)
        self.add_node(to_id)

        from_node = self.nodes[from_id]
        to_node = self.nodes[to_id]

        # Create forward and backward (reverse) edges
        forward_edge = Edge(from_node, to_node, capacity)
        backward_edge = Edge(to_node, from_node, 0)  # Reverse edge has 0 initial capacity

        # Link the reverse edges to each other
        forward_edge.reverse = backward_edge
        backward_edge.reverse = forward_edge

        # Add to each node's edge list
        from_node.edges.append(forward_edge)
        to_node.edges.append(backward_edge)

        # Add both to the graph's edge list
        self.edges.append(forward_edge)
        self.edges.append(backward_edge)


    def get_node(self, node_id):
        return self.nodes.get(node_id)
    
    # Graph printing
    def __repr__(self):
        nodes = ', '.join(map(str, self.nodes.keys()))
        edge_descriptions = [
            f"{e.from_node.id} -> {e.to_node.id} (cap: {e.capacity})"
            for e in self.edges if e.capacity > 0  # Skip reverse edges with 0 capacity
        ]
        return f"Nodes: {nodes}\nEdges:\n" + "\n".join(edge_descriptions)