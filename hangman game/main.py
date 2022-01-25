import random
from hangman_art import stages
from hangman_word import word_list
from hangman_art import logo

choosen_word = random.choice(word_list)
solution = choosen_word
print(logo)
display = []
for i in range(len(choosen_word)):
    display += "_"
lives =  6
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if choosen_word[position] == guess:
            display[position] = letter
    print(display)
    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lost!")
    print(f"{' '.join(display)}")
    print(stages[lives])
    if "_" not in display:
        print("You won!")
        end_of_game = True
print(f"The word was {solution}")
