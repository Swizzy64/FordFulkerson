class FordFulkersonSolver:
    def __init__(self, graph):
        self.graph = graph

    # Depth First Search to find an augmenting path
    def dfs(self, current_node, sink_id, visited, flow):
        # If you are in sink then return path and flow
        if current_node.id == sink_id:
            return [], flow

        visited.add(current_node.id)

        for edge in current_node.edges:
            residual = edge.residual_capacity()
            if edge.to_node.id not in visited and residual > 0:
                path, bottleneck = self.dfs(edge.to_node, sink_id, visited, min(flow, residual))
                if bottleneck > 0:
                    return [edge] + path, bottleneck

        return None, 0

    # Ford-Fulkerson algorithm to find max flow from source to sink
    def ford_fulkerson(self, source_id, sink_id):
        max_flow = 0

        while True:
            visited = set()
            source_node = self.graph.get_node(source_id)
            path, flow = self.dfs(source_node, sink_id, visited, float('inf'))

            if flow == 0:
                break  # No more augmenting paths

            max_flow += flow
            for edge in path:
                edge.flow += flow
                edge.reverse.flow -= flow

        return max_flow
