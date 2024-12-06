a=int(input("enter the number who's factorial is required"))

product=1
for i in range(1,a+1):
    product=product*i
    i+=1
print(product)