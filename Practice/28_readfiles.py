f=open('myfile.txt', "r")
data=f.read()
print(data)
f.close()

print(" without writing close we can open and close a file using with")

with open("myfile.txt") as f:
        print(f.read())

        npm install -D tailwindcss