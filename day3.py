                            # Control overflow IF /ELSE STATMENT

################################### Ride Cheacker

# height = int(input("Whats Your Height\n"))
#
#
# if height > 120:
#     print("you can ride")
#     age = int((input("write your age")))
#
#     if age >18:
#         print("your ride charge is 12$")
#     elif age >=12:
#         print("your ride charge is 7$")
#     else:
#         print("your ride charge is 5$")
#
# else:
#     print("your are not allowed")

########################   Pizza Order

# print("Welcome to Pizza Zilla")
#
# size = input("what the size of a pizza you want: S , L or M")
# pepperoni = input("do you add pepproni: Y , N ")
# extra_cheese = input("do you add extra cheese : Y , N ")
#
# bill = 0
# if size == "S":
#    bill += 15
# elif size == "M":
#     bill =+ 20
# else:
#     bill =+30
#
# if pepperoni == "Y":
#    if size == "S":
#        bill += 3
#    else:
#        bill =+5
#
# if extra_cheese == "Y":
#    if size == "S":
#        bill += 3
#    else:
#        bill =+5
#
# print(f"Your Subtotal is {bill}")

##################### Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



name1.lower()
name2.lower()


t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")


l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e = name1.count("e") + name2.count("e")


true = t+r+u+e
love = l+o+v+e

ans = str(true) + str(love)
point = int(ans)
if point < 10 or point > 90:
  print(f"Your score is {point}, you go together like coke and mentos.")

elif point >= 40 and point <= 50:
  print(f"Your score is {point}, you are alright together.")

else:
  print(f"Your score is {point}.")
