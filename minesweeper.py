from random import *

print()
print("=== Minesweeper ===")
print("Угловые клетки всегда безопасны.")
print("Удачной игры!")
print()

n=10
m=10
k=randint(11,20)

field=[[0 for i in range(m)] for j in range(n)]

for i in range(k):
    while True:
        x = randint(0,n-1)
        y = randint(0,m-1)
 
        if field[x][y]!='*':
            field[x][y]='*'
            break
        else:
            x=x

for i in (0,n-1):
    for j in (0,m-1):
        if field[i][j]=='*':         
            field[i][j]=0
            k-=1

    
for x in range(n):
    for y in range(m): 
        if field[x][y]=='*':
            for v in range(x-1,x+2):
                for w in range(y-1,y+2):
                    if 0<=v<=n-1 and 0<=w<=m-1:
                        if field[v][w]!='*':
                            field[v][w]=int(field[v][w])+1
for x in range(n):
    for y in range(m):
        if field[x][y]==0:
            field[x][y]='.'

Playfield=[['#' for i in range(m)] for j in range(n)]

while True:
    for row in Playfield:
        print(*row)
    Ex=-1
    Ey=-1
    while (Ex<0 or Ex>=n) or (Ey<0 or Ey>=m) or Playfield[Ex][Ey]!='#':
        print("Введите координаты ячейки, которую хотите открыть")
        try:
            Ex, Ey = [int(x)-1 for x in input().split()]
        except:
            Ex=-1
            Ey=-1
    if field[Ex][Ey]=='*':
        Playfield[Ex][Ey]='*'
        for row in Playfield:
            print(*row)
        print('You lose!')
        break
    elif field[Ex][Ey]!='*':
        Playfield[Ex][Ey]=field[Ex][Ey]
    check=True
    while check:
        check=False
        for x in range(n):
            for y in range(m):
                if Playfield[x][y]=='.':
                    for v in range(x-1,x+2):
                        for w in range(y-1,y+2):
                            if v>=0 and v<n and w>=0 and w<m:
                                if Playfield[v][w]=='#' and field[v][w]!='*':
                                    Playfield[v][w]=field[v][w]
                                    check=True
    mines=0
    for i in range(n):
        mines+=Playfield[i].count('#')
    if mines==k:
        Playfield[Ex][Ey]=field[Ex][Ey]
        for row in Playfield:
            print(*row)
        print('You win!')
        break
