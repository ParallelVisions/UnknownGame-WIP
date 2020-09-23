import random

game_over = False
ChanceToHit = str(range(0, 100))
health = 100
damage = [20, 40, 10]

for damage in list(damage):
        health -= damage       

while not health == 0:

    if health >= 0:
        print("You still have", health, "health.")
        game_over = False
        break

    elif health == -20:
        print("You died!")
        game_over = True
        break
    if game_over == True:
        print("Game over. Try again?")



