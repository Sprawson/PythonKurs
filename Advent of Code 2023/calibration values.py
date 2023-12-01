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
    calibration_values.append(first_digit*10 +second_digit)

print(calibration_values)
print(sum(calibration_values))


