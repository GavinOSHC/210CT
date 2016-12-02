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
          """ DFS on a graph by visiting each vertex
              finds the first edge fot the vertext given
              loop through the egdes until the next unvisited vertex
              marks the vertex as visited and then keeps going
              until all vertices are in visited.
          """
          stack = []     #initalising the dfs with a stack
          visited = []
          stack.append(v)
          while len(stack) != 0:   #loops throught the graph using the first item in the stack
               u = stack.pop()
               if u not in visited:     
                    visited.append(u)   # add that vertex to visited
                    for edge in self.graph_dic[u]: #loop through the edge connected to that vertex and add edge to the stack
                         stack.append(edge)

                    #writing to a file    
                    file = open("dfs.txt","w")
                    file.write(str(visited))
                    file.close

          return visited

     def bfs(self,v):
          """ BFS on a graph by by visiting each edge from
              the vertex given. Only moves onto the next vertex in the
              graph once all the edges have been visited.
              Very similar to DFS but a queue is used instead of stack 
          """
          queue = []     #creating a queue
          visited = []
          queue.insert(0,v)
          while len(queue) != 0:    #loops through the graph using the start value
               u = queue.pop()     
               if u not in visited:     
                    visited.append(u)   #add the vertex to visited 
                    for edge in self.graph_dic[u]: #loops through the edges connect to that vertex and insert it into the queue 
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
