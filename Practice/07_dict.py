z={}   #empety dictionary

marks={
     "hanu":99,
     "Hunny":33,
     "honey":50,
     "negi":98,
     619:"yayaya"
  #syntax for making a dicitionay
}

print(marks,type(marks))

print(marks["Hunny"])   #if we write ruchi3 it will give error
print(marks.get("Hunny"))  #if wewrite ruchi3 it will give none

#methods of dict
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Hunny":69,"jyoti":79})
marks.update({"Honey":69,"usha":79})
print(marks)


s=marks.pop("negi")
print(s)
print(marks)

#prob

words={
    "hello": "namaste",
    "annyo": "yes",
    "de":"no"
}
word=input("Enter your word to serch its meaning : ")
print(words[word])
print(words["d"])