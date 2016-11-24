class Graph():
    def __init__(self, graph_list):
        """ initalising the graph"""

        if graph_list == None:
            graph_list = {}
        self.graph_list = graph_list

    def node(self):
        return list(self.graph_list.keys())

    def edges_create(self):
        edges = []

        for node in self.graph_list:
            for neighbour in self.graph_list[node]:
                if {neighbour, node} not in edges:
                    edges.append({node, neighbour})

        return edges

    def edges(self):
        return self.edges_create()


    def add_node(self, node):
        if node not in self.graph_list:
            self.graph_list[node] = []

    def add_edge(self, edge):
        edge = set(edge)
        (node1, node2) = tuple(edge)
        if node1 in self.graph_list:
            self.graph_list[node1].append(node2)
        else:
            self.graph_list[node1] = [node2]

def dfs(g,v):
    s = []
    visited = []
    s.append(v)
    while not len(s) == 0:
        u = s.pop()
        if u not in visited:
            visited.append(u)
            s.extend([x for x in g[u] if x  not in visited])
    return visited
        


g = { "a" : ["b"],
      "b" : ["c"],
      "c" : ["a", "b"]
    }

graph = Graph(g)
print(graph.node())
print(graph.edges())
graph.add_node("s")
print(graph.node())
graph.add_edge({"a", "s"})
print(graph.edges())
nodes = graph.node()
print(dfs(g,"a"))



#http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
#http://www.python-course.eu/graphs_python.php


