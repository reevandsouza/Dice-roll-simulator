import random
print("This is a dice simulator!")
roll_it_again = "y"
while roll_it_again == "y":
    dice_face_number = random.randint(1, 6)
    if dice_face_number == 1:
        print(" -------- ")
        print("|        |")
        print("|    0   |")
        print("|        |")
        print(" ________ ")
    if dice_face_number == 2:
        print(" --------- ")
        print("|         |")
        print("|   0  0  |")
        print("|         |")
        print(" --------- ")
    if dice_face_number == 3:
        print(" -------- ")
        print("|  0     |")
        print("|    0   |")
        print("|      0 |")
        print(" -------- ")
    if dice_face_number == 4:
        print(" -------- ")
        print("|  0  0  |")
        print("|        |")
        print("|  0  0  |")
        print(" -------- ")
    if dice_face_number == 5:
        print(" -------- ")
        print("| 0    0 |")
        print("|    0   |")
        print("| 0    0 |")
        print(" -------- ")
    if dice_face_number == 6:
        print(" -------- ")
        print("|  0  0  |")
        print("|  0  0  |")
        print("|  0  0  |")
        print(" -------- ")
    roll_it_again = input("Enter y to roll it again : ")
