import turtle
import random

class World:
    def __init__(self, mx, my, nb, nf, np, nberry):
        self.maxX = mx
        self.maxY = my
        self.thingList = []
        self.grid = []
        self.FishCount = nf
        self.BearCount = nb
        self.PlantCount = np
        self.BerryCount = nberry

        for arow in range(self.maxY):     
            row = []
            for acol in range(self.maxX):
                row.append(None)
            self.grid.append(row)        
        
        self.wturtle = turtle.Turtle()
        self.wscreen = turtle.Screen()
        self.wscreen.setworldcoordinates(0,0,self.maxX-1,self.maxY-1)   
        self.wscreen.addshape("Bear.gif")
        self.wscreen.addshape("Fish.gif")
        self.wscreen.addshape("Plant.gif")
        self.wscreen.addshape("Berries.gif")
        self.wturtle.hideturtle()               

    def draw(self):
        self.wscreen.tracer(0)
        self.wturtle.forward(self.maxX-1)
        self.wturtle.left(90)
        self.wturtle.forward(self.maxY-1)
        self.wturtle.left(90)
        self.wturtle.forward(self.maxX-1)
        self.wturtle.left(90)
        self.wturtle.forward(self.maxY-1)
        self.wturtle.left(90)    
        for i in range(self.maxY-1):
            self.wturtle.forward(self.maxX-1)
            self.wturtle.backward(self.maxX-1)
            self.wturtle.left(90)
            self.wturtle.forward(1)
            self.wturtle.right(90)
        self.wturtle.forward(1)
        self.wturtle.right(90)
        for i in range(self.maxX-2):
            self.wturtle.forward(self.maxY-1)
            self.wturtle.backward(self.maxY-1)
            self.wturtle.left(90)
            self.wturtle.forward(1)
            self.wturtle.right(90)
        self.wscreen.tracer(1)
        self.wscreen.colormode(255)
        self.wturtle.fillcolor(0, 255, 255)
        self.wturtle.penup()
        self.wturtle.goto(25,0)
        self.wturtle.pendown()
        self.wturtle.begin_fill()
        self.wturtle.goto(25,24)
        self.wturtle.goto(0,24)
        self.wturtle.goto(0,0)
        self.wturtle.goto(25,0)
        self.wturtle.end_fill()
        self.wturtle.fillcolor(107,142,35)
        self.wturtle.penup()
        self.wturtle.goto(25,24)
        self.wturtle.pendown()
        self.wturtle.begin_fill()
        self.wturtle.goto(49,24)
        self.wturtle.goto(49,0)
        self.wturtle.goto(25,0)
        self.wturtle.goto(25,24)
        self.wturtle.end_fill()

    def freezeWorld(self):
        self.wscreen.exitonclick()
        
    def addThing(self, athing, x, y):   
        athing.setX(x)
        athing.setY(y)
        self.grid[y][x] = athing        
        athing.setWorld(self)
        self.thingList.append(athing)   
        athing.appear()                 
    
    def delThing(self,athing):
        athing.hide()                                     
        self.grid[athing.getY()][athing.getX()] = None     
        self.thingList.remove(athing)                      
    
    def moveThing(self,oldx,oldy,newx,newy):
        self.grid[newy][newx] = self.grid[oldy][oldx]
        self.grid[oldy][oldx] = None
    
    def getMaxX(self):
        return self.maxX
    
    def getMaxY(self):
        return self.maxY
    
    def liveALittle(self):                                  
        if self.thingList != [ ]:
           athing = random.randrange(len(self.thingList))    
           randomthing = self.thingList[athing]              
           randomthing.liveALittle()                       
     
    def emptyLocation(self,x,y):
        if self.grid[y][x] == None:
            return True
        else:
            return False
        
    def lookAtLocation(self,x,y):
        return self.grid[y][x]
    
    def FishCount(self):
        return self.FishCount

    def BearCount(self):
        return self.BearCount

    def PlantCount(self):
        return self.PlantCount
    
    def BerryCount(self):
        return self.BerryCount

