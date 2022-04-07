import random

dice_roll = random.randint(1,6)
print(dice_roll)

def roll_dice(dice_str):
    instr = dice_str.lower().split('d')
    m = int(instr[0])
    n = int(instr[1])
    print(f'rolling {m} * d{n}')

    rolls = []
    for i in range(0,m):
        rolls.append(random.randint(1,n))
    print(f'result: {", ".join([str(roll) for roll in rolls])}')
    print(f'total: {sum(rolls)}')

roll_dice('3D6')

eval("roll_dice('4d10')")

# wrap multiple dice calls with a regex capture group to keep the variables