'''This program prints the fibonacci sequence till the desired number using Recursive function'''
''' example: 0,1,1,2,3,5,8,13,....'''

def fibonacci(n):
    if (n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2) #Recursive function

n=int(input("Enter the number of terms: "))
for i in range(n):
    print(fibonacci(i),end=" ")