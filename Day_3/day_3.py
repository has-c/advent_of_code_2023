import numpy as np

if __name__ == "__main__":

    puzzle_input_path = r"C:\Users\hcheena\OneDrive - Quantium\Documents\Repos Copy\adhoc_scripts\advent_of_code_2023\Day_3\day_3_puzzle.txt"
    
    # Create gameboard
    engine = list()
    with open(puzzle_input_path, 'r') as file:
        # Read each line
        for line in file:
            line = line.strip()
            # Process game
            chunks, chunk_size = len(line), 1
            engine_row = [line[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
            engine.append(engine_row)

    # Part 1 
    valid_symbol =["+","-","*","/","%","=","&","|","!","^","~","$","@","*","^","#","$"]
    not_part_number = list()
    all_part_numbers = list()
    engine_array = np.array(engine)
    num_rows = engine_array.shape[0]
    num_cols = engine_array.shape[1]
    row_idx = 0
    col_idx = 0
    scan = True # False when we've scanned all rows and cols

    while scan:

        engine_element = engine_array[row_idx,col_idx]
        if engine_element.isdigit():
            
            # Find end of numbers
            result = []
            for element_idx in range(col_idx,num_cols):
                element = engine_array[row_idx,element_idx]
                if not(element.isdigit()):
                    # symbol so break not a number
                    break
                result.append(element)

            # Is a number so check if adjacent to a valid symbol
            if row_idx == 0 and col_idx == 0:
                engine_slice = engine_array[row_idx:row_idx+2,col_idx:element_idx+1]
                is_part_number = any(np.isin(engine_slice.flatten(), valid_symbol))
            elif row_idx == 0 and col_idx != 0:
                engine_slice = engine_array[row_idx:row_idx+2,col_idx-1:element_idx+1]
                is_part_number = any(np.isin(engine_slice.flatten(), valid_symbol))
            elif row_idx != 0 and col_idx == 0:
                engine_slice = engine_array[row_idx:row_idx+2,col_idx:element_idx+1]
                is_part_number = any(np.isin(engine_slice.flatten(), valid_symbol))                
            else:
                #Normal not edge case part detection
                engine_slice = engine_array[row_idx-1:row_idx+2,col_idx-1:element_idx+1]
                is_part_number = any(np.isin(engine_slice.flatten(), valid_symbol))
            
            # Find a complete number
            schematic_number = "".join(result)

            # Add to not part number list
            if not(is_part_number):
                not_part_number.append(int(schematic_number))
            all_part_numbers.append(int(schematic_number))
        
        else:
            # Not a number continue to iterate
            element_idx = col_idx + 1


        # Skip to next slot to scan for new number
        col_idx = element_idx
        row_idx = row_idx 
        if col_idx == (num_cols - 1):
            if row_idx+1 == num_rows:
                # Hit the end
                scan = False
                break
            else:
                # columns iterated next row time
                row_idx += 1
                col_idx = 0

    print(not_part_number)
    print(sum(all_part_numbers) - sum(not_part_number))
            
    # Part 2 - Determine gear ratio
    # Each number is it adjacent to a gear
    # If is it what is the gear location
    # Two gears adjacent to the same gears are then assumed to be part of the same gear ratio

    valid_gear_symbol = ["*"]
    engine_array = np.array(engine)
    num_rows = engine_array.shape[0]
    num_cols = engine_array.shape[1]
    row_idx = 0
    col_idx = 0
    scan = True # False when we've scanned all rows and cols
    gear_ratios = {} # key is location, value are part numbers
    while scan:

        engine_element = engine_array[row_idx,col_idx]
        if engine_element.isdigit():
            
            # Find end of numbers
            result = []
            for element_idx in range(col_idx,num_cols):
                element = engine_array[row_idx,element_idx]
                if not(element.isdigit()):
                    # symbol so break not a number
                    break
                result.append(element)

            # Is a number so check if adjacent to a valid symbol
            if row_idx == 0 and col_idx == 0:
                engine_slice = engine_array[row_idx:row_idx+2,col_idx:element_idx+1]
                is_gear = any(np.isin(engine_slice.flatten(), valid_gear_symbol))
                start_x = row_idx
                start_y = col_idx
            elif row_idx == 0 and col_idx != 0:
                engine_slice = engine_array[row_idx:row_idx+2,col_idx-1:element_idx+1]
                is_gear = any(np.isin(engine_slice.flatten(), valid_gear_symbol))
                start_x = row_idx
                start_y = col_idx-1
            elif row_idx != 0 and col_idx == 0:
                engine_slice = engine_array[row_idx:row_idx+2,col_idx:element_idx+1]
                is_gear = any(np.isin(engine_slice.flatten(), valid_gear_symbol))     
                start_x = row_idx
                start_y = col_idx           
            else:
                #Normal not edge case part detection
                engine_slice = engine_array[row_idx-1:row_idx+2,col_idx-1:element_idx+1]
                is_gear = any(np.isin(engine_slice.flatten(), valid_gear_symbol))
                start_x = row_idx - 1
                start_y = col_idx-1

            # Find a complete number
            schematic_number = "".join(result)

            # Add to not part number list
            if is_gear:
                gear_x,gear_y = np.where(engine_slice == valid_gear_symbol)
                global_gear_x = gear_x + start_x
                global_gear_y = gear_y + start_y
                gear_global = str(global_gear_x) + str(global_gear_y)
                if gear_global in gear_ratios:
                    gear_ratios[gear_global] += [int(schematic_number)]
                else:
                    gear_ratios[gear_global] = [int(schematic_number)]
        
        else:
            # Not a number continue to iterate
            element_idx = col_idx + 1


        # Skip to next slot to scan for new number
        col_idx = element_idx
        row_idx = row_idx 
        if col_idx == (num_cols - 1):
            if row_idx+1 == num_rows:
                # Hit the end
                scan = False
                break
            else:
                # columns iterated next row time
                row_idx += 1
                col_idx = 0
    
    # Gears and product numbers have been allocated
    # Find gear ratio
    gear_ratio_sum = 0
    gear_ratio_product = []
    for gear in gear_ratios:
        if len(gear_ratios[gear]) > 1:
            gear_ratio_sum += np.product(gear_ratios[gear])
            gear_ratio_product.append(gear_ratios[gear])
    print(gear_ratio_sum)