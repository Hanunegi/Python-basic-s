import array
#ladoo=[];   #or create an array like this but when we check type of this it shes LIST
    
ladoo=array.array('i',[]);    #also like this we can create empty array

n=int(input("Enter the number of elements in the array : "));

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    ladoo.append(element)

print("The Array is:", ladoo);

a=int(input("ENTER the elemets whos occurence is counted : "))
occurences=ladoo.count(a);
print(f"{a} = {occurences}");
ladoo.reverse();   #reverse the array
print(type(ladoo));






