def add_die(type, input):
    input_array = np.array(input)
    if type == "base":
	    # Base dice results 1-4: Create temp_array equal to the input array multiplied by four.
        # Because adding a die with result 1-4 doesn't change any input results,
            # and there are four ways that can happen.
         temp_array = np.array(input_array) * 4
	elif type == "push":
	    # Push dice results 2-4: Create temp_array equal to the input array multiplied by three.
        # Because adding a push die with result 2-4 doesn't change any input results,
            # and there are three ways that can happen.
        temp_array = np.array(input_array) * 3
		    # Push dice result 1: Any input results remain plus a setback
        temp_array[0:4, 1] = temp_array[0:4, 1] + input_array[0:4, 1]
	    temp_array[0:4, 2] = temp_array[0:4, 2] + input_array[0:4, 2]
	else: print("Error: invalid die type.")
    # Dice result 5: Any misses input become weak hits, and keep any weak hits input
    temp_array[1, 0:3] = temp_array[1, 0:3] + input_array[0, 0:3] + input_array[1, 0:3]
    # Continue result 5: Keep strong hits and crit hits input unchanged
    temp_array[2:4, 0:3] = temp_array[2:4, 0:3] + input_array[2:4, 0:3]
    # Dice Result 6: Any misses and weak hits input become strong hits
    temp_array[2, 0:3] = temp_array[2, 0:3] + input_array[0, 0:3] + input_array[1, 0:3]
    # Continue result 6: Any strong hits input become crits, and keep any crits input
    temp_array[3, 0:3] = temp_array[3, 0:3] + input_array[2, 0:3] + input_array[3, 0:3]
    return temp_array
	
def main_loop(base_dice, push_dice):
    if base_dice not in range(1, 6):
        print("Error: Use between 1 and 5 base dice")
	if push_dice not in range(0, 3):
        print("Error: Use between 0 and 2 push dice")
    else:
        base_iteration = 1
		push_iteration = 0
        # This starting array is the possible results from 1 base and 0 push dice
        # Four misses (1-4), one weak hit (5), one strong hit (6), no crits (2 or more 6s)
		# And no setbacks, which only occur on a 1 on a push die
        base_iterative_array = np.array([4, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0])
		globals()[f"b{base_iteration}_p{push_iteration}"]
            = np.round(base_iterative_array / 6**(base_iteration + push_iteration) * 100, 2)
		print("Base: ", base_iteration, ", Push: ", push_iteration,
		    f"b{base_iteration}_p{push_iteration}", "-- "
			)
        while base_iteration < base_dice or push_iteration < push_dice
			push_iterative_array = base_iterative_array
		    while push_iteration < push_dice:
                push_iteration = push_iteration + 1
			    # Function call to add results of one additional base die to the combinations
                push_iterative_array = add_die("push", push_iterative_array)
				globals()[f"b{base_iteration}_p{push_iteration}"]
                    = np.round(push_iterative_array / 6**(base_iteration + push_iteration) * 100, 2)
		        print("Base: ", base_iteration, ", Push: ", push_iteration,
			        f"b{base_iteration}_p{push_iteration}", "-- "
			        )
			if base_iteration < base_dice:
                base_iteration = base_iteration + 1
            	push_iteration = 0
                # Function call to add results of one additional base die to the combinations
                base_iterative_array = add_base_die("base", base_iterative_array)
		        globals()[f"b{base_iteration}_p{push_iteration}"]
                    = np.round(base_iterative_array / 6**(base_iteration + push_iteration) * 100, 2)
		        print("Base: ", base_iteration, ", Push: ", push_iteration,
			        f"b{base_iteration}_p{push_iteration}", "-- "
			        )

main_loop(5, 2)
