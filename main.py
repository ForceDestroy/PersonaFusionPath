import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
from persona import Persona

class Main():
    def __init__(self, persona_dict, graph, counter, labels):
        self.persona_dict = persona_dict
        self.graph = graph
        self.counter = counter
        self.labels = labels

def main():
    persona_dict = fileIO()
    graph = nx.Graph()
    labels = {}
    
    m = Main(persona_dict, graph, 0, labels)

    inp = input()

    if inp in m.persona_dict:
        inp += "-" + str(0)
        generationDown(m, None, inp)
    
    G = m.graph
    pos = graphviz_layout(G, prog="dot")
    nx.draw(G, pos, node_size=[len(v) * 200 for v in G.nodes()], node_shape='s', node_color='white', with_labels=False)
    nx.draw_networkx_labels(G, pos, m.labels)
    plt.show()

def fileIO() -> dict:
    persona_dict = dict()

    with open("personas.txt", "r") as file:
        for line in file:
            level = int(line[:2])
            name = line.partition("{")[0][3:-1]
            
            fusions = []
            _temp = line.partition("{")[2][:-2].split(",")
            for value in _temp:
                recipe = []
                value = value[1:-1]
                values = value.split(" + ")
                for i in range(len(values)):
                    values[i] = values[i][1:-1]
                    recipe.append(values[i])
                fusions.append(recipe)
            
            persona = Persona(name, level, fusions)
            
            persona_dict[persona.name] = persona
    return persona_dict

def generationDown(m, parent, persona):
    _temp = persona.split("-")[0]
    m.labels[persona] = _temp
    p = m.persona_dict[_temp]
    m.graph.add_node(persona)

    if parent:
        m.graph.add_edge(parent, persona)

    m.counter += 1

    for recipe in p.fusions:
        _recipe = " + ".join(recipe) + "-" + str(m.counter)
        m.labels[_recipe] = " + ".join(recipe)
        m.graph.add_node(_recipe)
        m.graph.add_edge(_recipe, persona)
        m.counter += 1

        for component in recipe:
            _label = component + "-" + str(m.counter)
            m.labels[_label] = component
            m.graph.add_node(_label)
            m.graph.add_edge(_label, _recipe)
            # counter +=1

            if component == "Arsene" or component == "Jack-O-Lantern" or component == "Pixie":
                continue
            
            child = m.persona_dict[component].name + "-" + str(m.counter)
            generationDown(m, _label, child)
            m.counter += 1
    
if __name__ == "__main__":
    main()

