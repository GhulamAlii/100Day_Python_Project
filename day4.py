#################### Day 4 ####################

#################### head and tail program ################

# import random
#
# # coin = random.randint(0,1)
# #
# # if coin == 1:
# #     print("head")
# # else:
# #     print("tail")

#################### bank Roulette ###########

# import random
#
# name_inp = input("enter the name by seprated comma\n")
# person_name = name_inp.split(", ")
#
#     #######  With randint
#
# # random_person = random.randint(0,len(person_name)-1)
# # bill_person = person_name[random_person]
# # print(bill_person)
#
#     ####### with randChoice
#
# bill_boy = random.choice(person_name)
# print(bill_boy)
#

######################### Treasur game ###############

#
# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this row 👇
#
#
# row = int(position [0])
# col = int(position [1])
#
# map[row-1][col-1] = " x   "
#
# #Write your code above this row 👆
#
# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

#################### Rock Paper Seccior Game $$$$$$$$$$$$$$

# import random
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
#
# action = [rock,paper,scissors]
#
# user_inp = int(input("1:Rock\n2:Paper\n3:scissors"))
#
# user_ans = action[user_inp-1]
# print(f"You Choose \n{user_ans}")
#
# cmp_select = random.randint(1,3)
#
# cmp_ans = action[cmp_select-1]
# print(f"The computer Choose \n{cmp_ans}")
#
# if cmp_ans == user_ans:
#     print("you both are tie")
# elif cmp_ans == 0 and user_ans == 2:
#     print("You win")
#
# elif cmp_ans == 2 and user_ans == 0:
#     print("You lose")
#
# elif cmp_ans > user_ans :
#     print("You loss")
#
# elif cmp_ans < user_ans :
#     print("You win")

