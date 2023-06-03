print("Welcome to my Computer Quiz!!")

playing = input("Would you like to play?\n")
if playing != "yes":
    quit()

print("Great, let's crack on!\n")

answer = input("What does CPU stand for?\n")
if answer == "central processing unit":
    print("Correct, Well Done!\n")
else:
    print("Sorry, that's wrong\n")

answer = input("What does GPU stand for?\n")
if answer == "graphical processing unit":
    print("Correct, Well Done!\n")
else:
    print("Sorry, that's wrong\n")

answer = input("What does RAM stand for?\n")
if answer == "random access memory":
    print("Correct, Well Done!\n")
else:
    print("Sorry, that's wrong\n")

answer = input("What does PSU stand for?\n")
if answer == "power supply unit":
    print("Correct, Well Done!\n")
else:
    print("Sorry, that's wrong\n")