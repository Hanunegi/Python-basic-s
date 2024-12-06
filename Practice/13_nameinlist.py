list=["hanu","ruchi","anjali","tanu","hanumant",25,30,18,75,85,45,45]    #list can take anytype of element
print(list)

Name=input("Enter your name here = ")

if(Name in list):
    print("Your name is in list & shortlisted")

else:
    print("Sorry! your name not found in the list, plz try next year....")

list.append(86)
list.append("what")
print(list)
list.reverse()
print(list)
list.insert(5,"love")
print(list)
list.remove("tanu")
print(list)
list.pop(1)
print(list)

l1=int(input("Enter the number of elements in list"))
list1=[]
for i in range(l1):
    element=int(input(f"enter the elemnt numbre{i+1} : "))
    list1.append(element)
print(list1)

