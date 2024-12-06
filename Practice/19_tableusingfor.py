t=int(input("Enter the required number table: "))

for i in range (1,11):
    print(f"{t} x {i}  =  {t*i}")


t=int(input("Enter the required number table: "))

print('''using while loop''')
i=1
while(i<11):
    print(f"{t} x {i}  =  {t*i}")
    i+=1

print("natutral number sums")

n=int(input("Enter the number till you want sum"))
i=0
sum=0
while(i<=n):
    sum+=i
    i+=1
print( sum)