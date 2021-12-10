import os
import random

def cls():
  os.system("cls" if os.name == "nt" else "clear")

def make_code():
  code = ""

  for i in range(4):
    digit = random.randint(0, 9)

    while str(digit) in code:
      digit = random.randint(0, 9)

    code += str(digit)

  return code

def get_guess():
  while True:
    guess = input("Enter a guess: ")

    if len(guess) == len(code) and all(digit in "0123456789" for digit in guess):
      return guess
    else:
      print("Invalid guess.\n")

def check_guess(guess):
  correct = 0
  misplaced = 0
  used_digits = []

  for i in range(len(guess)):
    if guess[i] == code[i]:
      correct += 1
      used_digits.append(guess[i])

  for i in range(len(guess)):
    if guess[i] in code and guess[i] not in used_digits:
      misplaced += 1
      used_digits.append(guess[i])

  return correct, misplaced

cls()
print()

print("The secret code is 4 non-repeating digits from 0-9.\n")

code = make_code()
game_over = False
num_guesses = 0

while not game_over:
  guess = get_guess()
  num_guesses += 1
  correct, misplaced = check_guess(guess)

  if correct == len(code):
    game_over = True

    if num_guesses == 1:
      print("Wow, you cracked the code on the first try!")
    else:
      print(f"You cracked the code in {num_guesses} tries!")
  else:
    print(f"Number of correctly placed digits: {correct}")
    print(f"Number of misplaced digits: {misplaced}\n")