class Fish:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.up()
        self.turtle.hideturtle()
        self.turtle.shape("Fish.gif")
        
        self.xpos = 0
        self.ypos = 0
        self.world = None                 
        
        self.starveTick = 0
        self.breedTick = 0
        self.energyTick = 15

    def setX(self,newx):
        self.xpos = newx
    
    def setY(self,newy):
        self.ypos = newy
    
    def getX(self):
        return self.xpos
    
    def getY(self):
        return self.ypos
    
    def setWorld(self,aworld):
        self.world = aworld
 
    def appear(self):
        self.turtle.goto(self.xpos, self.ypos)
        if 1 <= self.xpos < 23:
            self.turtle.showturtle()
            self.world.FishCount += 1

    def hide(self):
        self.turtle.hideturtle()
        self.world.FishCount -= 1

    def move(self,newx,newy):
        self.energyTick -= 1
        self.world.moveThing(self.xpos,self.ypos,newx,newy)
        self.xpos = newx
        self.ypos = newy
        self.turtle.goto(self.xpos, self.ypos)

    def liveALittle(self):
        offsetList = [(-1,1) ,(0,1) ,(1,1),          
                      (-1,0)        ,(1,0),
                      (-1,-1),(0,-1),(1,-1)]     
        adjfish = 0                                  
        for offset in offsetList:                    
            newx = self.xpos + offset[0]             
            newy = self.ypos + offset[1]
            if 1 <= newx < 23  and  1 <= newy < 23:          
                if (not self.world.emptyLocation(newx,newy)) and isinstance(self.world.lookAtLocation(newx,newy),Fish):
                    adjfish = adjfish + 1   
     
        if adjfish >= 2:                   
            self.world.delThing(self)      
        else:
            self.tryToEat()
            if self.starveTick == 10:
                self.world.delThing(self)
            elif self.energyTick == 0:
                self.world.delThing(self)
            self.breedTick = self.breedTick + 1
            if self.breedTick >= 10:
                self.tryToBreed()

            self.tryToMove()

    def tryToBreed(self):
        offsetList = [(-1,1) ,(0,1) ,(1,1),          
                      (-1,0)        ,(1,0),
                      (-1,-1),(0,-1),(1,-1)]    
        randomOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randomOffsetIndex]
        nextx = self.xpos + randomOffset[0]
        nexty = self.ypos + randomOffset[1]
        while not (1 <= nextx <= 23 and 
                  1 <= nexty < 23):  
            randomOffsetIndex = random.randrange(len(offsetList))
            randomOffset = offsetList[randomOffsetIndex]
            # fish spawn from eggs, therefore can spawn anywhere, not necessary to be next to parent if not possible.
            nextx = random.randint(1,23)
            nexty = random.randint(1,23)
    
        if self.world.emptyLocation(nextx,nexty) and self.energyTick >= 5:    
           self.energyTick -= 5
           childThing = Fish()
           self.world.addThing(childThing,nextx,nexty)
           self.breedTick = 0
    
    def tryToMove(self):
        offsetList = [(-1,1) ,(0,1) ,(1,1),          
                      (-1,0)        ,(1,0),
                      (-1,-1),(0,-1),(1,-1)]   
        randomOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randomOffsetIndex]
        nextx = self.xpos + randomOffset[0]
        nexty = self.ypos + randomOffset[1]
        while not ((1 <= nextx <= 23) and (1 <= nexty <= 23)):
            randomOffsetIndex = random.randrange(len(offsetList))
            randomOffset = offsetList[randomOffsetIndex]
            nextx = self.xpos + randomOffset[0]
            nexty = self.ypos + randomOffset[1]
    
        if self.world.emptyLocation(nextx,nexty):
           self.move(nextx,nexty)

    def tryToEat(self):
        offsetList = [(-1,1) ,(0,1) ,(1,1),          
                      (-1,0)        ,(1,0),
                      (-1,-1),(0,-1),(1,-1)] 
        adjprey = []                 
        for offset in offsetList:
            newx = self.xpos + offset[0]
            newy = self.ypos + offset[1]
            if 1 <= newx <= 23 and 1 <= newy <= 23:
                if (not self.world.emptyLocation(newx,newy)) and isinstance(self.world.lookAtLocation(newx,newy),Plant):
                    adjprey.append(self.world.lookAtLocation(newx,newy))       
                
        if len(adjprey)>0:                
            randomprey = adjprey[random.randrange(len(adjprey))]   
            preyx = randomprey.getX()
            preyy = randomprey.getY()
        
            self.world.delThing(randomprey)                            
            self.move(preyx,preyy)                                      
            self.starveTick = 0
            self.energyTick += 5
        else:
            self.starveTick = self.starveTick + 1  

