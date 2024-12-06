
def f_to_c():
    f=int(input("Enter temperature in Farenhite : "))
    c=5*(f-32)/9
    print(f"Temperature in celcius is {c}")
f_to_c()


print("inches to centimeters : ")

def inch_to_cent(inch):
    return inch*2.5
   
n=int(input("Enter the valu in inches : "))
print(f"the valuef of following in centimeters is : {inch_to_cent(n)}")

