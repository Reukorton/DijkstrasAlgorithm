import random
import networkx as nx
import matplotlib.pyplot as plt

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

    def draw_graph(self):
        """Отрисовка ориентированного графа без петель и кратных рёбер"""

        size = self.size
        G = nx.DiGraph()  # ОРИЕНТИРОВАННЫЙ граф
        G.add_nodes_from(range(size))

        # Сбор рёбер из верхней диагонали
        for i in range(size):
            for j in range(i + 1, size):
                weight = self.matrix[i][j]
                if weight > 0:
                    G.add_edge(i, j, weight=weight)

        pos = nx.circular_layout(G)

        # Рисуем вершины
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=400)
        nx.draw_networkx_labels(G, pos, font_size=12)

        # Рисуем рёбра с весами
        nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowsize=20, width=1.5)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title("Ориентированный граф")
        plt.axis('off')
        plt.show()
