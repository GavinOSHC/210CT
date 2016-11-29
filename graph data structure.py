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

    def dfs(self,v):
        s = []
        visited = []
        s.append(v)
        while not len(s) == 0:
            u = s.pop()
            if u not in visited:
                visited.append(u)
                s.extend([x for x in g[u] if x  not in visited])

        file = open("dfs.txt","w")
        file.write(str(visited))
        file.close
        return visited


    def bfs(self,v):
        q = []
        visited = []
        q.append(v)
        while not len(q) == 0:
            u = q.pop()
            if u not in visited:
                visited.append(u)
                q.extend([x for x in g[u] if x  not in visited])
    
        file = open("bfs.txt","w")
        file.write(str(visited))
        file.close
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
