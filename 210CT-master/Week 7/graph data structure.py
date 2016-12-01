class Graph():
    def __init__(self, graph_list):
        """ initalising the graph
        if no dictionary is given or the dictionary is none
        set new dictionary

        """

        if graph_list == None:
            graph_list = {}
        self.graph_list = graph_list

    def node(self):
        return list(self.graph_list.keys()) #returning the node of the graph

    def edges_create(self):
        """ here we creat the edges of the graph
            the edges are represented by one or two nodes
            looping through the graph with the node add the
            edge to the node with th neidhbouring node
        """
        edges = []

        for node in self.graph_list:
            for neighbour in self.graph_list[node]:
                if {neighbour, node} not in edges:
                    edges.append({node, neighbour})

        return edges

    def edges(self):
        return self.edges_create()# return the edges of the graph


    def add_node(self, node):
        """ if the node is not in the graph list
            add the node to the dictionary
        """
        if node not in self.graph_list:
            self.graph_list[node] = []

    def add_edge(self, edge):
        """ we set edge as a set and then set node1 as
            and node2 as a tuple, then if node1 in graph
            list append node2 as an edge to that node
        """        
        edge = set(edge)
        (node1, node2) = tuple(edge)
        if node1 in self.graph_list:
            self.graph_list[node1].add(node2)
        else:
            self.graph_list[node1] = [node2]

def dfs(graph, start):
    """DEPTH-FIRST-SEARCH (G, v)
         S←new Stack()
         visited←[]
         S.push(v)
         WHILE S is not empty
              u←S.pop()
              IF u is not in visited
                   visited.append(u)
                   FOR all edges, e, from u, S.push(e.to)
         RETURN visited
    """
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

            file = open('dfs.txt', 'w') #open and create 
            file.write(str(visited))    #write to a file
            file.close                  #close the file
            
    return visited

def bfs(graph, start):
    """BREADTH-FIRST-SEARCH(G,v)
         Q←new Queue()
         visited←[]
         Q.enqueue(v)
         WHILE Q is not empty
            u←q.dequeue()
            IF u is not in visited
            visited.append(u)
            FOR all edges, e, from u
                  Q.enqueue(e.to)
         RETURN visited
 """
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

            file = open('bfs.txt', 'w') #open file and set to write
            file.write(str(visited))    #write to file
            file.close                  #close the file
            
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
#graph.add_edge({'Z', 'A'})
#print(graph.edges())
