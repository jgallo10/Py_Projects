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

#list of words, word picked, length of word, and lives variable
word_list = ["aardvark", "baboon", "camel"]
word = random.choice(word_list)
word_len = len(word)
lives = 6
print(word)

#loop to create empty list 
player_list = []
for _ in range(word_len):
    player_list.append("_")
print(player_list)
    

#while loop inorder to keep getting player guesses
while "_" in player_list:

    #player choosing letter
    word_guess = input("Please choose a letter. \nYou chose: ").lower()

    for position in range(word_len):
        letter = word[position]
        if word[position] == word_guess:
            player_list[position] = letter
            
     
    if word_guess not in player_list:
        lives -= 1
        print(f"\nSorry try again \nYou have {lives} left! \n")
        if lives < 1:
            print(stages[lives]) 
            print(f"Sorry you have {lives} lives left. \nYOU LOSE!")
            break          
    
    print(stages[lives])
    print(player_list)
    print("----------------------------------------------------\n")