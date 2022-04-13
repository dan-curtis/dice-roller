import random
import re


########################## PART 1 ##########################



def _roll_dice(m:int, n:int)->list:
    ''' 
    m = multiplier, aka number of dice
    n = max number of pips on die
    output list of individual outcomes
    '''
    results = []
    for _ in range(m):
        results.append(random.randint(1,n))
    return results


def main_roll_dice(dice_str):
    ''' 
    dice_str: string of form "mDn+c" 
    i.e. "3D6+2" for 3 x 6-sided die rolls and add 2 to the score
    the D is not case sensitive
    '''

    dice_str = re.sub("-", "+-", dice_str)
    dice_str = dice_str.lower()

    list_dice_str = dice_str.split('+')
    if len(list_dice_str) == 2:
        c = int(list_dice_str[1])
    elif len(list_dice_str) == 1:
        c = 0
    else:
        return 'error: too many additions, max = 1'

    dice_str = list_dice_str[0]

    list_dice_str = dice_str.split('d')
    if len(list_dice_str) > 2:
        return 'error: too many dice, max = 1'
    if list_dice_str[0] == '':
        m = 1
    else:
        m = int(list_dice_str[0])
    n = int(list_dice_str[1])

    print(f'rolling {m} * d{n}{" + " + str(c) if c else ""}')
    dice_results = _roll_dice(m,n)
    total = sum(dice_results) + c

    print(f'result: {", ".join([str(result) for result in dice_results])}')
    print(f'total: {total}')

    return total

############################################################

########################## PART 2 ##########################
############################################################

########################## PART 3 ##########################
############################################################

########################## PART 4 ##########################
############################################################













def tidy_instruction(instruction:str)->list:
    '''
    
    '''
    # replace spaces between ints with pipes
    instruction = re.sub(r"(?<=\d)\s+(?=\d)", "|", instruction)
    # replace space before a dD with pipes
    instruction = re.sub(r"(?<=\d)\s+(?=[dD])", "|", instruction)
    # remove remaining space
    instruction = re.sub(r"\s+", "", instruction)
    # add +s to subtractions
    instruction = re.sub("-", "+-", instruction)

    #TODO: handle addition of roll outputs, use dictionaries?


    list_instruction = instruction.split('|')
    # split sub-rolls into m and n/c
    for ix,value in enumerate(list_instruction):
        sub_list = value.lower().split('d')
        if sub_list[0] == '':
            sub_list[0] = '1'
        list_instruction[ix] = sub_list
    for ix,value in enumerate(list_instruction):
        sub_list = value[1].split('+')
        list_instruction[ix][1] = sub_list[0]
        list_instruction[ix].append('0')
        if len(sub_list) > 1:
            list_instruction[ix][2] = sub_list[1]

    list_instruction = [[int(x) for x in sub_list] for sub_list in list_instruction]
    list_instruction
    return list_instruction

def evaluate_results(instruction:str)->list:
    list_instruction = tidy_instruction(instruction)
    list_result = []
    for i in list_instruction:
        list_result.append(sum(roll_dice(i[0],i[1]))+i[2])
    return list_result



def main_roll_dice(dice_str, verbose=False):
    instr = dice_str.lower().split('d')
    m = int(instr[0])
    n = int(instr[1])

    if verbose:
        print(f'rolling {m} * d{n}')

    results = roll_dice(m,n)

    if verbose:
        print(f'result: {", ".join([str(result) for result in results])}')
        print(f'total: {sum(results)}')

    return sum(results)


main_roll_dice('3D6')

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