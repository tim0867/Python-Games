print("Welcome to my Computer Quiz!!")

playing = input("Would you like to play?\n")
if playing.lower() != "yes":
    quit()

print("Great, let's crack on!\n")
score = 0

answer = input("What does CPU stand for?\n")
if answer.lower() == "central processing unit":
    print("Correct, Well Done!\n")
    score += 1
else:
    print("Sorry, that's wrong\n")

answer = input("What does GPU stand for?\n")
if answer.lower() == "graphical processing unit":
    print("Correct, Well Done!\n")
    score += 1
else:
    print("Sorry, that's wrong\n")

answer = input("What does RAM stand for?\n")
if answer.lower() == "random access memory":
    print("Correct, Well Done!\n")
    score += 1
else:
    print("Sorry, that's wrong\n")

answer = input("What does PSU stand for?\n")
if answer.lower() == "power supply unit":
    print("Correct, Well Done!\n")
    score += 1
else:
    print("Sorry, that's wrong\n")

print ("Well done you have scored " + str(score) + " points\n")
print ("You got " + str((score / 4) * 100) + "%\n\n")