import random
from graph import Graph

class GraphGenerator:
    def __init__(self, num_nodes, edge_probability, min_capacity, max_capacity):
        self.num_nodes = num_nodes
        self.edge_probability = edge_probability
        self.min_capacity = min_capacity
        self.max_capacity = max_capacity

    def generate(self):
        graph = Graph()
        source = 0
        sink = self.num_nodes - 1

        # Add all nodes to the graph
        for node_id in range(self.num_nodes):
            graph.add_node(node_id)

        # Added edges are unique
        added_edges = set()

        # Create one guaranteed path from source through random order of nodes to sink
        path_nodes = [source] + random.sample(range(1, sink), self.num_nodes - 2) + [sink]
        for i in range(len(path_nodes) - 1):
            u, v = path_nodes[i], path_nodes[i + 1]
            capacity = random.randint(self.min_capacity, self.max_capacity)
            graph.add_edge(u, v, capacity)
            # Keep track of already added edges
            added_edges.add((u, v))

        # --- STEP 2: Add random edges ---
        possible_edges = [
            (u, v)
            for u in range(self.num_nodes)  # Every node can be a start
            for v in range(self.num_nodes)  # Every node can be an end
            # No edge to self, no edge to source, no edge from sink, and no duplicates
            if u != v and v != source and u != sink and (u, v) not in added_edges
        ]

        # Shuffle possible edges list
        random.shuffle(possible_edges)
        num_edges_to_add = int(len(possible_edges) * self.edge_probability)

        # Add the number of edges from the shuffled list of possible edges
        for u, v in possible_edges[:num_edges_to_add]:
            capacity = random.randint(self.min_capacity, self.max_capacity)
            graph.add_edge(u, v, capacity)

        return graph
