"""
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover.
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?"""


def get_words(string):
    pos1 = 10000
    pos2 = -1
    word1 = -1
    word2 = -1
    substrings = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                  'nine': 9}
    for substring in substrings:
        # find first occurrence
        first = string.find(substring)
        # find last occurrence
        last = string.rfind(substring)
        # check if most left value was found
        if first != -1:
            if pos1 >= first:
                pos1 = first
                word1 = substrings[substring]
        # check if most right value was found
        if last != -1:
            if pos2 < last:
                pos2 = last
                word2 = substrings[substring]
        if word2 == -1 and pos1 != 10000:
            word2 = word1
            pos2 = pos1



    return pos1, word1, pos2, word2


def get_digits(string):
    f_digit = -1
    second_digit = -1
    first_position = 10000
    second_position = -1
    for x in range(len(string)):
        if string[x].isdigit():
            if f_digit == -1:
                f_digit = int(string[x])
                first_position = x
            else:
                second_digit = int(string[x])
                second_position = x
    if second_digit == -1 and first_position != 10000:
        second_digit = f_digit
        second_position = first_position

    return first_position, f_digit, second_position, second_digit


file = open('input.txt', 'r')

input_file = file.readlines()

calibration_values = []
for value in input_file:
    first_digit = -1
    second_digit = -1
    first_word_position, first_word_value, second_word_position, second_word_value = get_words(value)
    first_digit_position, first_digit_value, second_digit_position, second_digit_value = get_digits(value)
    if first_word_position > first_digit_position:
        first_digit = first_digit_value
    else:
        first_digit = first_word_value

    if second_digit_position > second_word_position:
        second_digit = second_digit_value
    else:
        second_digit = second_word_value


print((sum(calibration_values)))
