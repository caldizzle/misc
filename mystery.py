import random

won = False
play_again = "y"
question_number = 1
higher = ["Guess higher. ", "You're guess is to low. ", "Try again - guess higer. "]
lower = ["Guess lower. ", "You're guess is to high. ", "Try again - guess lower. "]

name = input("Whats you're name? ")

while play_again == "y" or play_again == "Y":
    min = input("What do you want the min to be? ")
    max = input("What do you want the max to be? ")
    min = int(min)
    max = int(max)
    print("Hello " + name + "! I am thinking of a random number between " + str(min) + ", and " + str(max) + ".")
    number = random.randint(min, max)
    question_number = 1
    won = False

    while question_number < max/10-2 and won == False:
        guess = input("What is your guess for my number? ")
        guess = int(guess)
        if guess > number:
            print(random.choice(lower))
        if guess < number:
            print(random.choice(higher))
        if guess == number:
            print("You won!!!")
        won = True

    if question_number > 7:
        print("Sorry, you ran out of questions. ")
        play_again = input("Would you like to play again? y/n. ")
