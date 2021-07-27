############################ Calculator #################




def sum(n1,n2):
    return n1+n2

def min(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

opt = {
    "+":sum,
    "-":min,
    "/":div,
    "*":mul
}

def calc():

    num1 = eval(input("enter the number"))
    end = False
    while not end:





        for symbol in opt:
            print(symbol)

        operation = input("what action you want")
        num2 = eval(input("enter the number"))
        action = opt[operation]

        ans=(action(num1,num2))
        print(ans)
        re_run = input(f"type \'y\'  to continue calculate with {ans} the program or enter \'n\' to clear all")
        if re_run == "y":
            num1 = ans
        else:
            end = True
            calc()

calc()