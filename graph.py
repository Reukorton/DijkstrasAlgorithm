import random
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import os
import datetime

class Graph:
    def __init__(self):
        self.size = int(input("Размерность графа: "))
        self.matrix = [[0 if i < j else None for j in range(self.size)] for i in range(self.size)]
        self.generate_graph()

    def generate_graph(self):
        for i in range(self.size):
            for j in range(i + 1, self.size):
                weight = random.choice([0, random.randint(1, 10)])
                if weight > 0:
                    self.matrix[i][j] = weight

    def get_neighbors(self, node):
        return [(j, self.matrix[node][j]) for j in range(node + 1, self.size) if self.matrix[node][j] > 0]

    def print_matrix(self):
        for row in self.matrix:
            print(["x" if x is None else x for x in row])

    def dijkstra(self, start: int):
        """Алгоритм Дейкстры от вершины start. Возвращает расстояния и предков."""

        dist = [float('inf')] * self.size
        prev = [None] * self.size
        dist[start] = 0

        visited = [False] * self.size
        heap = [(0, start)]  # (расстояние, вершина)

        while heap:
            current_dist, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True

            # Проходим только по выходящим рёбрам
            for v, weight in self.get_neighbors(u):
                if not visited[v] and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    prev[v] = u
                    heapq.heappush(heap, (dist[v], v))

        return dist, prev

    def draw_graph(self):
        """Отрисовка ориентированного графа без петель и кратных рёбер"""

        size = self.size
        G = nx.DiGraph()
        G.add_nodes_from(range(size))


        for i in range(size):
            for j in range(i + 1, size):
                weight = self.matrix[i][j]
                if weight > 0:
                    G.add_edge(i, j, weight=weight)

        pos = nx.circular_layout(G)

        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=400)
        nx.draw_networkx_labels(G, pos, font_size=12)

        nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowsize=20, width=1.5)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title("Ориентированный граф")
        plt.axis('off')
        plt.tight_layout()

        # Сохраняем в ту же папку, где запускается main.py
        save_path = os.path.join(os.getcwd(), "graph.jpg")
        plt.savefig(save_path, dpi=300)
        plt.close()
