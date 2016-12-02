class Graph:
     def __init__(self):
          self.graph_dic = {} ##Creating the dictionary

     def add_node(self, node):
          self.graph_dic[node] = []

     def add_edge(self, node1, node2): ##Adding the edge to the node given
          self.graph_dic[node1].append(node2)
          self.graph_dic[node2].append(node1)

     def printing(self): #go through the graph to print all the keys and the values
          for key,value in self.graph_dic.items():
               print(key ,"|", value)
    
     def dfs(self,v):        
          stack = []
          visited = []
          stack.append(v)
          while len(stack) != 0:
               u = stack.pop()
               if u not in visited:
                    visited.append(u)
                    for edge in self.graph_dic[u]:
                         stack.append(edge)

                    #writing to a file    
                    file = open("dfs.txt","w")
                    file.write(str(visited))
                    file.close

          return visited

     def bfs(self,v):
          queue = []
          visited = []
          queue.insert(0,v)
          while len(queue) != 0:
               u = queue.pop()
               if u not in visited:
                    visited.append(u)
                    for edge in self.graph_dic[u]:
                         queue.insert(0,edge)

          #write to a file               
          file = open("bfs.txt","w")
          file.write(str(visited))
          file.close
          
          return visited



g = Graph()

g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,6)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(3,6)
g.add_edge(4,5)
g.add_edge(5,6)

print(g.dfs(1))
print(g.bfs(1))

g.printing()