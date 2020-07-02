
class Node:
    def __init__(self, id):
        self.id = id
        self.neighbours = []

class Edge:
    def __init__(self, s, t, w=1):
        self.src = s
        self.dest = t
        self.wt = w

class Graph:
    def __init__(self, N):
        self.N = N
        self.AdjList = [Node(i) for i in range(N)]

    def printGraph(self):
        for Node in self.AdjList:
            print("{",Node.id,end=" : ")
            for neighbour in Node.neighbours:
                print("(",neighbour.dest, end=", ")
                print(neighbour.wt, end="), ")

            print("}",end="\n")
        print("\n")

    def addEdge(self, src, dest, wt=1):
        self.AdjList[src].neighbours.append(Edge(src, dest, wt))

    def DFS(self, src):
        visitedList = [False] * self.N
        print("DFS : ")
        self.DFSUtil(src, visitedList)
        print("\n")

    def DFSUtil(self,src, visited):
        visited[src] = True
        print(src,end=" -> ")
        for neighbour in self.AdjList[src].neighbours:
            if not visited[neighbour.dest]:
                self.DFSUtil(neighbour.dest,visited)

    def BFS(self,src):
        visitedList = [False]*self.N
        Queue = []
        Queue.append(src)
        print("BFS : ")
        self.BFSUtil(src, visitedList, Queue)
        print("\n")

    def BFSUtil(self, src, visited, queue):
        while(len(queue) != 0):
            q = queue[0]
            del queue[0]
            visited[q] = True

            print(q, end=" -> ")
            for neighbour in self.AdjList[q].neighbours:
                if not visited[neighbour.dest]:
                    queue.append(neighbour.dest)

    def biDirEdge(self,src,dest,wt=1):
        self.addEdge(src,dest,wt)
        self.addEdge(dest,src,wt)

    def ConnectedComponents(self):
        count = 0
        component = [0]*self.N
        visitedList = [False]*self.N
        res = self.ConnectedUtil(count,component,visitedList)
        print("\n")
        print(res[0])
        print(res[1])
        print("\n")


    def ConnectedUtil(self,count,component,visited):
        for i in range(self.N):
            if not visited[i]:
                count += 1
                self.ConnectedDFSUtil(i,count,component,visited)
        return (count,component)

    def ConnectedDFSUtil(self,src,count,component,visited):
        visited[src] = True
        component[src] = count
        print(src,end=" -> ")
        for neighbour in self.AdjList[src].neighbours:
            if not visited[neighbour.dest]:
                self.ConnectedDFSUtil(neighbour.dest,count,component,visited)

    def topological(self):
        result = []
        visited = [False for i in range(self.N)]

        for i in range(self.N):
            if not visited[i]:
                self.topologicalUtil(i,visited,result)
        print(list(reversed(result)))

    def topologicalUtil(self,src,visited,result):
        visited[src] = True
        for neighbour in self.adjList[src].neighbours:
            if visited[neighbour.dest] == False:
                self.topologicalUtil(neighbour.dest,visited,result)
        result.append(src)            

def main():
    # g = Graph(4)
    # DFS
    # g.addEdge(0,1)
    # g.addEdge(0,2)
    # g.addEdge(1,2)
    # g.addEdge(2,0)
    # g.addEdge(2,3)
    # g.addEdge(3,3)
    # g.printGraph()
    # g.DFS(1) # 1 2 0 3

    # BFS
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 2)
    # g.addEdge(2, 0)
    # g.addEdge(2, 3)
    # g.addEdge(3, 3)
    # g.printGraph()
    # g.BFS(2) # 2 0 3 1

    # Connected Components for Un Dir Graph
    # g = Graph(5)
    # g.biDirEdge(1, 0)
    # g.biDirEdge(2, 3)
    # g.biDirEdge(3, 4)
    # g.printGraph()
    # g.ConnectedComponents()
    
    # topological ordering    
    # g = Graph(6)
    # g.addEdge(5, 2);
    # g.addEdge(5, 0);
    # g.addEdge(4, 0);
    # g.addEdge(4, 1);
    # g.addEdge(2, 3);
    # g.addEdge(3, 1);
    # print("Topological")
    # g.topological()


main()