class Bear:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.up()
        self.turtle.hideturtle()
        self.turtle.shape("Bear.gif")

        self.xpos = 0
        self.ypos = 0
        self.world = None
        
        self.energyTick = 15
        self.starveTick = 0
        self.breedTick = 0
        
    def setX(self,newx):
        self.xpos = newx
    
    def setY(self,newy):
        self.ypos = newy
    
    def getX(self):
        return self.xpos
    
    def getY(self):
        return self.ypos
    
    def setWorld(self,aworld):
        self.world = aworld
 
    def appear(self):
        self.turtle.goto(self.xpos, self.ypos)
        if 26 <= self.xpos <= 48:
            self.turtle.showturtle()
            self.world.BearCount += 1

    def hide(self):
        self.turtle.hideturtle()
        self.world.BearCount -= 1

    def move(self,newx,newy):
        self.energyTick -= 1
        self.world.moveThing(self.xpos,self.ypos,newx,newy)
        self.xpos = newx
        self.ypos = newy
        self.turtle.goto(self.xpos, self.ypos)

    def liveALittle(self):
        self.breedTick = self.breedTick + 1
        if self.breedTick >= 9:
            self.tryToBreed()
    
        self.tryToEat()          
    
        if self.starveTick == 10:
            self.world.delThing(self)
        elif self.energyTick == 0:
            self.world.delThing(self)
        else:
            self.tryToMove()

    def tryToEat(self):
        offsetList = [(-1,1) ,(0,1) ,(1,1),          
                      (-1,0)        ,(1,0),
                      (-1,-1),(0,-1),(1,-1)] 
        adjprey = []                 
        for offset in offsetList:
            newx = self.xpos + offset[0]
            newy = self.ypos + offset[1]
            if 1 <= newx < self.world.getMaxX() and 0 <= newy < self.world.getMaxY():
                if (not self.world.emptyLocation(newx,newy)) and (isinstance(self.world.lookAtLocation(newx,newy),Fish)):
                    adjprey.append(self.world.lookAtLocation(newx,newy))       
                elif (not self.world.emptyLocation(newx,newy)) and (isinstance(self.world.lookAtLocation(newx,newy),Berry)):
                    adjprey.append(self.world.lookAtLocation(newx,newy))       
                
        if len(adjprey)>0:                
            randomprey = adjprey[random.randrange(len(adjprey))]   
            preyx = randomprey.getX()
            preyy = randomprey.getY()
        
            self.world.delThing(randomprey)                            
            self.move(preyx,preyy)                                      
            self.starveTick = 0
            self.energyTick += 5
        else:
            self.starveTick = self.starveTick + 1  
            
    def tryToBreed(self):
        if (26 <= self.xpos <= 48) and (1 <= self.ypos <= 23): 
            offsetList = [(-1,1) ,(0,1) ,(1,1),          
                          (-1,0)        ,(1,0),
                          (-1,-1),(0,-1),(1,-1)]    
            randomOffsetIndex = random.randrange(len(offsetList))
            randomOffset = offsetList[randomOffsetIndex]
            nextx = self.xpos + randomOffset[0]
            nexty = self.ypos + randomOffset[1]
            while not (26 <= nextx <= 48) and (1 <= nexty <= 23):
                randomOffsetIndex = random.randrange(len(offsetList))
                randomOffset = offsetList[randomOffsetIndex]
                nextx = nextx + randomOffset[0]
                nexty = nexty + randomOffset[1]
                self.tryToMove()
            if self.world.emptyLocation(nextx,nexty) and self.energyTick >= 5:   
                self.energyTick -= 5
                childThing = Bear()
                self.world.addThing(childThing,nextx,nexty)
                self.breedTick = 0

    def tryToMove(self):
        offsetList = [(-1,1) ,(0,1) ,(1,1),          
                      (-1,0)        ,(1,0),
                      (-1,-1),(0,-1),(1,-1)]   
        randomOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randomOffsetIndex]
        nextx = self.xpos + randomOffset[0]
        nexty = self.ypos + randomOffset[1]
        while not(1 <= nextx <= 48 and 
                  1 <= nexty <= 23 ):
            randomOffsetIndex = random.randrange(len(offsetList))
            randomOffset = offsetList[randomOffsetIndex]
            nextx = self.xpos + randomOffset[0]
            nexty = self.ypos + randomOffset[1]
    
        if self.world.emptyLocation(nextx,nexty):
           self.move(nextx,nexty)
           
