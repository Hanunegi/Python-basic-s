a=int(input("Enter your age: "))

if(a>18):
    print("You are eligible for voting")
    print("You are eligible for drinking")
    print("You are eligible for marrying")
    
elif(a<0):
    print("are you kidding me jerk, when the age is count in negative")
elif(a==0):
    print("101 You are not born yet")

else:
    print("You are not eligible for voting")
    print("You are not eligible for drinking & smoking")
    print("You are not eligible for marring")


#multiple if statment
b=int(input("Enter your age: "))

if(b%2==0):
    print("Age is a Even number")    #1st if statement , it is independent as it is not followed by any else

if(b>18):   #2nd if statement with else ,elif ladder
    print("You are eligible for voting")
    
elif(b<0):
    print("are you kidding me jerk, when the age is count in negative")
elif(b<0):
    print("are you kidding me jerk, when the age is count in negative")
elif(b==0):
    print("101 You are not born yet")

else:
    print("You are not eligible for voting")
  
#finding biggest of the enterd number

a1=int(input("Enter the 1 number = "))
a2=int(input("Enter the 2 number = "))
a3=int(input("Enter the 3 number = "))
a4=int(input("Enter the 4 number = "))

if(a1>a2 and a1>a3 and a1>a4):
    print("HEY! The 1st number is bigger.")
elif(a2>a1 and a2>a3 and a2>a4):
    print("HEY! The 2nd number is bigger.")
elif(a3>a2 and a3>a1 and a3>a4):
    print("HEY! The 3rd number is bigger.")
elif(a4>a2 and a4>a3 and a4>a1):
    print("HEY! The 4th number is bigger.")



number=int(input("Enter the number"))
if(number%2==0):
    print("It is a even number")
else:
    print("It is a odd number");
