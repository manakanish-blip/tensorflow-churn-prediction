import random
def guess_the_number():
    secret_number= random.randint(1,100)
    attempts=0
    max_attempts=7

    print("WELCOME TO THE GUESS THE NUMBER GAME")
    print("I'm thinking of a number between 1 to 100")

    for current_attempt in range(1,max_attempts+1):

        while True:
            try:
                user_input=input(f"Attempt{current_attempt}/{max_attempts}-Enter your guess:")
                user_guess=int(user_input)
                break
            except ValueError:
                print("Please enter valid integer")

        if user_guess<secret_number:
            print("Too low! Try again")
        elif user_guess>secret_number:
            print("Too high! Try again")
        else:
            print("Congratulation you guess the right number in",attempts,"attempts")
            return

    print("Game Over! You've run out of your attempts")
    print( "The secret number is:",secret_number)
                

if __name__ == "__main__":
    guess_the_number()