class Plant:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.up()
        self.turtle.hideturtle()
        self.turtle.shape("Plant.gif")

        self.xpos = 0
        self.ypos = 0
        self.world = None
        
        self.breedTick = 0
        
    def setX(self,newx):
        self.xpos = newx
    
    def setY(self,newy):
        self.ypos = newy
    
    def getX(self):
        return self.xpos
    
    def getY(self):
        return self.ypos
    
    def setWorld(self,aworld):
        self.world = aworld
 
    def appear(self):
        self.turtle.goto(self.xpos, self.ypos)
        if 1 <= self.xpos <= 23:
            self.turtle.showturtle()
            self.world.PlantCount += 1

    def hide(self):
        self.turtle.hideturtle()
        self.world.PlantCount -= 1

    def move(self,newx,newy):
        self.world.moveThing(self.xpos,self.ypos,newx,newy)
        self.xpos = newx
        self.ypos = newy
        self.turtle.goto(self.xpos, self.ypos)

    def liveALittle(self):
            self.breedTick = self.breedTick + 1
            if self.breedTick >= 11:
                self.tryToBreed()
            
    def tryToBreed(self):
        offsetList = [(-1,1) ,(0,1) ,(1,1),          
                      (-1,0)        ,(1,0),
                      (-1,-1),(0,-1),(1,-1)]    
        randomOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randomOffsetIndex]
        nextx = self.xpos + randomOffset[0]
        nexty = self.ypos + randomOffset[1]
        while not (1 <= nextx < 23 and 
                   1 <= nexty < 23 ):  
            randomOffsetIndex = random.randrange(len(offsetList))
            randomOffset = offsetList[randomOffsetIndex]
            nextx = random.randint(1,23)
            nexty = random.randint(1,23)

        if self.world.emptyLocation(nextx,nexty):    
           childThing = Plant()
           self.world.addThing(childThing,nextx,nexty)
           self.breedTick = 0

