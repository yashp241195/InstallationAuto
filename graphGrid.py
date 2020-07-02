
import random as rand

def isValidMove(r,c,R,C,grid):
    return (r < R and r >= 0 )and (c >= 0 and c < C) and grid[r][c] == 0

def BFS(r,c,R,C,grid):
    gridVisited = [[ 0 for j in range(C)] for i in range(R)]

    QueueR = []
    QueueC = []

    QueueR.append(r)
    QueueC.append(c)

    grid[r][c] = 2
    gridVisited[r][c] = 1
    count = 3

    while(len(QueueC) != 0):

        r = QueueR[0]
        c = QueueC[0]

        del QueueR[0]
        del QueueC[0]

        dr = [-1,+1,0,0,1,-1,1,-1]
        dc = [0,0,-1,+1,1,1,-1,-1]

        for i in range(8):
            if(isValidMove(r+dr[i],c+dc[i],R,C,grid)):
                if(gridVisited[r+dr[i]][c+dc[i]] == 0):
                    QueueR.append(r+dr[i])
                    QueueC.append(c+dc[i])
                    gridVisited[r+dr[i]][c+dc[i]] = 1
                    grid[r+dr[i]][c+dc[i]] = count
                    count += 1

        # count += 1

    print("\nSolution")
    printGrid(gridVisited)

    print("\nSolution")
    printGrid(grid)


def printGrid(grid):
    print("\n")
    for i in grid:
        print(i)


def main():
    N = 5
    R=C=N
    grid = [[ 0 for j in range(C)] for i in range(R)]

    grid[1][2] = 0
    printGrid(grid)
    BFS(4,4,N,N,grid)


main()
