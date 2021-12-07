############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


from replit import clear
from art import logo
import random


def play(playercards, compcards):
  print(logo)
  playercards = [random.choice(cards), random.choice(cards)]
  compcards = [random.choice(cards), random.choice(cards)]
  show_score(playercards, compcards)
  if sum(playercards) == 21:
    end(playercards, compcards)
    print("Blackjack! You Win!")
    return
  if sum(compcards) == 21:
    end(playercards, compcards)
    print("Lose, opponent has Blackjack!")
    return
  deal(playercards, compcards)


def show_score(playercards, compcards):
  print(f"\tYour cards: {playercards}, current score: {sum(playercards)}")
  print(f"\tComputer's first card: {compcards[0]}")


def show_final_score(playercards, compcards):
  print(f"\tYour final hand: {playercards}, final score: {sum(playercards)}")
  while (sum(compcards) < 17):
    compcards.append(random.choice(cards))
    if sum(compcards) > 21:
      if 11 in compcards:
        compcards[compcards.index(11)] = 1
  print(f"\tComputer's final hand: {compcards}, final score: {sum(compcards)}")
  if sum(compcards) > 21:
    print(f"Computer went over 21, You win!")
  else:
    if sum(compcards) < sum(playercards):
      print("You win!")
    elif sum(compcards) == sum(playercards):
      print("Draw!")
    else:
      print("You lose!")


def deal(playercards, compcards):
  if sum(playercards) > 21:
    if 11 in playercards:
      playercards[playercards.index(11)] = 1
      deal(playercards, compcards)
    end(playercards, compcards)
    print("You went over! You Lose!")
    return
  elif sum(playercards) == 21:
    end(playercards, compcards)
    print("You win!")
    return
  else:
    if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
      playercards.append(random.choice(cards))
      show_score(playercards, compcards)
      deal(playercards, compcards)
    else:
      show_final_score(playercards, compcards)
      

def end(playercards, compcards):
  print(f"Your final hand: {playercards}, final score: {sum(playercards)}")
  print(f"Computer's final hand: {compcards}, final score: {sum(compcards)}")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playercards = []
compcards = []
while True:
  if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    clear()
    play(playercards, compcards)
  else:
    break