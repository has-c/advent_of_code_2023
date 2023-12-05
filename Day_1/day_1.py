import re

def process_line(line):
    num_dict = {"zero": "0","one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
            "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    
    # Pass to find first digit
    digits = [digit for digit in line if digit.isdigit()]
    first_num = digits[0]
    last_num = digits[-1]
    first_digit_idx = line.index(first_num)
    last_digit_idx = line.rindex(last_num)

    # Pass to find first word
    first_words = []
    first_words_num = []
    first_words_idx = []
    last_words = []
    last_words_num = []
    last_words_idx = []
    for num in num_dict.keys():
        try:
            idx = line.index(num)
            r_idx = line.rindex(num)
            if idx == r_idx:
                # Match has been made and only single
                first_words.append(num)
                first_words_num.append(num_dict[num])
                first_words_idx.append(idx)
                last_words.append(num)
                last_words_num.append(num_dict[num])
                last_words_idx.append(idx)

            else:
                # Match has been made and there are two
                first_words.append(num)
                first_words_num.append(num_dict[num])
                first_words_idx.append(idx)
                last_words.append(num)
                last_words_num.append(num_dict[num])
                last_words_idx.append(r_idx)
        except:
            pass
    
    try:
        first_word = first_words[first_words_idx.index(min(first_words_idx))]
        last_word = last_words[last_words_idx.index(max(last_words_idx))]
        first_word_idx = line.index(first_word)
        last_word_idx = line.rindex(last_word)
        first_word_num = first_words_num[first_words_idx.index(min(first_words_idx))]
        last_word_num = last_words_num[last_words_idx.index(max(last_words_idx))]
    except ValueError:
        # No words
        first_word_idx = 1e10
        last_word_idx = -1
            
    if first_word_idx < first_digit_idx:
        first_digit = first_word_num
    else:
        first_digit = first_num
    
    if last_word_idx > last_digit_idx:
        last_digit = last_word_num
    else:
        last_digit = last_num

    number = str(first_digit) + str(last_digit)    

    return number

def get_calibration_number_from_string(calibration_num):

    numbers = "".join(re.findall(r'\d+', calibration_num))

    if len(numbers) > 1:
        # The first and last digits are the first and last characters of the string
        first_digit = numbers[0]
        last_digit = numbers[-1]
    
    elif len(numbers) == 1:
        # Last and first number are the same 
        first_digit = numbers[0]
        last_digit = numbers[0]

    else:
        first_digit = 0
        last_digit = 0

    # return 2 digit number
    number = int(str(first_digit) + str(last_digit))

    return number

if __name__ == "__main__":

    puzzle_input_path = r"C:\Users\hcheena\OneDrive - Quantium\Documents\Repos Copy\adhoc_scripts\advent_of_code_2023\Day_1\day_1_puzzle.txt"
    
    # Day 1 Part 1
    calibration_numbers = []
    with open(puzzle_input_path, 'r') as file:
        # Read each line
        for line in file:
            calibration_numbers.append(get_calibration_number_from_string(line.strip()))
            print(get_calibration_number_from_string(line.strip()), line)
    print("Calibration Total ", sum(calibration_numbers))

    # Day 1 Part 2
    calibration_numbers = []
    with open(puzzle_input_path, 'r') as file:
        # Read each line
        for line in file:
            converted_number = process_line(line.strip())
            calibration_numbers.append(get_calibration_number_from_string(converted_number))
            print(line, calibration_numbers[-1])
    print("Calibration Total ", sum(calibration_numbers))