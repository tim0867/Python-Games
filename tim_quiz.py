print("\nHi there, Welcome to Tim's Quiz!\n")

playing = input("Would you like to play?\n")
if playing.lower() != "yes":
    quit()
else:
    print("\nAwesome, let's crack on!!\n")

score = 0

print("Question 1.\n")
answer = input("Which Irish city's name is derived from the Irish word for marsh?\n")
if answer.lower() != "Cork":
    print("Sorry, that's wrong. The answer was Cork.\n")
else:
    print("Correct, well done!\n")
    score =+ 1

print("Question 2.\n")
answer = input("Name the type of animal which killed Captain Hook in Peter Pan\n")
if answer.lower() != "crocodile":
    print("Sorry, that's wrong. It was a crocodile.\n")
else:
    print("Correct, well done!\n")
    score =+ 1

print("Question 3.\n")
answer = input("What does a seismograph [pr. 'size-ma-graf' ] measure?\n")
if answer.lower() != "earthquakes":
    print("Sorry, that's wrong. It was earthquakes.\n")
else:
    print("Correct, well done!\n")
    score =+ 1

print("Question 4.\n")
answer = input("How many of his five stones did David use to slay Goliath?\n")
if answer.lower() != "one":
    print("Sorry, that's wrong. It was one\n")
else:
    print("Correct, well done!\n")
    score =+ 1

print("Question 5.\n")
answer = input("Fill in the missing word from the famous quote, 'There are lies, damned lies, and ______'\n")
if answer.lower() != "statistics":
    print("Sorry, that's wrong. It was statistics.\n")
else:
    print("Correct, well done!\n")
    score =+ 1

print("Question 6.\n")
answer = input("YES or NO: An email address can also be a website address?\n")
if answer.lower() != "No":
    print("Sorry, that's wrong!\n")
else:
    print("Correct, well done!\n")
    score =+ 1

print("Question 7.\n")
answer = input("TRUE or FALSE: Meteors are meteorites which have landed?\n")
if answer.lower() != "False":
    print("Sorry, that's wrong!\n")
else:
    print("Correct, well done!\n")
    score =+ 1

print("Question 8.\n")
answer = input("YES or NO: Hyundai cars originate in South Korea?\n")
if answer.lower() != "Yes":
    print("Sorry, that's wrong!\n")
else:
    print("Correct, well done!\n")
    score =+ 1

print("Question 9.\n")
answer = input("Which actor starred in the movie The Cable Guy ?\n")
if answer.lower() != "Jim Carrey":
    print("Sorry, that's wrong. It was Jim Carrey\n")
else:
    print("Correct, well done!\n")
    score =+ 1

print("Question 10.\n")
answer = input("Name the metal that has the chemical symbol Ag?\n")
if answer.lower() != "silver":
    print("Sorry, that's wrong. It was Silver\n")
else:
    print("Correct, well done!\n")
    score =+ 1

print("Congratulations, you scored " + str(score) + " points\n\n")
print("That's " + str((score / 10) * 100) + "%" + " - Fantastic\n\n")

