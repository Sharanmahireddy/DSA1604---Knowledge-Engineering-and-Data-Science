import networkx as nx

G = nx.DiGraph()
G.add_edge("Smartphone", "Device", relation="is-a")
G.add_edge("Smartphone", "Battery", relation="has-part")
G.add_edge("Smartphone", "Camera", relation="has-part")
G.add_edge("Camera", "Zoom", relation="has-property")

for u, v, d in G.edges(data=True):
    print(u, "--", d["relation"], "-->", v)
