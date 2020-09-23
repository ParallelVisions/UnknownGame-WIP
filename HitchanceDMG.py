import random

ChanceToHit = list(range(0, 101))

if ChanceToHit >= list(range(95-101)):
    print("Critical hit!")
elif ChanceToHit >= list(range(50-94)):
    print("You hit!")
elif ChanceToHit <= list(range(0-49)):
    print("You miss!")

    



print(random.choice(ChanceToHit))