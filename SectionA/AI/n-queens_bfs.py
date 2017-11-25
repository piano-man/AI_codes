import sys
import copy
from os import system

#Set the console title
system("title Michael Fiford - Breadth First N-Queen Solver")

class QueenSolver:
    tableSize = 0
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    queue = []

    #Whether or not the solver can be ran
    canRun = False

    def setup(self, queenNumber):
        
        self.tableSize = queenNumber
        self.canRun = True
        if queenNumber < 4:
            print ("No Solution")
            self.canRun = False
        elif queenNumber > 13:
            print("Over Flow")
            self.canRun = False

    def blankTable(self):
        table = []
        for row in xrange(self.tableSize):
            new = []
            for col in xrange(self.tableSize):
                new.append(0);
            table.append(new)
        return table

    def placeQueen(self, table, row, col):
        t2 = copy.deepcopy(table)
        t2[row][col] = 1
        return t2

    #The main program loop
    def loopBoard(self):
        col = 1
        while len(self.queue):
            queue2 = []
            print (col, "Queens Placed")
            #Loop the queue, looking for positions from each status
            #s is an array containing the current queen positions for this status
            for s in self.queue:
                #Get what moves are available from this status
                availableMoves = self.getPositions(s, col)
                #If we are placing the last queen, and there are solutions available, finish
                if col == self.tableSize -1 and len(availableMoves):
                    #Clear queue
                    self.queue = []
                    #Get the solution (or one of them, we only care about the first one)
                    s = availableMoves[0]
                    break;
                #Add the possible moves to the new queue
                #This a table containing all queens now placed
                if len(availableMoves):
                    queue2 += availableMoves
            #Replace the old queue with the new one
            self.queue = queue2
            #Increase Queen/col counter
            col += 1
        self.finish(s, col)

    #Get an array of moves that are available, given info about the current table, and the current column
    def getPositions(self, table, col):        
        #Create a row counter, and array to contain our position info
        row = 0
        possiblePositions = []

        #Loop all rows on the board
        while row < self.tableSize:
            #If we can place in this space
            if self.canPlace(table, row, col):
                #Add the table with the newly added queen to the list of possible moves
                possiblePositions.append(self.placeQueen(table, row, col))
            row += 1
        return possiblePositions

    #Check whether or not we can place a queen in a position, given the table and the row and col of the desired position
    #Return True if space is available
    def canPlace(self, table, row, col):
        # - Direction
        # Check left/right
        x = 0
        #Loop across the table
        while x < self.tableSize:
            if table[x][col]:
                return False
            x += 1

        # | Direction
        #Check up/down
        y = 0
        #Loop down the table
        while y < self.tableSize:
            if table[row][y]:
                return False
            y += 1


        # / Direction
        #Check up right Diagonal
        #We can start in the cell 1 up and 1 right of the cell in question, as we have already checked the actual cell in the above 2 checks
        x = row + 1
        y = col + 1
        #Loop up/right through the table
        while x < self.tableSize and y < self.tableSize:
            if table[x][y]:
                return False            
            x += 1
            y += 1
        #Check down left Diagonal
        #Again, not starting in the cell specified
        x = row - 1
        y = col - 1
        #Loop down/left through the table
        while x >= 0 and y >= 0:
            if table[x][y]:
                return False
            x -= 1
            y -= 1

        # \ Direction
        #Check up left diagonal
        #Again, not starting in the cell specified
        x = row - 1
        y = col + 1
        #Loop up left through the table
        while x >= 0 and y < self.tableSize:
            if table[x][y]:
                return False
            x -= 1
            y += 1
        #Check down right diagonal
        #Again, not starting in the cell specified
        x = row + 1
        y = col - 1
        #Loop down right through the table
        while x < self.tableSize and y >= 0:
            if table[x][y]:
                return False
            x += 1
            y -= 1

        return True

    #Output a table to a user, looking all pretty
    def display(self, table):
        #Max Number Length, so we can indent our table nicely later
        mnl = len(str(len(table)))

        #New Line
        print ""

        #Top of the table, E.g "     A B C D"
        print " "*mnl, "  ",
        for x in range(self.tableSize):
            print self.alphabet[x],
        #New Line
        print ""
        #Row spacer, E.g "   * - - - - *
        print " " * mnl, " *",
        for x in range(self.tableSize):
            print "-",
        print "*"

        #Row Counter
        #Print the actual table, with the Queens as 1's, empty space as 0
        #Also prefixed by the row number, E.g " 3 | 0 1 0 0 |
        x = 1
        for row in table:
            #If numbers are shorter than the largest number, give them extra spaces so the rows still line up
            extraPadding = mnl - len(str(x))
            #Show the number prefix, spaces, and | symbol, E.g " 6  | "
            print "", x, " "*int(extraPadding) + "|",
            #Show the value of the cell (1 or 0)
            for col in row:
                print col,
            #End of the row
            print "|"
            #Next Row
            x += 1
        #Show the same row spacer as at the top of the table, E.g "   * - - - - *
        print " " * mnl, " *",
        for x in range(self.tableSize):
            print "-",
        print "*"

    #We're done! Show output to the user
    def finish(self, table, col):
        #If we found the right number of queens
        if col == self.tableSize:
            print ""
            print "Total of", self.tableSize, "Queens placed!"
            print "Solution:"
            self.display(table)
        else:
            print ""
            print "ERROR: Could not place all queens for some unknown reason =["

    #Run the script
    def run(self):
        if not self.canRun:
            print "ERROR: Can not run"
        else:
            print ""
            print "Working..."
            print ""
            self.queue = self.getPositions(self.blankTable(), 0)
            self.loopBoard()


def run():
    qs = QueenSolver()
    while(not qs.canRun):
        print ("Enter the number of queens[8]:")
        qs.setup(int(input()))
    print ""
    qs.run()


if __name__ == "__main__":
    run()