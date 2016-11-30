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

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

            file = open('dfs.txt', 'w')
            file.write(str(visited))
            file.close
            
    return visited

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

            file = open('bfs.txt', 'w')
            file.write(str(visited))
            file.close
            
    return visited

        


g = {'A': set(['B', 'C']),
     'B': set(['A', 'C']),
     'C': set(['A']),
     'E': set(['B','C'])
     
    }


         
graph = Graph(g)
print(graph.node())
print(graph.edges())
graph.add_node('Z')
print(graph.node())

nodes = graph.node()
print(dfs(g,'A'))
print(bfs(g,'E'))
graph.add_edge({'Z', 'A'})
print(graph.edges())
