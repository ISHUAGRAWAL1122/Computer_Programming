#3

import random
c=random.randint(1,100)
score=10
while True:
    n=int(input("Guess number between 1 to 100: "))
    if n==c:
        print("You got it right")
        break
    elif c<n:
        print("Too far")
    elif c>n:
        print("Too near")
    score=score-1
print(score)
