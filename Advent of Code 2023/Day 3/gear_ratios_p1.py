"""The engine schematic (your puzzle input) consists of a visual representation of the engine.
There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum.
(Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol:
114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?"""

import re

f = open("input.txt", 'r')
file_lines = f.readlines()

lines = []
part_numbers = []
# Add dots on all sides
lines.append('.' * (len(file_lines)+2))
for line in file_lines:
    buf = '.' + line.strip() + '.'
    lines.append(buf)
lines.append('.' * (len(file_lines)+2))

for x in range(len(lines)):
    numbers = re.finditer("\d+", lines[x])
    for match in numbers:
        start_pos = match.span()[0]
        end_pos = match.span()[1]
        number_value = match.group()
        # Check left and right
        if lines[x][start_pos - 1] != '.' or lines[x][end_pos] != '.':
            part_numbers.append(int(number_value))
        else:
            # Check symbols in line above and below
            for y in range(start_pos - 1, end_pos + 1):
                if lines[x - 1][y] != '.' or lines[x + 1][y] != '.':
                    part_numbers.append(int(number_value))

print(sum(part_numbers))