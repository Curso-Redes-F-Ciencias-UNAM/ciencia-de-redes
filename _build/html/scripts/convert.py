#! /bin/python3

# script para convertir archivos gexf a json
import networkx as nx
import json

path = "./gexf/836.gexf"

G = nx.read_gexf(path)
json_obj = json.dumps(nx.node_link_data(G), indent=4)

with open("toy-stoy.json", "w") as salida:
    salida.write(json_obj)
