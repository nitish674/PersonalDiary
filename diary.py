from typing import Text


print("Welcome To Diary, Saatvik!")
print("What you want to do ")
print("1. Read")
print("2. Write")
option = int(input())
if (option==1):    
    f = open("diary.txt")
    text = f.read()
    print(text)
    f.close
elif (option==2):
    day = input("Enter Today Day : ")
    date = input("Enter Today Date : ")
    salutation = "Dear diary,"
    content = input("""Dear Diary,
    """)
    footer = "Thank you, Bye Bye"
    newline = print()
    f = open("diary.txt","a")
    f.write(day)
    f.write("\n")
    f.write(date)
    f.write("\n")
    f.write(salutation)
    f.write("\n")
    f.write(content)
    f.write("\n")
    f.write(footer)
    f.write("\n")
    f.write("\n")
    f.close()