class Berry:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.up()
        self.turtle.hideturtle()
        self.turtle.shape("Berries.gif")

        self.xpos = 0
        self.ypos = 0
        self.world = None
        
        self.breedTick = 0
        
    def setX(self,newx):
        self.xpos = newx
    
    def setY(self,newy):
        self.ypos = newy
    
    def getX(self):
        return self.xpos
    
    def getY(self):
        return self.ypos
    
    def setWorld(self,aworld):
        self.world = aworld
 
    def appear(self):
        self.turtle.goto(self.xpos, self.ypos)
        if 26 <= self.xpos < 48:
            self.turtle.showturtle()
            self.world.BerryCount += 1

    def hide(self):
        self.turtle.hideturtle()
        self.world.BerryCount -= 1

    def move(self,newx,newy):
        self.world.moveThing(self.xpos,self.ypos,newx,newy)
        self.xpos = newx
        self.ypos = newy
        self.turtle.goto(self.xpos, self.ypos)

    def liveALittle(self):
            self.breedTick = self.breedTick + 1
            if self.breedTick >= 9:
                self.tryToBreed()
            
    def tryToBreed(self):
        offsetList = [(-1,1) ,(0,1) ,(1,1),          
                      (-1,0)        ,(1,0),
                      (-1,-1),(0,-1),(1,-1)]    
        randomOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randomOffsetIndex]
        nextx = self.xpos + randomOffset[0]
        nexty = self.ypos + randomOffset[1]
        while not (26 <= nextx < 48 and 
                   1 <= nexty < 23 ):  
            randomOffsetIndex = random.randrange(len(offsetList))
            randomOffset = offsetList[randomOffsetIndex]
            nextx = random.randint(26,48)
            nexty = random.randint(1,23)
    
        if self.world.emptyLocation(nextx,nexty):    
           childThing = Berry()
           self.world.addThing(childThing,nextx,nexty)
           self.breedTick = 0

#def histogram():
#    f = open("steady.dat", 'r')
#    bturtle = turtle.Turtle()
#    fturtle = turtle.Turtle()
#    pturtle = turtle.Turtle()
#    berryturtle = turtle.Turtle()


def mainSimulation():
    numberOfBears = 0
    numberOfFish = 0
    numberOfPlants = 0
    numberOfBerries = 0
    worldLifeTime = 2500
    worldWidth = 50
    worldHeight = 25
    listBear = []
    listFish = []
    listPlant = []
    listBerry = []
    
    myworld = World(worldWidth,worldHeight,numberOfBears, numberOfFish,numberOfPlants,numberOfBerries)      
    myworld.draw()                               

    for i in range(10):  
        newfish = Fish()
        x = random.randrange(1,23)
        y = random.randrange(1,23)
        while not myworld.emptyLocation(x,y):
            x = random.randrange(1,23)
            y = random.randrange(1,23)
        myworld.addThing(newfish,x,y)        
    
    for i in range(10):   
        newbear = Bear()
        x = random.randrange(26,48)
        y = random.randrange(1,23)
        while not myworld.emptyLocation(x,y):   
            x = random.randrange(26,48)
            y = random.randrange(1,23)
        myworld.addThing(newbear,x,y)    
        
    for i in range(30):   
        newplant = Plant()
        x = random.randrange(1,23)
        y = random.randrange(1,23)
        while not myworld.emptyLocation(x,y):   
            x = random.randrange(1,23)
            y = random.randrange(1,23)
        myworld.addThing(newplant,x,y)      
    
    for i in range(30):
        newberry = Berry()
        x = random.randrange(26,48)
        y = random.randrange(1,23)
        while not myworld.emptyLocation(x,y):
            x = random.randrange(26,48)
            y = random.randrange(1,23)
        myworld.addThing(newberry,x,y)
    
    f = open("steady.dat", 'w')
    for i in range(worldLifeTime):     
        myworld.liveALittle()
        if i % 100 == 0:
            f.write(str(i))
            f.write(' ')
            f.write(str(myworld.FishCount))
            f.write(' ')
            f.write(str(myworld.BearCount))
            f.write(' ')
            f.write(str(myworld.PlantCount))
            f.write(' ')
            f.write(str(myworld.BerryCount))
            f.write('\n')
            listFish.append(myworld.FishCount)
            listBear.append(myworld.BearCount)
            listPlant.append(myworld.PlantCount)
            listBerry.append(myworld.BerryCount)

    myworld.freezeWorld()          

mainSimulation()
