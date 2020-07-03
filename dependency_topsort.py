import os

class Node:
    def __init__(self, id):
        self.id = id
        self.neighbours = []

class Edge:
    def __init__(self,s,d,wt=1):
        self.src = s
        self.dest = d
        self.wt = wt

class Graph:
    def __init__(self,N):
        self.N = N
        self.adjList = [Node(i) for i in range(N)]

    def addEdge(self,s,d,wt=1):
        self.adjList[s].neighbours.append(Edge(s,d,wt))

    def topological(self):
        visited = [False for i in range(self.N)]
        stack = []

        for i in range(self.N):
            if not visited[i]:
                self.topologicalUtil(i,visited,stack)

        return stack

    def topologicalUtil(self,src,visited,stack):
        visited[src] = True
        for neighbour in self.adjList[src].neighbours:
            if not visited[neighbour.dest]:
                self.topologicalUtil(neighbour.dest,visited,stack)
        # add node to stack while backtrack
        stack.append(src)

def scriptcreatenew(cmd):
    try:
        size = len(cmd)
        os.system("mkdir scripts")
        for i in range(size):
            make_bash_file(cmd[i])
    except Exception as e:
        print(e)
        print("File not created")


def make_bash_file(name):
    try:
        os.system("touch scripts/"+name)
        os.system("echo 'echo Hello "+name+"' > scripts/"+name)
        print("file : ",name," created")
    except Exception as e:
        print(e)
        print("File not created")

def run_script(name):
    try:
        print("starting ",name)
        os.system("sudo chmod 777 scripts/"+name)
        os.system("sudo ./scripts/"+name)
    except Exception as e:
        raise


def main():
    cmd = ["node","react","npm","nvm","python","pip"]
    size = len(cmd)
    g = Graph(size)

    # create the script folder
    # scriptcreatenew(cmd)

    cmdMap = {}
    for i in range(size):
        cmdMap[cmd[i]] = i

    dependencies = [
        ["react",["nvm","npm"]],
        ["npm",["node"]],
        ["pip",["python"]],
    ]

    for x,y in dependencies:
        for yc in y:
            g.addEdge(cmdMap[x], cmdMap[yc]);


    print("Dependencies :\n")
    for x,y in dependencies:
        print(x,y)

    stack = g.topological()
    print("\nTopological Ordering of dependencies :\n")

    for x in stack:
        print(cmd[x], end="->")
    print("\n")
    for x in stack:
        run_script(cmd[x])


    print("")


main()
