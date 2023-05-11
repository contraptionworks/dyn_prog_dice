import numpy as np

print("            0     1     2     3")
def add_base_die(input):
    input_array = np.array(input)
    # print("Input Array: ", input_array)
    # Dice results 1-4: Create temp_array and make it four times the input
    temp_array = np.array(input_array) * 4
    # print("Temp Array after adding Fours: ", temp_array)
    # Dice result 5: Turn input misses into weak hits, keep input weak hits
    temp_array[1] = temp_array[1] + input_array[0] + input_array[1]
    # print("Temp Array after adding weak hits from Fives: ", temp_array)
    # 5 cont: Keep input strong and crit hits unchanged
    temp_array[2:4] = temp_array[2:4] + input_array[2:4]
    # print("Temp Array after adding strong and crits from Fives: ", temp_array)
    # Dice Result 6: Turn input misses and weak hits into to strong hits
    temp_array[2] = temp_array[2] + input_array[0] + input_array[1]
    # print("Temp Array after adding strong hits from input Sixes: ", temp_array)
    # 6 cont: Turn input strong hits into crits, keep input crit hits
    temp_array[3] = temp_array[3] + input_array[2] + input_array[3]
    # print("Temp Array after adding critical hits from input Sixes: ", temp_array)
    return temp_array

def main_loop(number_of_dice):
    if number_of_dice < 1:
        print("Error: Use between 1 and 20 dice")
    elif (number_of_dice > 20):
        print("Error: Use between 1 and 20 dice")
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
    # return iterative_array
    # print("Iterative Array: ", iterative_array)
    percentages_array = np.round(
        np.copy(iterative_array) / 6**number_of_dice * 100, 2
        )
    # print(percentages_array)
    print(number_of_dice, "Dice: ", percentages_array)

main_loop(7)
