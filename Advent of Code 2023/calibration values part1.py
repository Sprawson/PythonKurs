"""
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?"""


file = open('input.txt','r')

input  = file.readlines()

print(input)
calibration_values = []
for value in input:
    first_digit = None
    second_digit = None
    for char in value:
        if char.isdigit():
            if first_digit == None:
                first_digit = int(char)
            else:
                second_digit = int(char)
    if second_digit == None:
        second_digit = first_digit
    calibration_values.append(first_digit*10 + second_digit)

print(calibration_values)
print(sum(calibration_values))


