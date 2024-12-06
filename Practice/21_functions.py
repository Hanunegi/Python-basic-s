


def avg():   #function creation
    a=int(input("Enter the number = "))
    b=int(input("Enter the number = "))
    c=int(input("Enter the number= "))
    d=int(input("Enter the number = "))

    average=(a+b+c+d)/4
    print(average)

avg()   #function call


def greet(): # function without arguments

    a=input("your name plz : ")
    print(f"have a good day mr./ms {a}")

greet()

def greet1(name,end="thankyou"): #function with argument if value of end is not given by default it is thankyou then
    print(f"hello {name} we wish you a happy birthday " +end)

greet1("hanumant singh negi", "sir")
