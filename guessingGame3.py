import random


# core function are evaluating inputs
def evaluateInput(answer, chancesLeft, top):

    print(f"You have {chancesLeft} chances to guess a random number between 1 and {top}.")

    while chancesLeft:
        guess = input(f"Guess a number between 1 and {top}: ")

        # handle non-int guesses
        try:
            guess = int(guess)
        except ValueError:
            print("You did not input an integer. Try again\n")
            continue

        # handle numbers outside boundary
        if guess < 1 or guess > top:
            print(f"Numbers should be between 1 and {top}")

        if guess == answer:
            print("You got it right!")
            break
        else: print("That was wrong")

        chancesLeft -= 1
        if chancesLeft == 0: print("Game Over\n")
        elif chancesLeft == 1: print(f"You have {chancesLeft} chance left\n")
        else: print(f"You have {chancesLeft} chances left\n")
    

def easy():
    chancesLeft = 6
    top = 10
    answer = random.choice(range(1,11))
    evaluateInput(answer, chancesLeft, top)

def medium():
    chancesLeft = 4
    top = 20
    answer = random.choice(range(1,21))
    evaluateInput(answer, chancesLeft, top)

def hard():
    chancesLeft = 3
    top = 50
    answer = random.choice(range(1,51))
    evaluateInput(answer, chancesLeft, top)
        

print("\nWelcome to a number guessing game!")
print("You could pick easy, medium or hard stages")

for i in range(3):
    level = input('enter "1" for easy, "2" for medium, or "3" for hard: \n')
    try: 
        level = int(level)
    except ValueError:
        print("integer not entered")
        continue
    
    if level < 1 or level > 3:
        print("option slected not valid")
        continue

    break

if level == 1: easy()
elif level == 2: medium()
elif level == 3: hard()

