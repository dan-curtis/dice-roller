import random
import re

def _roll_dice(m:int, n:int)->list:
    ''' m = multiplier, aka number of dice
        n = max number of pips on die
        output list of individual outcomes'''
    results = []
    for _ in range(m):
        results.append(random.randint(1,n))
    return results

def roll_dice(dice_str, verbose=False):
    instr = dice_str.lower().split('d')
    m = int(instr[0])
    n = int(instr[1])

    if verbose:
        print(f'rolling {m} * d{n}')

    results = _roll_dice(m,n)

    if verbose:
        print(f'result: {", ".join([str(result) for result in results])}')
        print(f'total: {sum(results)}')

    return sum(results)


roll_dice('3D6')

eval("roll_dice('4d10')")

test = '3D6+ 4 2d7 -2 d8'

# replace space between two digits with a pipe
line = re.sub(r"(?<=\d)\s+(?=\d)", "|", test)
line
# replace space between two digits followerd by Dd with a pipe
line = re.sub(r"(?<=\d)\s+(?=[dD])", "|", line)
line
# remove remaining whitespace
line = re.sub(r"\s+", "", line)
line
# add plus signs to minuses
line = re.sub("-", "+-", line)
line
# split into sub-rolls
test_list = line.split('|')
# split sub-rolls into m and n/c
for ix,value in enumerate(test_list):
    sub_list = value.lower().split('d')
    if sub_list[0] == '':
        sub_list[0] = '1'
    test_list[ix] = sub_list
for ix,value in enumerate(test_list):
    sub_list = value[1].split('+')
    if len(sub_list) > 1:
        test_list[ix][1] = sub_list[0]
        test_list[ix].append(sub_list[1])

test_list = [[int(x) for x in sub_list] for sub_list in test_list]
test_list


# wrap multiple dice calls with a regex capture group to keep the variables