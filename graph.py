
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



def main():
    g = Graph(4)
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

main()
