import re

f = open("input.txt", 'r')
file_lines = f.readlines()


# for x in range(len(lines)):
#     if x == 0:
#         print()
#     elif x == len(lines):
#         print()
#     else:
#         for y in range(len(lines[x])):
#             if y ==0 :
#                 print()
#             elif y == len(lines[x]):
#                 print()
#             else:
#                 if lines[x][y].isdigit():
#                     if lines[x-1][y-1] != '.' or lines[x-1][y].isalpha() or lines[x-1][y-1] ==

def check_left(line_number, start):
    if lines[line_number][start - 1] != '.':
        return True
    else:
        return False


def check_right(line_number, end):
    if lines[line_number][end] != '.':
        return True
    else:
        return False
def check_below(line_number, position ):
    if lines[line_number + 1][position] != '.':
        return True
    else:
        return False
def check_above(line_number, position ):
    if lines[line_number - 1][position] != '.':
        return True
    else:
        return False

lines = []
part_numbers = []
#delete \n at the end of lines and add additional '.'
lines.append('.' * (len(file_lines)+2))
for line in file_lines:
    buf = '.' + line.strip()+ '.'
    lines.append(buf)
lines.append('.' * (len(file_lines)+2))

# string = '................*..................-..113.......3*..............219.........495%................40....97.......*.......670.60..../..........'
# regex = re.compile('[0-9]+')
# numbers= regex.finditer(string,re.NOFLAG)
# for match in numbers:
#     print(match)

for x in range(len(lines)):
    regex = re.compile('\d+')
    string = lines[x]
    numbers = regex.finditer(string,re.NOFLAG)
    print(lines[x])
    for match in numbers:
        print(match)
        start_pos = match.span()[0]
        end_pos = match.span()[1]
        number_value = match.group()
        # Check left and right
        #print(match)
        if lines[x][start_pos - 1] != '.' or lines[x][end_pos] != '.':
            part_numbers.append(int(number_value))
            break
        else:
            # check symbols in line above and below
            for y in range(start_pos - 1, end_pos + 1):
                if lines[x - 1][y] != '.' or lines[x + 1][y] != '.':
                    part_numbers.append(int(number_value))
                    break
print(sum(part_numbers))