#conway's game of life page 144
import random, time, copy
WIDTH=60
HEIGHT=20
#create a list of list for the cells:
nextCells=[]
for x in range(WIDTH):
    column=[]
    for y in range(HEIGHT):
        if random.randint(0,1)==0:
            column.append('#') #add aliving cell
        else:
            column.append('') #add adead cell
    nextCells.append(column) #next cell is a list of collumn lists.
while True:
    print('\n\n\n\n\n') #separate each step with new lines.
    currentCells=copy.deepcopy(nextCells)

    #print currentCells on screen:
    for y in range(HEIGHT):
        for y in range(WIDTH):
            #get the neighboring coordinates
            leftcoord=(x-1)% WIDTH
            rightcoord=(x+1)%WIDTH
            abovecoord=(y-1)%HEIGHT
            belowcoord=(y+1)%HEIGHT

            #count the number of living neighbor
            numNeighbors=0
            if currentCells[leftcoord][abovecoord]=='#':
                numNeighbors +=1 #top left neighbor is alive
            if currentCells[x][abovecoord]=='#':
                numNeighbors+=1 #top neighbor is alive
            if currentCells[rightcoord][abovecoord]=='#':
                numNeighbors+=1 #top right neighbor is alive
         #   if currentCells[leftcoord]abovecoord[y]=='#':
                numNeighbors+=1 #left neighbor is alive
           # if currentCells[rightcoord][y]=='#':
                numNeighbors+=1 #right neighbor is alive. 
            if currentCells[leftcoord][belowcoord]=='#':
                numNeighbors+=1 #bottom left neighbor is alive
            if currentCells[x][belowcoord]=='#':
                numNeighbors+=1 #bottom neighbor is alive
            if currentCells[rightcoord][belowcoord]=='#':
                numNeighbors+=1 #bottom right neighbor is alive

                #set cell based on conways game of life rules
              #  if currentCells[x][y]=='#' and (numNeighbors==2 or numNeighbors==3):
                    #living cells with 2 or 3 stays alive
                    nextCells[x][y]=='#'
                elif currentCells[x][y]==' ' and numNeighbors==3:
                    #dead cells with three neighbors become alive:
                    nextCells[x][y]='#'
                else:
                    #everything dies or stays dead:
                    nextCells[x][y]=' '
            time.sleep(1) #add a 1 second pause to reduce flickering.



