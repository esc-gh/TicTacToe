class Player:
    
    def __init__(self, p_num):  # assign a player number for use in definition 
        run = 1
        while run:              # loop to assign the player name
            run2 = 1
            name1 = input(f"\nEnter Player {p_num} name: ").title()
            if name1.__len__() > 20:    # make sure input isn't long enough to break things
                print("Player name too long, maximum 20 characters")
            else:
                while run2:             # loop to confirm name input
                    n_check = input(f"Player 1 name is {name1}, is this correct? (Y/N): ").upper()
                    if n_check == "Y":
                        self.name = name1
                        run,run2 = 0,0
                    elif n_check == "N":
                        print("Please input again")
                        run2 = 0
                    else:
                        print("Invalid input, please use Y/N")
    
    def set_symbol(self):   # loop to choose symbol with input validation
        run = 1
        while run:
            run2 = 1
            symbol = input(f"\n{self.name} please pick a symbol (x/o): ").lower()
            if symbol == "x" or symbol == "o":
                while run2:
                    s_check = input(f"You picked {symbol}, is this correct? (Y/N): ").upper()
                    if s_check == "Y":
                        self.symbol = symbol
                        run,run2 = 0,0
                    elif s_check == "N":
                        print("Please input again")
                        run2 = 0
                    else:
                        print("Invalid input, please use Y/N")
            else:
                print("Invalid input, please use x/o")
            
    
    def get_name(self):
        return self.name
    
    def get_symbol(self):
        return self.symbol