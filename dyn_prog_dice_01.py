import numpy as np


print("            0     1     2     3")
print("          Miss  Weak  Strong Crit")
def add_base_die(input):
    input_array = np.array(input)
    # Dice results 1-4: Create temp_array and make it four times the input
    # Adding a die with result 1-4 doesn't change any input outcomes
    temp_array = np.array(input_array) * 4
    # Dice result 5: Any input misses become weak hits, keep input weak hits
    temp_array[1] = temp_array[1] + input_array[0] + input_array[1]
    # Result 5 cont: Keep input strong hist and crit hits unchanged
    temp_array[2:4] = temp_array[2:4] + input_array[2:4]
    # Dice Result 6: Any input misses and weak hits become strong hits
    temp_array[2] = temp_array[2] + input_array[0] + input_array[1]
    #Result 6 cont: Any input strong hits become crits, keep input crit hits
    temp_array[3] = temp_array[3] + input_array[2] + input_array[3]
    return temp_array

def main_loop(number_of_dice):
    if number_of_dice not in range(1, 11):
        print("Error: Use between 1 and 10 dice")
    else:
        iteration = 1
        iterative_array = np.array([4, 1, 1, 0])
    while iteration < number_of_dice:
        percentages_array = np.round(
            np.copy(iterative_array) / 6**iteration * 100, 2
            )
        print(iteration, "Dice: ", percentages_array)
        iterative_array = add_base_die(iterative_array)
        iteration = iteration + 1
    percentages_array = np.round(
        np.copy(iterative_array) / 6**number_of_dice * 100, 2
        )
    print(number_of_dice, "Dice: ", percentages_array)

main_loop(7)
