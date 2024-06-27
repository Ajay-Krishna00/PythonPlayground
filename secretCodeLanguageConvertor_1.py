# This is a python program to translate a message into secret code language.
# Rules below are used to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# '.' represents a space and '#' represents a fullstop
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

import random
list1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ran=random.choices(list1,k=100)
print("WELCOME!")
str1= input("Enter the sentence which you want to convert:\n")
choice=input("Do you want to encode or decode?\n")
i=0
try:
    if choice.lower()=="encode" :
        li=list(str1)
        fs=li.count(".")
        if fs!=0:
            str1=input("Make sure that a space is left before and after the fullstops\nIf space is not left write again\n")
        str0=str1.lower()
        str2=str0.strip()
        str3=str2.split(" ")
        print("The Encoded sentence is as follows:\n")
        while i!=len(str3):
                l=list(str3[i])
                if str3[i]== ".":
                    print("#",end=" . ")    #converting all full stop to '#'
                elif len(str3[i]) == 1:
                    print(str3[i],end=" ")  #printing the words with 1 letter as it is
                    print(".",end=" ")
                elif len(str3[i]) < 3:
                    l.reverse()             #reversing the word if it has 2 letters
                    for item in l:
                            print(item,end=" ")
                    print(".",end=" ")
                elif len(str3[i]) >=3:
                        temp=str3[i][0]
                        l.pop(0)            #removing the first letter
                        l.append(temp)      #appending the first letter 
                        for k in range(0,3):
                            l.append(ran[(random.randint(0,99))])           #just adding some(3) random letters to the word
                            l.insert(0,ran[(random.randint(0,99))])
                        for item in l:
                            print(item,end=" ")
                        print(".",end=" ")
                i += 1
        print("\n")
    elif choice.lower()=="decode" :
            no_spaces = str1.replace(" ", "")       #replacing extra spaces
            # or using list comprehension: no_spaces = "".join([char for char in str1 if char != " "])
#from here onwards just doing everything opposite to what done above to decode this
            sen=no_spaces.replace("."," ")          #replacing . with spaces that we actually need
            sen2=sen.replace("#",".")               #replacing # with fullstops
            word=sen2.split(" ")
            i=0
            print("The Decoded sentence is as follows:\n")
            while i != len(word):
                if len(word[i])==1:
                    print(word[i].title(),end=" ") 
                elif len(word[i])<3:
                    print(word[i][::-1].title(),end=" ")
                elif len(word[i])>=3:
                    try:
                        temp=word[i]
                        w=temp[3:-3]
                        modiW=w[-1]+w[:-1]
                        print(modiW.capitalize(),end=" ")
                    except:
                        print("Also check if correct input is given to the question\'Do you want to code or decode?\'")
                i+=1
except ValueError:
    print("Invalid input")
