#This litrally took over 5 trys of recoding...

import random
listOwords5 = ["frogs","lakes","field","board","ponds","ocean","cubes",
               "chair","books","audio","truck","shoot","lemon","pines","mouse",
               "fizzy","pizza","cobra","fused","hazel","hertz","joyed","jumps",
               "mixup"]
wordNum = random.randint(0,((len(listOwords5)-1)))
print (listOwords5[wordNum])
Word = (listOwords5[wordNum])

#rules
print("Hangman")
print("=================")
print("Rules ---")
print("No capitals")
print("one letter at a time")
print("all words are 5 letters")
print("GLHF=======================")

#Code acually starts here~
numOguess = 0
G1=Word[0]
G2=Word[1]
G3=Word[2]
G4=Word[3]
G5=Word[4]NumOguess = 0
G = "Guess"
CorrectAmm = 0
Check = 0
List = [G1,G2,G3,G4,G5]
PList = ["_","_","_","_","_"]

while NumOguess < 10 and CorrectAmm < 5:
    G = (input("Guess:   "))
    NumOguess +=1
    for i in range(5):
        if G == List[i]:
            if PList[i] == "_":
                #
                PList[i]= List[i]
                print("Correct          V")
                CorrectAmm += 1
                Check = 1
            else:
                print("already guessed")
    if Check == 0:
        print("Failed        X")
    else:
        Check = 0
    print(PList)
    
#results

if CorrectAmm >= 5:
    print("Compleated puzzle")
    print("--------------------------------")
    print("--------------------------------")
    print("--------------------------------")

else:
    
    print("Failed-------------------------")
    print("--------------------------------")
    print("--------------------------------")
    print("--------------------------------")
