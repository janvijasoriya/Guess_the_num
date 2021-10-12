import random
t_range=input("type a num: ")
if t_range.isdigit():
    t_range=int(t_range)

    if t_range<=0:
        print("please typr num larger than 0 next time.")
        quit()

else:
    print("Please type a number next time.")
    quit()

r= random.randint(0,t_range)
guesses=0

while True:
    guesses+=1
    guess=input("Make a guess: ")

    if guess.isdigit():
        guess=int(guess)

    else:
        print("Please type a number next time.")
        continue

    if guess==r:
        print("you got it!!")
        break
  
    elif guess>r:
            print("you were above the num!")
    else:
            print("you were blow the num")
        
print(" you got it in", guesses, "guesses")   

