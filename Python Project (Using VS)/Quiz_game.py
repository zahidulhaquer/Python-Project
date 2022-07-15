print("Welcome to our quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes": 
    quit()

print("Alright! Let's play!! ")
score = 0

answer = input("what does GP stand for? ")
if answer.lower() == "grameenphone":
    print("You're correct!!") 
    score += 1
else: print("Incorrect!!")

answer = input("what does CS stand for? ").lower()
if answer == "computerscience":
    print("You're correct!!") 
    score += 1
else: print("Incorrect!!")

answer = input("what does BD stand for? ").upper()
if answer == "BANGLADESH":
    print("You're correct!!") 
    score += 1
else: print("Incorrect!!")

print("You got " + str(score) + " Question correct!" )
print("You got " + str((score/3) * 100) + "%" )