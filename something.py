import random

class Hand():
    def __init__(self, hand_name):
        self.hand_name = hand_name
        self.play = ""

    def rock(self):
        self.play = "rock"

    def paper(self):
        self.play = "paper"

    def scissors(self):
        self.play = "scissors"

class Dealer():
    def __init__(self):
        self.dealer_hand = Hand("Dealer")

    def make_play(self):
        possible_plays = ["rock","paper","scissors"]
        choice = random.choice(possible_plays)
        if choice == "rock":
            self.dealer_hand.rock()
        elif choice == "paper":
            self.dealer_hand.paper()
        elif choice == "scissors":
            self.dealer_hand.scissors()

class Player():
    def __init__(self, name):
        self.player_name = name
        self.player_hand = Hand(name)

    def make_play(self, choice):
        if choice == "rock":
            self.player_hand.rock()
        elif choice == "paper":
            self.player_hand.paper()
        elif choice == "scissors":
            self.player_hand.scissors()

def RPSGame():
    player_name = input("what is your name player?:  ")
    player = Player(player_name)
    dealer = Dealer()
    print("Welcome to Rock, Paper and Scissors, {}!".format(player_name))
    choice = input("what will you play? [rock, paper, scissors]:  ")
    player.make_play(choice)
    player_choice = player.player_hand.play
    dealer.make_play()
    dealer_choice = dealer.dealer_hand.play
    print("you have played {}".format(player_choice))
    print("opponent has played {}".format(dealer_choice))
    if player_choice == "rock":
        if dealer_choice == "paper":
            print("you lose!")
        elif dealer_choice == "scissors":
            print("You Win!")
        else:
            print("no one wins.")
    if player_choice == "paper":
        if dealer_choice == "scissors":
            print("you lose!")
        elif dealer_choice == "rock":
            print("You Win!")
        else:
            print("no one wins.")
    if player_choice == "scissors":
        if dealer_choice == "rock":
            print("you lose!")
        elif dealer_choice == "paper":
            print("You Win!")
        else:
            print("no one wins.")

if __name__ == "__main__":
    RPSGame()


