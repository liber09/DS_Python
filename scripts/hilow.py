

import random

max = 10 #max value
min = 1 #min value

score = 0 #current player score

#The random number between min & max
random_num = random.randint(min, max)

while True:
    print("Your number is: ", random_num)

    #Player guess
    guess = input("Let's guess, higher or lower? (h/l) (exit): ")

    if guess != "h" and guess != "l" and guess != "exit":
        continue

    if guess == "exit":
        print("Thank you for playing, better luck next time!")
        break

    #new random number
    new_num = random.randint(min, max)

    #Correct guess
    if new_num >= random_num and guess == "h":
        score += 1
        print("Wohooo!! Right, your current score is: ", score)
    #Correct guess
    elif new_num <= random_num and guess == "l":
        score += 1
        print("Wohooo!! Right, your current score is: ", score)    
    else:
        #Wrong guess, reset score
        print("Ohhh noooo!!! That's wrong. Your score ended at: ", score)
        score = 0
        print("Try again")

    random_num = new_num