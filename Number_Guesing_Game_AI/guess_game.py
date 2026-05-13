import random

print("Welcome to Guessing Game!!")

difficulty_level = int(input("Choose dificulty level between 1 to 3"))

if difficulty_level == 1:
    Secret_number = random.randint(1 , 10)

elif difficulty_level == 2:
        Secret_number = random.randint(1 , 50)


else:
        Secret_number = random.randint(1 , 100)


attempts = 0
won = False

while(attempts < 5):
    guess_number = int(input("Guess a number between 1 to 10"))

    attempts += 1

    if guess_number == Secret_number:
        print("Yayy!!You guessed the correct number!")
        print("Attempts : ", attempts)
        won = True
        break
    elif guess_number > Secret_number:
        print("Too high, guess Smaller number")
    else:
        print("Too low , guess larger number")


if won == False:
     print("Game Over!")
     print(f"Correct Number was {Secret_number}")