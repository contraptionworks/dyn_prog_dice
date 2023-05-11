import numpy as np

# Dynamic programming using numpy arrays to calculate probabilities
    # for a simplified version of the Ruffians dice system, with only base dice.
# Players roll a pool of between 1 and 7 six-sided dice.
    # If there are two or more sixes, it's a critical hit.
    # If there is one six, it's a strong hit.
    # If there are no sixes but at least one five, it's a weak hit.
    # If there are no fives or sixes, it's a miss.
# The main_loop starts with an array of possible outcomes from one die
    # and calls the add_base_die function in a loop until it reaches the input number.
# The script operates in raw combinations, so each die added multiples the total by six.
    # Probabilities are only output as percentages.

print("            0     1     2     3")
print("          Miss  Weak  Strong Crit")

def add_base_die(input):
    # Input is an array of results combinations from previous dice rolled.
    # Each result on the added die has various effects on array elements.
    input_array = np.array(input)
    # Dice results 1-4: Create temp_array equal to the input array multiplied by four.
    # Because adding a die with result 1-4 doesn't change any input outcomes,
    # and there are four ways that can happen.
    temp_array = np.array(input_array) * 4
    # Dice result 5: Any input misses become weak hits, and keep any input weak hits
    temp_array[1] = temp_array[1] + input_array[0] + input_array[1]
    # Continue result 5: Keep input strong hits and crit hits unchanged
    temp_array[2:4] = temp_array[2:4] + input_array[2:4]
    # Dice Result 6: Any input misses and weak hits become strong hits
    temp_array[2] = temp_array[2] + input_array[0] + input_array[1]
    # Continue result 6: Any input strong hits become crits, and keep input crits
    temp_array[3] = temp_array[3] + input_array[2] + input_array[3]
    return temp_array

def main_loop(number_of_dice):
    if number_of_dice not in range(1, 11):
        print("Error: Use between 1 and 10 dice")
    else:
        iteration = 1
        # This starting array is the possible results from one die
        # Four misses (1-4), one weak hit (5), one strong hit (6), no crits (2 or more 6s)
        iterative_array = np.array([4, 1, 1, 0])
    while iteration < number_of_dice:
        # Print the probabilities for each number of dice up to n-1
        percentages_array = np.round(
            np.copy(iterative_array) / 6**iteration * 100, 2
            )
        print(iteration, "DICE: ", percentages_array)
        # Function call to add results of one additional base die to the combinations
        iterative_array = add_base_die(iterative_array)
        iteration = iteration + 1
    # Print the probabilities of the full number of dice
    percentages_array = np.round(
        np.copy(iterative_array) / 6**number_of_dice * 100, 2
        )
    print(number_of_dice, "Dice: ", percentages_array)

main_loop(7)
