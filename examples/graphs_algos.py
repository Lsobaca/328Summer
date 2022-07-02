from collections import defaultdict





class Graph:
    def __init__(self) -> None:
        # makes a dictionary to store graph
        self.graph = defaultdict(list)

    # function to add edges
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # function to print a BFS of a graph
    def bfs(self,s):
        # marks if had went to that node
        visted  = [False]*(len(self.graph))
        # create a queue for bfs
        queue = []

        # marks the source and adds it to the source
        queue.append(s)
        visted[s] = True


        while queue:
            # dequeue a vertex from the queue and prints it
            s = queue.pop(0)
            print(s,end=' ')

            # checks all the adjacent vertices of the dequeue
            # if the adjecent had not been visted then mark it
            for i in self.graph[s]:
                if visted[i] == False:
                    queue.append(i)
                    visted[i] = True



    def bfs_sp(self,start,goal):
        visted = []
        queue =  [[start]]

        if start == goal:
            print("all ready there")
            return
        

        while queue:
            path  = queue.pop(0)
            node = path[-1]

            if node not in visted:
               next_door = self.graph[node]

               for next in next_door:
                    new_path = list(path)
                    new_path.append(next)
                    queue.append(new_path)


                    if next == goal:
                     print('shortest path is ',*new_path)
                     return
            visted.append(node)

        print("no path")
        return







g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 4)
g.addEdge(3, 1)
g.addEdge(4,2)
g.addEdge(4,3)

g.bfs(3)
print()
g.bfs_sp(0,3)
