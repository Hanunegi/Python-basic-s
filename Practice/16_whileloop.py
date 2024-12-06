J=1

while (J<=8):
    print(J)
    J+=1


print("for loop ex:")
for K in range(1,7):
    print(K)



print("List elements")
li=[5,6,88,44,55,11,9,2]
for i in li:
    print(i )
else:                           #for can be used with else
    print("done h boss")
    
print("tuple elements")
tuple=(5,6,5,4,8,5,2,2)

for i in tuple:
    print(i)

#printing numbers from 1to100

print("numbers from 1 to 100")
n=1
while(n<=100):
    print(n)
    n+=1

#printing numbers from 100to1

print("numbers from 100 to 1")
n=100
while(n>=1):
    print(n)
    n-=1

#printing tabls using while loop
j=1
t=int(input("Enter the number fro table : "))

while(j<=10):
    print(f"{t}*{j}={t*j}")
    j+=1


for i in range (10):
    print(i)

for i in range (5, 10):
    print(i)


for i in range (1,20, 3):
    print(i)



#for factiroal of number
en=int(input("Factorial of numbrr : "))
factorial=1
for i in range (1,en+1):
    factorial*=i
print(factorial)

