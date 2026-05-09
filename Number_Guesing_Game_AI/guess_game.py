import random

Secret_number = random.randint(1 , 10)

while(True):
    guess_number = int(input("Guess a number between 1 to 10"))

    if guess_number == Secret_number:
        print("Yayy!!You guessed the correct number!")
        break
    elif guess_number > Secret_number:
        print("Too high, guess Smaller number")
    else:
        print("Too low , guess larger number")