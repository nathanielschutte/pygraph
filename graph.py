import random

class Vertex:
    def __init__(self, data, weight):
        self.vertex = data
        self.next = None
        self.weight = weight

class GraphList:
    def __init__(self, vertices):
        self.vert = vertices
        self.graph = [None] * self.vert

    # add edge between src and dest vertices, undirected
    def addEdge(self, src, dest, weight):

        # add node with vertex value dest to start of src list
        v = Vertex(dest, weight)
        v.next = self.graph[src]
        self.graph[src] = v

        # same thing other direction
        v = Vertex(src, weight)
        v.next = self.graph[dest]
        self.graph[dest] = v

    # randomly generate a graph with given vertex count
    def randomGraph(self):
        for i in range(1, self.vert):
            s = list(range(0, i))
            x = random.randint(1, i)
            for j in range(0, x):
                w = random.randint(10, 100)
                dest = s[random.randint(0, len(s)-1)]
                self.addEdge(i, dest, w)
                s.remove(dest)

    # get weight of edge from vertices a and b
    def getWeight(self, a, b):
        node = graph[a]
        while(node.next != b):
            node = node.next
        return node.weight

    # breadth first search algorithm
    def BFS(self):
        marked = [False] * self.vert
        queue = []
        total = 0

        # pick random starting vertex
        start = random.randint(0, self.vert-1)

        # begin queue of unvisited nodes
        queue.append(start)
        marked[start] = True
        while(len(queue) > 0):
            vertex = queue.pop(0)
            node = self.graph[vertex]

            # look for edges to unvisited nodes, queue up
            while(node != None):
                if not marked[node.vertex]:
                    queue.append(node.vertex)
                    total = total + node.weight
                    marked[node.vertex] = True
                node = node.next
                
        return total

    # use for prim's.  find min edge off of vertex set mst
    def minEdge(self, mst, marked):
        m = -1
        mark = -1
        for v in mst:
            node = self.graph[v]
            while(node != None):
                edge = node.vertex
                if marked[edge] == False:
                    if m == -1 or node.weight < m:
                        m = node.weight
                        mark = edge
                node = node.next

        marked[mark] = True
        mst.append(mark)
        return m
    

    # prim's MST algorithm
    def primMST(self):
        weight = 0
        mst = []
        marked = [False] * self.vert

        mst.append(random.randint(0, self.vert-1))
        while(len(mst) < self.vert):
            nextW = self.minEdge(mst, marked)
            weight = weight + nextW
        return weight
        


    # print out connections
    def printGraph(self):
        for i in range(self.vert):
            print("Vertex {}:".format(i), end = "")
            temp = self.graph[i]             
            while temp:
                print(" -> {}(w: {})".format(temp.vertex, temp.weight), end = "")
                temp = temp.next
            print("\n")

    # write graph to file in matrix format
    def writeGraph(self, file):

        # convert to matrix format
        m = [[0 for i in range(self.vert)] for j in range(self.vert)]
        for i in range(self.vert):
            node = self.graph[i]
            while(node != None):
                m[i][node.vertex] = node.weight
                node = node.next

        # write matrix to file
        f = open(file, "w")
        for i in range(self.vert):
            for j in range(self.vert):
                f.write(str(m[i][j]) + "\t")
            f.write("\n")
        f.close()


    # read file and construct graph
    def readGraph(self, file):

        # read matrix format directly to list
        f = open(file, "r")
        lines = f.readlines()
        self.vert = len(lines)
        self.graph = [None] * self.vert
        for line in range(len(lines)):
            edges = lines[line].split()
            for edge in range(line, len(edges)):
                if int(edges[edge]) > 0:
                    self.addEdge(line, edge, int(edges[edge]))

# -------------------------------------------------------------------------------------
