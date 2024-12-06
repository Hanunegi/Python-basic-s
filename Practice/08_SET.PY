e=set()  #empety set   #e={} will create empety dicitionary
s={1,2,3,5,6,5,4,2,4,4,4,4,4,4}  #set  #also one value is considerd only once

print(type(e))
print(s,type(s))

x=set()
x.add(20)
x.add("20")
print(x)



#methods
s.add("hanumant")
print(s)


print(len(s))
s.remove(4)
print(s)

s.pop()  #remove random element
print(s)
s.pop()  #remove random element
print(s)

s2={9,10,11,2,1,2,"ruchi"}
print(s.union(s2))
print(s.intersection(s2))

#problem
set3=set()
r=input("enter the number 1 ")
set3.add(int(r))
r=input("enter the number 2 ")
set3.add(int(r))
r=input("enter the number 3 ")
set3.add(int(r))
r=input("enter the number 4 ")
set3.add(int(r))
r=input("enter the number 5 ")
set3.add(int(r))
r=input("enter the number 6 ")
set3.add(int(r))
r=input("enter the number 7 ")
set3.add(int(r))
print(set3)

set3.clear()   #clear the set
print(set3)