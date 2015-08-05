import sys

class SparseLifeGrid:

    generations = list()

    def __init__(self):
        """
        "pass" just allows this to run w/o crashing.
        Replace it with your own code in each method.
        """
        self._cells = []
        self._generations = list()

    def minRange(self):
        """
        Return the minimum row & column as a tuple.
        """
        if len(self._cells) > 0:
            minRow = self._cells[0].row
            minCol = self._cells[0].col
            for element in self._cells:
                if element.row < minRow:
                    minRow = element.row
                if element.col < minCol:
                    minCol = element.col
            minRow = int(minRow)
            minCol = int(minCol)
            return (minRow,minCol)
        else:
            return (0,0)
        
    def maxRange(self):
        """
        Returns the maximum row & column as a tuple.
        """
        if len(self._cells) > 0:
            maxRow = self._cells[0].row
            maxCol = self._cells[0].col
            for element in self._cells:
                if element.row > maxRow:
                    maxRow = element.row
                if element.col > maxCol:
                    maxCol = element.col
            maxRow = int(maxRow)
            maxCol = int(maxCol)
            return (maxRow,maxCol)
        else:
            return (0,0)

    def configure(self,coordList):
        """
        Set up the initial board position.
        "coordlist" is a list of coordinates to make alive.
        """
        for i in coordList:
            self.setCell(i[0],i[1])


    def clearCell(self,row, col):
        """
        Set the cell to "dead" (False)
        """
        test = GoLMatrixElement(row,col)
        for element in self._cells:
            if element == test:
                self._cells.remove(element)
                break
    
    def setCell(self,row, col):
        """
        Set the cell to "live" (True") and if necessary, expand the
        minimum or maximum range.
        """
        element = GoLMatrixElement(row,col)
        self._cells.append(element)

    def isLiveCell(self,row, col):
        row = int(row)
        col = int(col)
        test = GoLMatrixElement(row,col)
        for element in self._cells:
            row1 = int(element.row)
            col1 = int(element.col)
            if row == row1:
                if test.col == element.col:
                    return True
        return False

    def numLiveNeighbors(self, row,col):
        """
        Returns the number of live neighbors a cell has.
        """
        count = 0
        test0 = GoLMatrixElement(row+1,col+1)
        test1 = GoLMatrixElement(row+1,col)
        test2 = GoLMatrixElement(row+1,col-1)
        test3 = GoLMatrixElement(row,col+1)
        test4 = GoLMatrixElement(row,col-1)
        test5 = GoLMatrixElement(row-1,col+1)
        test6 = GoLMatrixElement(row-1,col)
        test7 = GoLMatrixElement(row-1,col-1)
        for element in self._cells:
            if test0 == element:
                count += 1
            if test1 == element:
                count += 1
            if test2 == element:
                count += 1
            if test3 == element:
                count += 1
            if test4 == element:
                count += 1
            if test5 == element:
                count += 1
            if test6 == element:
                count += 1
            if test7 == element:
                count += 1
        return count


    def __getitem__(self,ndxTuple):
        row = ndxTuple[0]
        col = ndxTuple[1]
        test = self.isLiveCell(row,col)
        if test == True:
            return 1
        else:
            return 0

    def __setitem__(self,ndxTuple, life):
        """
        The possible values are only true or false:
        True says alive, False for dead.
        Also, check to see if this cell is outside of the maximum row and/or
        column. If it is, modify the maximum row and/or maximum column.
        """
        row = ndxTuple[0]
        col = ndxTuple[1]
        if life == True and self.isLiveCell(row,col)==False:
            test = GoLMatrixElement(row,col)
            self._cells.append(test)
        elif life == False and self.isLiveCell(row,col)==True:
            test = GoLMatrixElement(row,col)
            self._cells.remove(test)

    def __str__(self):

        """
        Print a column before and after the live cells
        """
        s=""
        maxRange=self.maxRange()
        minRange=self.minRange()
        for i in range(minRange[0]-1,maxRange[0]+2):
            for j in range(minRange[1]-1,maxRange[1]+2):
                s+=" "+str(self[i,j])
            s+="\n"
        return s

    def getCopy(self):
        """
        Return a copy of the current board object, including the max and min
        values, etc.
        """
        return self

    def evolve(self):
        """
        Save the current state to the "generations" list.
        Based on the current generation, return the next generation state.
        """
        minRange = self.minRange()
        maxRange = self.maxRange()
        minRow = minRange[0]
        minCol = minRange[1]
        maxRow = maxRange[0]
        maxCol = maxRange[1]
        tempAdd = []
        tempDel = []
        for i in range(minRow-2,maxRow+2,1):
            for j in range(minCol-2,maxCol+2,1):
                if self.isLiveCell(i,j):
                    count = self.numLiveNeighbors(i,j)
                    if count < 2 or count > 3:
                        test = GoLMatrixElement(i,j)
                        tempDel.append(test)
                else:
                    count = self.numLiveNeighbors(i,j)
                    if count == 3:
                        test = GoLMatrixElement(i,j)
                        tempAdd.append(test)
        for item in tempAdd:
            self._cells.append(item)
        for item in tempDel:
            self._cells.remove(item)
        check = self.hasOccurred()
        self._generations.append(self._cells)
        
    def hasOccurred(self):
        """
        Check whether  this current state has already occured.
        If not, return False.  If true, return which generation number (1-10).
        """
        count = 0
        for item in self._generations:
            count += 1
            if self._cells == item:
                return count
        return False

    
    def __eq__(self,other):
        """
        This is good method if we want to compare two sparse matrices.
        You can just use "sparseMatrixA == sparseMatrixB" once this method
        is working. 
        """
        return self._cells == other._cells


class GoLMatrixElement:
    """
    Storage class for one cell
    """
    def __init__(self,row,col):
        row = int(row)
        col = int(col)
        self.row = row
        self.col = col
        self.next = None  # 
        # Since this node exists, this cell is now alive!
        # To kill it, we just delete this node from the lists.
        
    def getRow(self):
        return self.row
    
    def getCol(self):
        return self.col
    

    def __eq__(self,other):
        oRow = other.getRow()
        oCol = other.getCol()
        s = (self.row,self.col)
        o = (oRow,oCol)
        return s == o

    def __str__(self):
        s = "{0},{1}".format(self.row,self.col)
        return s




