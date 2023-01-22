

import random

max = 10
min = 1

score = 0

random_num = random.randint(min, max)

while True:
    print("Your number is: ", random_num)

    guess = input("Let's guess, higher or lower? (h/l) (exit): ")

    if guess != "h" and guess != "l" and guess != "exit":
        continue

    if guess == "exit":
        print("Thank you for playing, better luck next time!")
        break

    new_num = random.randint(min, max)

    if new_num >= random_num and guess == "h":
        score += 1
        print("Wohooo!! Right, your current score is: ", score)
    elif new_num <= random_num and guess == "l":
        score += 1
        print("Wohooo!! Right, your current score is: ", score)
    else:
        print("Ohhh noooo!!! That's wrong. Your score ended at: ", score)
        score = 0
        print("Try again")

    random_num = new_num