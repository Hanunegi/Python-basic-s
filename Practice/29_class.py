class myself:                   #class creation     #only templaet defined no memory allocation
    name="Hanumant"
    world="student"
    age = 24
    def getinfo(self):                               #3rd   self is manadatory , we create a self function in the class it is a part of this class
            print(f"hanumant is learning his age is {self.age} & he is a {self.world} .")
   
   
    @staticmethod
    def greet():      #by using static method we dont need the object to call it which is in 3rd case it doent need object
          print(f"good morning mr hunny")

negi=myself()     #object creation  negi     #memory allocated when object is created
print(negi.name,negi.age)  


singh=myself()              #can make another object for same class
singh.name="what tha"                 #   can create a name and access it by using the object
print(singh.name, singh.world)                  #here the name is object instance attribute while the name is class is that class attribute
                                             #instance attribute take preferece over class attribute during assignment and retrivel.

negi.getinfo()          #calling the getinfo function of class
myself.getinfo(negi)    #also can call using this

negi.greet()   #by using static method without calling the 
