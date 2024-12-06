

def factorial(n):
    
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)
     
n=int(input("Enter a number for finding out its factorial : ")) 
print(f"The factorial of given number  is : {factorial(n)}")

print(factorial(4))







    