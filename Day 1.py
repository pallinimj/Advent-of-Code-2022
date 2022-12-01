# Calorie Counts by Elf
elf_cals = {'Elf_1':[1000,2000,3000],
            'Elf_2':[4000],
            'Elf_3':[5000,6000],
            'Elf_4':[7000,8000,9000],
            'Elf_5':[10000]}

def elf_calories(carried):
    # Use dict of elves and calories as input

    # Get total calories carried by each elf
    total_cals = []
    elf_names = []

    for k, v in elf_cals.items():
        total_cals.append(sum(v))
        elf_names.append(k) 
    
    # Solve for which elf is carrying the most and how much
    max_cals = 0
    max_cal_elf = ''

    max_cals = max(total_cals)
    for i in range(len(elf_names)):
        if total_cals[i] == max_cals:
            print('The Elf carrying the most calories is ' + elf_names[i])
    print('Calories:',+ max_cals)

elf_calories(elf_cals)