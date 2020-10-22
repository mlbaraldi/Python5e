import random
def rolld(d=20, r=1):
    critical_hit = False
    rolls = []
    for times in range(r):
        roll = random.randint(1,d)
        print("d"+ str(d), "-", "roll :", roll)
        if d == 20 and roll == 20:
            critical_hit = True
            print("-------------------")
            print("Its a critical hit!")
            print("-------------------")
        rolls.append(roll)
    return rolls

def to_hit(Atk, CA):
    rolled = rolld()
    print("Your attack of", str(Atk), "+", str(rolled[0]), "from the roll =", str(rolled[0]+Atk))
    print("The monster CA is", CA)    
    if rolled[0] + Atk >= CA:
        print("Thats a hit!")
    else:
        print("Thats not a hit ):")

def to_damage(weapon, r):
    sum_damage = 0
    for times in range(r):
        roll = rolld(weapon)
        sum_damage += roll[0]
    print("your damage was", sum_damage)
    return sum_damage

