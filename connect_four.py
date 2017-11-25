class Game:
    def __init__(self,row,column,l):
        self.row = size
        self.column = column
        self.field = []
        for _ in range(ROWS):
            field.append(list(input().strip()))
        self.tokens = ["X","0"]
        self.currPlayer = len(self.tokens)
        self.l = l

    def main(self):
        running = True
        movesLeft = self.size*self.size
        while(running and movesLeft > 0):
            self.currPlayer = (self.currPlayer+1) % len(self.tokens)
            x,y = self.place()
            movesLeft -= 1
            running = not self.won(x,y)
            self.display()
        if running:
            print "It was a draw! Who could have guessed!"
        else:
            print "The winner is player \"" + self.tokens[self.currPlayer] + "\""

    def get(self, x, y):
        if 0 <= x < len(self.field) and 0 <= y < len(self.field[x]):
            return self.field[x][y]
        else:
            return False

    def won(self, x, y):
        xline = yline = diagOne = diagTwo = 0
        for i in range(-4, 5):
            if xline > 3 or yline > 3: return True
            xline = xline+1 if self.get(x+i, y) == self.tokens[self.currPlayer] else 0
            yline = yline+1 if self.get(x, y+i) == self.tokens[self.currPlayer] else 0
            if diagOne > 3 or diagTwo > 3: return True
            diagOne = diagOne+1 if self.get(x+i,y+i) == self.tokens[self.currPlayer] else 0 
            diagTwo = diagTwo+1 if self.get(x-i,y-i) == self.tokens[self.currPlayer] else 0
        return False

    def display(self):
        buff = printbuff = ""
        for i in range(self.size):
            for j in range(self.size):
                value = self.get(i,j)
                buff += value if value != False else " "
            buff += "\n"
        reversebuff = [row[::-1] for row in buff.split("\n")[:-1]]
        for i in range(0, self.size):
            for j in reversebuff:
                printbuff += "|" + j[i]
            printbuff += "|\n"
        printbuff += "--"*self.size + "-"
        print printbuff

    def place(self):
        col = l[i]
        if col < self.size and len(self.field[col]) < self.size:
            self.field[col].append(self.tokens[self.currPlayer])
            return col,len(self.field[col])-1
        else:
            print "Invalid placement"
            return self.place()

if __name__ == '__main__':
    t=int(input())
    for i in t:
        l=[]
        m,n,a=map(int, input().strip().split())
        for j in a:
            l.append(int(input()))
            Game(m,n,l).main()

    