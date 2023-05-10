import numpy as np

def add_base_die(input_array):
    # Dice results 1-4: Create temp_array and populate it with four times unchanged input
    temp_array = np.array(input_array) * 4
    # Dice result 5: Turn input misses into weak hits and keep input weak hits
    temp_array[1] = temp_array[1] + input_array[0] + input_array[1]
    # 5 cont: Keep input strong and crit hits unchanged
  	# Could I do it this way instead? temp_array[2:4] = temp_array[2:4] + input_array[2:4]
    temp_array[2] = temp_array[2] + input_array[2]
  	temp_array[3] = temp_array[3] + input_array[3]
    # Dice Result 6: Turn input misses and weak hits into to strong hits
    temp_array[2]) = temp_array[2] + input_array[0] + input_array[1]
    # 6 cont: Turn input strong hits into crit hits and keep input crit hits
    temp_array[3] = temp_array[3] + input_array[2] + input_array[3]
    return temp_array

def main_loop(number_of_dice):
    if number_of_dice < 1:
	    return "Error: Use between 1 and 20 dice"
	elseif number_of_dice > 20:
	    return "Error: Use between 1 and 20 dice"
    else:
        iteration = 1
	    iterative_array = np.array([4, 1, 1, 0])
        while iteration < number_of_dice
	        iterative_array = add_base_die(iterative_array)
            iteration = iteration + 1
        return iterative_array

