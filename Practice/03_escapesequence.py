
who=input("enter your friend name  :  ")
print(f"hello , how are yoy my dear friend, {who}")    #f strings is used to put varisable inside print


letter='''Dear |name|,
           you are the winter soul
              its |date| and you still lokks beautifull as
              always'''
print(letter.replace("|name|","Ruchi ").replace("|date|","27-november-2025"))
#2nd .replace chnge the previus changed string its a chaining of .replace