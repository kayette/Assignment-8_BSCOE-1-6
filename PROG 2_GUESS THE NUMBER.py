import time, sys, random
typing_speed = 50

def pause(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*4.0/typing_speed)

def pauseNext(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

def getNum():
    getName = input("\nEnter your name to proceed: ")
    pauseNext(f"\nHello, {getName}!\nWelcome to  ‧₊˚✧  GUESS THE NUMBER  ‧₊˚✧")  
    time.sleep(1)
    pause("\nThe program will generate a random integer from 1 to 100. To win, you have to guess it correctly! Please get ready.\n")
    time.sleep(1)
    counter = 0
    randNum = random.randint(0,101)
    guess = True
    while guess:
        try: 
            userGuess = int(input("\nEnter your guess: "))
        except ValueError:
            print("\nInvalid value. Please enter an integer.\n")
            continue
        if randNum != userGuess:
            if randNum > userGuess:
                print("Your guess is less than the mystery number. Maybe try increasing the value of your guess?")
                time.sleep(0.5)
                counter+=1
            elif randNum < userGuess:
                print("Your guess is greater than the mystery number. Maybe try lowering the value of your guess?")
                time.sleep(0.5)
                counter+=1
        else:
            time.sleep(1)
            pause(f"\nCongratulations, {getName}! You guessed it right. The number is {randNum}.\n")
            print(f"It took you {counter} tries to get the correct value.\n")
            break

getNum()