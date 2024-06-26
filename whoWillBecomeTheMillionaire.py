import random

name=input("Enter your Name ")
print("\t\t\t","\t*CLAPPING*"*5)
print("\nWelcome ",name," to \"Who Will Become The Millionaire\"\n")
print("INSTRUCTIONS\n* There are 5 random questions\n* Answer should be entered in the form of option\n* Each correct answer will give you 10 Million\n* Each wrong answer will deduce 5 million\n\n\tSO LETS BEGIN")

q=[ "How many sides does an octagon have?",
    "From what country does the chihuahua dog originate?",
    "Who is the Roman goddess of love?",
    "Which side of the brain is responsible for logic and rational thought?",
    "Nyctophobia, Scotophobia, Lygophobia as well as Achluophobia are all the fear of what?",
    "What does the acronym RPM stand for?",
    "What is glass mainly made up of?",
    "Who developed the world's first vaccine?",
    "What is the capital of India?",
    "A cube is cut into two equal halves. How many sides does each cube have?"  ]
a=[     [8,6,12,10],
        ["Mexico","India","Australia","Canada"],
        ["Venus","Mars","Minerva","Juno"],
        ["left","right","Both left and right","none"],
        ["darkness or night","bacteria","balloon","height or weight"],
        ["Revolutions per minute","Rotations per minute","Reaction power measure","Road Permission Measure"],
        ["Sand","air","plant","water"],
        ["Edward Jenner","Charles Darwin","Carl Linnaeus","Rosalind Franklin"],
        ["Delhi","Bangalore","Kerala","Mumbai"],
        ["5 or 6","1 or 4",12,6]    ]
prizeMoney=0
def count(a):
    global prizeMoney
    if (a==10):
        prizeMoney+=10
    elif(prizeMoney==0):
        prizeMoney=0
    else:
        prizeMoney-=5

def check(question,option):
    userAnswer=int(input("Enter the answer: "))
    print()
    if (a[question][option[userAnswer-1]]==a[question][0] ):
        print("Correct Answer!")
        count(10)
    else:
        print("Wrong Answer! Correct answer is ",a[question][0])
        count(5)
    print("Current Balance=",prizeMoney,"Million","\n")
questionIndices=list(range(len(q)))
random.shuffle(questionIndices)
for i in range(5):
    print("Question no. ",i+1)
    question=questionIndices[i]
    option=random.sample(range(0,4),4)
    # random.sample(range(0,4),4) generates a list of 4 unique random numbers between 0 and 3.
    # random.sample(range(0,4),4)[i] selects the ith element from this random list.
    print(q[question])
    for j in range(4):
        print(j+1,") ",a[question][option[j]])
    check(question,option)
print("\t\t\t","\t*CLAPPING*"*5,"\n")
print("Congratulations You Have Won",prizeMoney,"Million")