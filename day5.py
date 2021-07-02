########################### day 5 ###############################
#----------------------------FOR LOOP----------------------------
######################### average age challenge ##################

#
# student_height = input("Enter the list of a age of student").split(" ")
#
# for i in range(0,len(student_height)):
#     student_height[i] = int(student_height[i])
# print(student_height)
# tot_num = 0
# for n in student_height:
#     tot_num+=n
# print(tot_num)
#
# tot_std=0
# for i in student_height:
#     tot_std+=1
# print(tot_std)
#
# avg_height = tot_num/tot_std
#
# print(avg_height)


######################### Highest Score challenge ###########

# student_score = input("Enter the list of a age of student").split(" ")
#
# for i in range(0,len(student_score)):
#     student_score[i] = int(student_score[i])
# print(student_score)
#
#
# no = 0
# x = 0
# for i in student_score:
#     if i>x:
#         x = i
#     no +=1
# print(x)



####################### Sum the All even number in range
#
# tot = 0
#
# for i in range(1,101):
#     if i%2==0:
#         tot+=i
#
# print(tot)

####################### fizz buzz game

#
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("buzz")
#     elif i % 3 == 0:
#         print("fizz")
#     else:
#         print(i)
#


###################### password generator
#
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#
# password=""
# for i in range(1, nr_letters+1):
#     password += random.choice(letters)
#
# for i in range(1, nr_numbers+1):
#     password += random.choice(numbers)
#
# for i in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
#
# print(password)
# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#
#
# passwords=[]
# for i in range(1, nr_letters+1):
#     passwords.append(random.choice(letters))
#
# for i in range(1, nr_numbers+1):
#     passwords.append(random.choice(numbers))
#
# for i in range(1, nr_symbols + 1):
#     passwords.append(random.choice(symbols))
#
# random.shuffle(passwords)
#
# ran_pass = ""
# for i in passwords:
#     ran_pass+=i
# print(ran_pass)


l = [1,2,3]
l2 = [1,2,3]

x = l == l2

print(x)