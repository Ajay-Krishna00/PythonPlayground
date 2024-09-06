#Hashing passwords with Python and Bcrypt

import bcrypt

password =(input("Enter your password: "))

# Convert the password to bytes
Passwd = password.encode('utf-8')

hashed= bcrypt.hashpw(Passwd, bcrypt.gensalt())

conform =(input("Conform your password: "))

if (bcrypt.checkpw(conform.encode('utf-8'),hashed)):
  print("Password Matched")
else:
  print("Password not matched")