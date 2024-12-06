marks=int(input("Enter your marks for checking your grade : ") )

if(marks>=90 and marks<=100):
    print("You get Grade 'EX' .")
elif(marks>=80 and marks<=90):
    print("You get Grade 'A' .")
elif(marks>=70 and marks<=80):
    print("You get Grade 'B' .")
elif(marks>=60 and marks<=70):
    print("You get Grade 'C' .")
elif(marks>=50 and marks<=60):
    print("You get Grade 'D' .")
elif(marks>=40 and marks<=50):
    print("You get Grade 'F' .")
else:
    print("You dumb , you are failed .")