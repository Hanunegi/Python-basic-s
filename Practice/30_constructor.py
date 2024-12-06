class myself:                  
    name="Hanumant"
    world="student"
    age = 24
    def getinfo(self):                              
            print(f"hanumant is learning his age is {self.age} & he is a {self.world} .")
    
    def __init__(self):    #it is a dunder method which is called automatically   #it is a constructor.
          print("hey fells its hunny here bois")    #as we can see we didnt call this but it automatically called


negi=myself()     
print(negi.name,negi.age)  

singh=myself()              
singh.name="what tha"                 
print(singh.name, singh.world)                 
 
