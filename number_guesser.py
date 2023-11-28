import random

max_range = input("Type in a number: ")

if max_range.isdigit():
    max_range = int(max_range)

    if max_range <= 0:
        print("Please type a number greater than 0.")
        quit()
else:
    print("Please type a number.")

# Generate any number between 0 and the users input
rand_num = random.randrange(max_range)
count_guess = 0

while True:
    count_guess += 1
    user_guess = input("Guess a number between 0 and " + str(max_range) + " ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == rand_num:
        print("You guessed right! :)")
        break
    elif user_guess > rand_num: 
        print("Guess a little lower...")
    else:
        print("Guess a little higher...")

print("It took you", count_guess, "tries!")