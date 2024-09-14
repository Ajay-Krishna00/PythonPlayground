#  Aim:
#  To Implement a Blog interface in Python, having the following compulsory features:
#   - Creating a Blog Post
#   - Deleting a Blog Post
#   - Modifying an existing Blog Post
#  This includes User Authentication, which means multiple users can register or log in and
#  each user can create their own blog . 
#   - Passwords must be encrypted and stored, so that users can login again.


import bcrypt
import sys

userDB={}

def login():
  currentUsername=input("Enter The Username: ")
  currentPassword=input("Enter The Password: ").encode('utf-8')
  if currentUsername in userDB and bcrypt.checkpw(currentPassword,userDB[currentUsername]["password"]):
    accessGranted(currentUsername)
  else:
    print("Wrong Credentials!\n")

def createAccount():
  username=input("Enter The Username: ")
  password=input("Enter The Password: ").encode('utf-8')
  hashedP=bcrypt.hashpw(password, bcrypt.gensalt())      # Hashing the password
  userDB[username] = {
        "password": hashedP,  # Stores the hashed password here
        "blogs": {}           # Initializing an empty blog collection 
    }
  print("Account created successfully. Please login.\n")
  login()

def displayBlog(currentUsername):
  print("Your Blogs are: ")
  length=len(userDB[currentUsername]["blogs"])
  if length!=0:
    for i in range(1,length+1):
      print(f"{i}. ",userDB[currentUsername]["blogs"][i])
  else:
    print("You have written no Blogs!\n")

def writeBlog(currentUsername):
  num=len(userDB[currentUsername]["blogs"]) + 1
  print("Write the contents of the blog\n")
  content=input()
  userDB[currentUsername]["blogs"][num]=content
  print("Blog added successfully!\n")

def editBlog(currentUsername):
  print("Enter the blog number you want to Edit")
  num=int(input())
  if num in userDB[currentUsername]["blogs"]:
    print("Enter the new content of the blog")
    content=input()
    userDB[currentUsername]["blogs"][num]=content
    print("Blog Edited successfully!\n")
  else:
    print("Invalid Blog Number\n")

def deleteBlog(currentUsername):
  print("Enter the blog number you want to delete")
  num=int(input())
  if num in userDB[currentUsername]["blogs"]:
    userDB[currentUsername]["blogs"].pop(num)
    # userDB[currentUsername]["blogs"].remove(num)

    #Now we need to update the blog numbers since we have deleted a blog
    for i in range(num+1,len(userDB[currentUsername]["blogs"])+2):
      userDB[currentUsername]["blogs"][i-1]=userDB[currentUsername]["blogs"][i]
      userDB[currentUsername]["blogs"].pop(i)

    print("Blog deleted successfully!")
  else:
    print("Invalid Blog Number")

def accessGranted(currentUsername):
  print(f"\nWelcome {currentUsername}, What do you want to do today?\n")
  while (True):
    inp=int(input("Enter 1 to display blog\n\t 2 to write blog\n\t 3 to Edit blog\n\t 4 to Delete blog\n\t 5 to exit\n"))
    match inp:
      case 1: displayBlog(currentUsername)
      case 2: writeBlog(currentUsername)
      case 3: editBlog(currentUsername)
      case 4: deleteBlog(currentUsername)
      case 5: 
        print("Thank you for using Ajay's Blog service!")
        print("Goodbye!")
        return
      case _: print("Invalid choice")

print("Welcome!")
inp=int(input("Enter 1 for Login and 2 for Creating Account: "))
try:
  if inp==1:
    login()
  elif inp==2:
    createAccount()
  else:
    print("Enter 1 or 2")
except ValueError:
  print("Invalid Input")
  sys.exit()
