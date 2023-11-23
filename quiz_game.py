print("Welcome to my Stock Market Quiz!")

is_playing = input("Do you want to play? ")

if is_playing.lower() != "yes":
    quit()
else:
    print("Okay! Let's play :D")
    score = 0
    answer = input("What does a green candle indicate in the Stock Market? ")
    if answer.lower() == "bullish":
        print('Correct!')
        score += 1
    else:
        print('Incorrect.)')

    answer = input("What does a red candle indicate in the Stock Market? ")
    if answer.lower() == "bearish":
        print('Correct!')
        score += 1

    else:
        print('Incorrect.)')
    
    answer = input("What is the name of the ETF of the S&P 500? ")
    if answer.lower() == "spy":
        print('Correct!')
        score += 1

    else:
        print('Incorrect.)')
    
    answer = input("What is the #1 holding in SPY? ")
    if answer.lower() == "aapl":
        print('Correct!')
        score += 1
    else:
        print('Incorrect.)')

    answer = input("Who is the Wolf of Wall Street? ")
    if answer.lower() == "jordan belfort":
        print('Correct!')
        score += 1
    else:
        print('Incorrect.)')

print("You got a total score of", score, "!")