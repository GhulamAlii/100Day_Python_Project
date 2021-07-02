############################    dAY 7   ########################

############################ hANGMAN pROJECT ##################

#Step 1

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["pakistan","srilanka","india"]

choosen_word = random.choice(word_list)

display = []

gameOver = True

lives = 6

for i in choosen_word:
    display.append("_")



while gameOver:
    if "_" in display:
        user_inp = input("guess a letter\n").lower()

        for position in range(0,len(choosen_word)):
            if user_inp == choosen_word[position]:
                display[position] = user_inp

        print(f"{' '.join(display)}")

        if user_inp not in choosen_word:
            lives -=1
        print(stages[lives])

        if lives == 0:
            print("you loose")
            break
    else:
        gameOver = False
        print("you win")
