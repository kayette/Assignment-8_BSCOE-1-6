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

def pauseSlow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*50.0/typing_speed)

def userGuess():
    num = 1
    userNums = []
    while num <= 3:
        try:
            getInput = int(input(f"\nGUESS {num}\nEnter a number from 0 to 9: ")) 
        except ValueError:
            print("\nInvalid input. Please select numerical values only.\n")
            continue
        if (getInput >= 0) and (getInput <= 9):
            if getInput not in userNums:
                userNums.append(getInput)
            else:
                print("\nInvalid value. You have already selected this number.\n")
                continue
        else:
            print("\nInvalid value. Selection is beyond the scope of the lottery numbers.")
            continue
        num += 1
    return sorted(userNums)

def winLotto():
    randNums = []
    for i in range(3):
        lottoNum = random.randint(0,10)
        while lottoNum in randNums: 
            lottoNum = random.randint(0,10)
        randNums.append(lottoNum)
    return sorted(randNums)

def getResult(userGuess, winLotto):
    counter = 0
    for getInput in userGuess:
        if getInput in winLotto:
            counter+=1
    retries = 0
    time.sleep(1)
    print("\n \nYour guesses are: ")
    time.sleep(2)
    pauseNext(f"{userGuess}\n")
    print("\nToday's winning numbers are: ")
    time.sleep(2)
    pauseSlow(f"{winLotto}\n")
    print(f"\nYou guessed {counter} number/s correct!\n")
    if userGuess == winLotto:
        pauseNext("Congratulations! \n\033[92m\033[1mY O U  W O N !\033[21m\033[0m \n")
        time.sleep(1)
        print(f"It took you {retries} to get the winning numbers.\n")
    else:
        pauseNext("\n\033[1m\033[91mY O U  L O S E \033[0m \n")
        retries +=1

def lotteryProper():
    playAgain = True
    while playAgain:
        num = userGuess()
        win = winLotto()
        getResult(num, win)
        lottoLoop()

def lottoLoop():
    confirm = 'y'
    while 'y' in confirm:
        answer = input("\n \nDo you want to play again?\n").lower()
        if "y" in answer:
            pause("\nAlright, may the odds be ever in your favor.\n")
            time.sleep(2)
            lotteryProper()
        elif "n" in answer:
            pauseNext("\nThank you for playing!\n")
            sys.exit()
        if not("y" in answer) and not("n" in answer):
            pause("\nInvalid input.\n")
            continue

lotteryProper()