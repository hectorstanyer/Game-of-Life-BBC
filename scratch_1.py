import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

#setting the intial parameters
alive = 1
dead = 0
value = [alive, dead]

def ranGrid(n):
    #This is setting a random choice to what coordiantes are dead or alive
 return np.random.choice(value, n*n, p = [0.1, 0.9]).reshape(n,n)
def switcher(x, y, grid):
    grid[x,y] = np.array([[0,1,0],[0,1,0],[0,1,0]])
#this sets up the rules for the game and determines the next move.
def nextMove(grid, n, image):
 NextGrid = grid.copy()
 for x in range(0,n):
     for y in range(0,n):
         NumNeigh = int((grid[x, (y-1)%n] + grid[x, (y+1)%n] +
                         grid[(x-1)%n, y] + grid[(x+1)%n, y] +
                         grid[(x-1)%n, (y-1)%n] + grid[(x-1)%n, (y+1)%n] +
                         grid[(x+1)%n, (y-1)%n] + grid[(x+1)%n, (y+1)%n])/1)
         if grid[x,y] == alive:
             if NumNeigh < 2 or NumNeigh > 3:
                 grid[x,y] = dead
         else:
             if NumNeigh == 3:
                 grid[x,y] = alive

 image.set_data(NextGrid)
 grid[:] = NextGrid[:]
 return(image)

def main():
    #Create commands for the argument in the main function
    parse = argparse.ArgumentParser(description="Conways gmae of life")
    parse.add_argument('--move_file', dest='movefile', required= False)
    parse.add_argument('--grid_size', dest='n', required= False)
    parse.add_argument('--interval', dest='interval', required=False)
    parse.add_argument('--switcher', action='store_true', required=False)

    pargs= parse.parse_arg()

    grid = np.array([])
    n = 150
    # making sure that the grid has engough to play the game of life
    if pargs.n and int(pargs.n) > 9:
        n= int(pargs.n)

    newInterval = 50
    #making sure we have enough invterals
    if pargs.interval:
        newInterval = int(pargs.interval)
     #this is if we want to design a spefic senorio.
    if pargs.switcher:
        grid = np.zeros(n*n).reshape(n, n)
        switcher(1,1,grid)
#this is a random one
    else:
        grid = ranGrid(n)
        #creating the animation for the gsme.
    figure, alpha = plt.subplots()
    image = alpha.imshow(grid, interpolation ='nearest')
    animation = anim.FuncAnimation(figure, nextMove(grid, n, image), frames = 15,
                                   interval = newInterval, save_count = 20)
    if pargs.movefile:
        animation.save(pargs.movefile, fps =20)
    plt.show()

main()

