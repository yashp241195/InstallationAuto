
import random as rand

def isValidMove(r,c,R,C,grid):
    return (r < R and r >= 0 )and (c >= 0 and c < C) and grid[r][c] == 0

def BFS(r,c,R,C,grid):
    gridVisited = [[0 for j in range(C)] for i in range(R)]

    QueueR = []
    QueueC = []

    QueueR.append(r)
    QueueC.append(c)

    gridVisited[r][c] = 1

    while(len(QueueC) != 0):

        r0 = QueueR[0]
        c0 = QueueC[0]

        grid[r0][c0] = 2 # marking on the grid

        del QueueR[0]
        del QueueC[0]

        dr = [-1,+1,0,0,+1,-1,+1,-1]
        dc = [0,0,-1,+1,+1,-1,-1,+1]

        for i in range(8):
            if(isValidMove(r+dr[i],c+dc[i],R,C,grid)):
                if(gridVisited[r+dr[i]][c+dc[i]] == 0):
                    r += dr[i]
                    c += dc[i]
                    QueueR.append(r)
                    QueueC.append(c)
                    gridVisited[r][c] = 1



    print("\nSolution")
    printGrid(gridVisited)

def printGrid(grid):
    print("\n")
    for i in grid:
        print(i)


def main():
    N = 5
    grid = [[ int(rand.random()*0) for j in range(N)] for i in range(N)]

    grid[1][2] = 0
    printGrid(grid)
    BFS(1,2,N,N,grid)

    printGrid(grid)


main()
