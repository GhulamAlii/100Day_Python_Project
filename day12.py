######################################## Number Guessing Game $$$$$$





import random

number = random.randint(1,100)

def_inp = int(input("Enter the Number of  dificulty  level you want \n1: Easy\n2: Hard\n"))

flag = 0

if def_inp == 1:
    flag = 10
elif def_inp == 2:
    flag = 5
else:
    print("Incorrect Value Enter")

for i in range(1,flag+1):

    inp_num = int(input("Enter Your Guess Number\n"))

    if i == flag:
        print(f"Your Guess is incorrect The Answer Is {number}")
        break
    elif inp_num == number:
        print("Congrat You Guess Correct Number\n")
        break

    elif inp_num > number:
        print("your guess is high \n")
        
    elif inp_num < number:
        print("your guess is low\n ")
      
    elif i == flag:
        print(f"Your Guess is incorrect The Answer Is {number}")
        