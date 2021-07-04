import random

class RockScissorPaper:
    "this is a rockscissorpaper object"
    def __init__(self, rsp = None):
        self.rsp = rsp
    
    def tie(self, other):
        if (self.rsp == other.rsp):
            return True
        else:
            return False
    
    def win(self, other):
        rock_win = (self.rsp == "rock" and other.rsp == "scissor")
        scissor_win = (self.rsp == "scissor" and other.rsp == "paper")
        paper_win = (self.rsp == "paper" and other.rsp == "rock")
        if rock_win or scissor_win or paper_win:
            return True
        else:
            return False
    
    def loss(self, other):
        rock_loss = (self.rsp == "rock" and other.rsp == "paper")
        scissor_loss = (self.rsp == "scissor" and other.rsp == "rock")
        paper_loss = (self.rsp == "paper" and other.rsp == "scissor")
        if rock_loss or scissor_loss or paper_loss:
            return True
        else:
            return False
            
"code for the actual game"            
computer_choices = ["rock","scissor","paper"]
print("Play Rock Paper Scissors with the Computer.")
play = True
current_winrate = 0
current_wins = 0
current_games = 0
while play:
    "current winrate without excluding ties"
    if current_games > 0:
        current_winrate = current_wins/(current_games)
    current_input = (input("Input your Choice: "))
    computer_choice = RockScissorPaper(random.choice(computer_choices))
    
    if current_input == "end":
        play = False
    elif current_input == "winrate":
        print("Winrate is currently: ",current_winrate)
    else:
        current_choice = RockScissorPaper(current_input)
        if current_choice.win(computer_choice):
            current_games += 1
            current_wins += 1
            print("you win")
        elif current_choice.loss(computer_choice):
            current_games += 1
            print("you lose")
        elif current_choice.tie(computer_choice):
            current_games += 1
            print("you tie")
    