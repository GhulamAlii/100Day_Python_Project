###################################### Day 8 ###############################

################################# Fucntions ####################################


################################  Area Calculator Project #######################

import math
#
# def paint_areaCalc(height, width, cover):
#     ans = (height*width) / cover
#     rpValue = math.ceil(ans)                   # roundof the number
#     print(f"you need {rpValue} can of paint")
#
# test_h = int(input("Enter the Height"))
# test_w = int(input("Enter the width"))
# coverage = 5
#
# paint_areaCalc(height=test_h,width=test_w,cover=coverage)
#


##########################      PRIME NUMER CHECKER ###############################

def prime_check(number):
    prime = True
    for i in range(2,number):
        if number % i == 0:
            prime = False

    if prime:
        print("this is a prime Number")
    else:
        print("This is not prime Number")


num = int(input("Enter the number\n"))
prime_check(number=num)