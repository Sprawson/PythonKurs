"""The missing part wasn't the only issue - one of the gears in the engine is wrong.
A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

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
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?"""

import re


def number_in_range(m, n):
    number_range = range(n.start() - 1, n.end() + 1)
    if n.start() - 1 == m.start() or n.end() == m.start():
        return True
    elif m.start() in number_range:
        return True
    else:
        return False


f = open("input.txt", 'r')
file_lines = f.readlines()
# Add dots on all sides and remove \n at the end of lines
lines = ['.' * (len(file_lines) + 2)]
for line in file_lines:
    buf = '.' + line.strip() + '.'
    lines.append(buf)
lines.append('.' * (len(file_lines) + 2))

gear_ratios = []
for x in range(len(lines)):
    number_find = re.compile("\d+")
    gear_find = re.compile("\*")
    gears = gear_find.finditer(lines[x])
    for match in gears:
        numbers_near = []
        adjecent_part_numbers = []
        # find numbers in line above *
        numbers_above = number_find.finditer(lines[x - 1])
        # find numbers next to *
        numbers_next_to = number_find.finditer(lines[x])
        # find numbers in line below
        numbers_below = number_find.finditer(lines[x + 1])

        for group in numbers_below, numbers_next_to, numbers_above:
            for number in group:
                if number_in_range(match, number):
                    adjecent_part_numbers.append(int(number.group()))

        if len(adjecent_part_numbers) == 2:
            gear_ratios.append(adjecent_part_numbers[0] * adjecent_part_numbers[1])

print(sum(gear_ratios))
