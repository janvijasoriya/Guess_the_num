print("Welcome people!!")

playing=input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play : ")
score=0

ans= input("What does CPU stand for? ")

if ans.lower() =="Central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect")

ans= input("what does GPU stand for? ")

if ans.lower() =="Graphics processing unit":
    print("Correct!")
    score +=1

else:
    print("Incorrect")

ans= input("What does Ram stand for? ")

if ans.lower() =="Random access memory":
    print("Correct!")
    score +=1

else:
    print("Incorrect")


print("you got "+ str(score)+ " questions right")
print("you got "+ str((score/4)*100)+ "%.")

