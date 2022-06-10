class Board:
    
    def __init__(self, grid = [" "]*9): # init with default grid set to be full of empty spaces
        self.grid = grid
    
    def show(self): # visual output of play grid
        print("\n\t"+self.grid[0]+" | "+self.grid[1]+" | "+self.grid[2]+"\n\t- | - | -\n\t"+self.grid[3]+" | "+self.grid[4]+" | "+self.grid[5]+"\n\t- | - | -\n\t"+self.grid[6]+" | "+self.grid[7]+" | "+self.grid[8]+"\n")
    
    def status(self): # visual output of numbered grid for symbol placement
        n_grid = ["1","2","3","4","5","6","7","8","9"]
        print("\n\t"+n_grid[0]+" | "+n_grid[1]+" | "+n_grid[2]+"\n\t- | - | -\n\t"+n_grid[3]+" | "+n_grid[4]+" | "+n_grid[5]+"\n\t- | - | -\n\t"+n_grid[6]+" | "+n_grid[7]+" | "+n_grid[8]+"\n")

    def play(self): # visual output of both grids in parallel for easier picking
        n_grid = ["1","2","3","4","5","6","7","8","9"]
        print("\n\t"+self.grid[0]+" | "+self.grid[1]+" | "+self.grid[2]+"\t"+n_grid[0]+" | "+n_grid[1]+" | "+n_grid[2])
        print("\t"+"- | - | -\t- | - | -")
        print("\t"+self.grid[3]+" | "+self.grid[4]+" | "+self.grid[5]+"\t"+n_grid[3]+" | "+n_grid[4]+" | "+n_grid[5])
        print("\t"+"- | - | -\t- | - | -")
        print("\t"+self.grid[6]+" | "+self.grid[7]+" | "+self.grid[8]+"\t"+n_grid[6]+" | "+n_grid[7]+" | "+n_grid[8]+"\n")
    
    def set_index(self, num, symbol): # change a grid square to a symbol
        self.grid[num] = symbol
    
    def get_index(self, num):       # output the value of a grid square
        return self.grid[num]
    
    def victory(self, symbol):  # check for the 8 victory conditions via 3 squares which are common to them
        self.win = False
        while self.grid[4] == symbol:
            if self.grid[4] == self.grid[0] == self.grid[8] or self.grid[4] == self.grid[2] == self.grid[6]or self.grid[4] == self.grid[3] == self.grid[5]or self.grid[4] == self.grid[1] == self.grid[7]:
                self.win = True
            break
        while self.grid[6] == symbol:
            if self.grid[6] == self.grid[0] == self.grid[3] or self.grid[6] == self.grid[7] == self.grid[8]:
                self.win = True
            break
        while self.grid[2] == symbol:
            if self.grid[2] == self.grid[0] == self.grid[1] or self.grid[2] == self.grid[5] == self.grid[8]:
                self.win = True
            break
        return self.win
    
    def check(self):    # if there are any blank squares returns False, when grid full returns True
        for i in range(0,9):
            if self.grid[i] == " ":
                return False
        return True
                