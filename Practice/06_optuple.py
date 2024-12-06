name=(1,2,5,"hanu","ruchi",False,"hanu","hanu","hanu")
print(name)


no=name.count("hanu")   #count the occurences
print(no)

print("length of the tuple is : ",len(name))
print(name.index("ruchi"))
print(name[1:6])

sirname=("negi","rawat")
new=name+sirname
print(new)
print(name+sirname)

repeat=name*5
print(repeat)

print("ruchi" in name)   #true/false
print(5 in name)
print(11 in name)



#list sum
a=[5,6,3,5,1,5]
print("sum of list is: ",sum(a))