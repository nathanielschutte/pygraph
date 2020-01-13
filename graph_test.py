import graph

# test using random graphs
def testRandom(n):
    myGraph = graph.GraphList(n)
    myGraph.randomGraph()

    print("Vertex count: " + str(myGraph.vert))

    bst = myGraph.BFS()
    prim = myGraph.primMST()
    
    print("BFS weight: " + str(bst))
    print("Prim's MST weight: " + str(prim))
    print("Percent diff: %.2f%%" % ((bst - prim) / prim * 100))

# test using graph from file
def testGraphList():
    myGraph = graph.GraphList(1)
    myGraph.readGraph("test_graph.txt")
    myGraph.printGraph()

    print("BFS weight: " + str(myGraph.BFS()))
    
    # graph.writeGraph("test_graph.txt")


if __name__ == "__main__":
    # testGraphList()
    testRandom(4)



