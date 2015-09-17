import time

def astar(m,startp,endp):
    w,h = 12,12
    sx,sy = startp
    ex,ey = endp
    #[parent node, x, y,g,f]
    node = [None,sx,sy,0,abs(ex-sx)+abs(ey-sy)] 
    closeList = [node]
    createdList = {}
    createdList[sy*w+sx] = node
    k=0
    while(closeList):
        node = closeList.pop(0)
        x = node[1]
        y = node[2]
        l = node[3]+1
        k+=1
        #find neighbours 
        #make the path not too strange
        if k|1:
            neighbours = ((x,y+1),(x,y-1),(x+1,y),(x-1,y))
        else:
            neighbours = ((x+1,y),(x-1,y),(x,y+1),(x,y-1))
        for nx,ny in neighbours:
            if nx==ex and ny==ey:
                path = [(ex,ey)]
                while node:
                    path.append((node[1],node[2]))
                    node = node[0]
                return list(reversed(path))            
            if 0<=nx<w and 0<=ny<h and m[ny][nx]==None:
                if ny*w+nx not in createdList:
                    nn = (node,nx,ny,l,l+abs(nx-ex)+abs(ny-ey))
                    createdList[ny*w+nx] = nn
                    #adding to closelist ,using binary heap
                    nni = len(closeList)
                    closeList.append(nn)
                    while nni:
                        i = (nni-1)>>1
                        if closeList[i][4]>nn[4]:
                            closeList[i],closeList[nni] = nn,closeList[i]
                            nni = i
                        else:
                            break


    return 'not found'

m = [[None,None,None,'ll',None,None,'ll',None,None,None,None,None],
     [None,None,None,None,'ll',None,'ll',None,None,None,None,None],
     [None,None,'ll','ll','ll',None,'ll',None,None,None,None,None],
     [None,None,None,None,'ll',None,'ll',None,None,None,None,None],
     [None,None,'ll','ll','ll',None,'ll',None,None,None,None,None],
     [None,None,None,'ll','ll',None,'ll','ll','ll',None,None,None],
     [None,None,None,None,'ll',None,'ll',None,None,None,None,None],
     [None,None,None,None,None,None,'ll',None,'ll','ll',None,None],
     [None,None,None,None,None,None,'ll',None,None,None,'ll',None],
     [None,None,None,None,None,None,'ll',None,None,None,None,'ll'],
     [None,None,None,None,None,None,'ll',None,None,None,'ll',None],
     [None,None,None,None,None,None,'ll',None,None,None,None,None]]

t1 = time.time()
for i in range(1000):
    result = astar(m,(11,11),(2,3))
print(time.time()-t1) 
cm = [list(x[:]) for x in m]


if isinstance(result, list):
    for y in range(len(m)):
        my = m[y]
        for x in range(len(my)):
            for px,py in result:
                if px==x and py ==y:
                    cm[y][x] = '++'
else:
    print(result)

for my in cm:
    print(' '.join([str(x) for x in my]))

exit(0)