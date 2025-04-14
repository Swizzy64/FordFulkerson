from graph_generator import GraphGenerator
from ford_fulkerson_solver import FordFulkersonSolver
import time

num_nodes = [6, 10, 50, 100, 200, 500, 900]
edge_probability = 0.3
min_capacity = 1
max_capacity = 10
results = ""

for i in num_nodes:
    generator = GraphGenerator(i, edge_probability, min_capacity, max_capacity)
    graph = generator.generate()
    # Count edges (only forward edges, not reverse used in algo logic)
    num_edges = sum(1 for edge in graph.edges if edge.capacity > 0)

    # Manual test
    # graph = Graph()
    # for node_id in range(6):
    #     graph.add_node(node_id)
    # Manually add the edges with their respective capacities
    # graph.add_edge(0, 1, 3)
    # graph.add_edge(0, 2, 7)
    # graph.add_edge(1, 3, 3)
    # graph.add_edge(1, 4, 4)
    # graph.add_edge(2, 1, 5)
    # graph.add_edge(2, 4, 3)
    # graph.add_edge(3, 4, 3)
    # graph.add_edge(3, 5, 2)
    # graph.add_edge(4, 5, 6)

    solver = FordFulkersonSolver(graph)
    start_time = time.time_ns()
    max_flow = solver.ford_fulkerson(0, i - 1)
    stop_time = time.time_ns()
    elapsed_time = stop_time - start_time

    # Prepare result summary
    summary = (
        f"Number of nodes: {len(graph.nodes)}\n"
        f"Number of edges: {num_edges}\n"
        f"Max flow from 0 to {i - 1}: {max_flow}\n"
        f"Execution time: {elapsed_time / 1000000} miliseconds\n"
        f"{'-'*40}\n"
    )

    results += summary

# Append to log file
with open("ff_results.txt", "a") as file:
    file.write(results)