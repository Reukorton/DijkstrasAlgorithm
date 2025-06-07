from graph import Graph

if __name__ == "__main__":
    graph = Graph()
    graph.print_matrix()
    graph.draw_graph()

    start = int(input("Начальная вершина: "))
    distances, predecessors = graph.dijkstra(start)

    print("\nКратчайшие расстояния:")
    for i, d in enumerate(distances):
        print(f"{start} -> {i} = {d if d != float('inf') else '∞'}")