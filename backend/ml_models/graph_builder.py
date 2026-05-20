import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

banks = [
    "JPM",
    "GS",
    "MS",
    "BAC"
]

for bank in banks:
    G.add_node(bank)

G.add_edge("JPM", "GS", weight=0.82)
G.add_edge("JPM", "MS", weight=0.74)
G.add_edge("GS", "BAC", weight=0.65)

nx.draw(
    G,
    with_labels=True
)

plt.show()