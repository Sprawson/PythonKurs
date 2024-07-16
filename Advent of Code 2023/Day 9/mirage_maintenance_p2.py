"""--- Part Two ---
Of course, it would be nice to have even more history included in your report. Surely it's safe to just extrapolate
backwards as well, right?

For each history, repeat the process of finding differences until the sequence of differences is entirely zero.
Then, rather than adding a zero to the end and filling in the next values of each previous sequence, you should instead
add a zero to the beginning of your sequence of zeroes, then fill in new first values for each previous sequence.

In particular, here is what the third example history looks like when extrapolating back in time:

5  10  13  16  21  30  45
  5   3   3   5   9  15
   -2   0   2   4   6
      2   2   2   2
        0   0   0
Adding the new values on the left side of each sequence from bottom to top eventually reveals
the new left-most history value: 5.

Doing this for the remaining example data above results in previous values of -3 for the
 history and 0 for the second history. Adding all three new values together produces 2.

Analyze your OASIS report again, this time extrapolating the previous value for each history.
 is the sum of these extrapolated values?"""


with open("input.txt", 'r') as file:
    lines = file.readlines()

history_sets = []
for line in lines:
    line = line.strip()
    history_sets.append([int(x) for x in line.split(" ")])

sum_extrapolated = 0
for history in history_sets:

    differences = []
    values = []
    sum_last = history[-1]
    first_row = history
    # check when all elements after subtraction reach 0:
    while set(history) != {0}:
        # find differences between numbers
        for n in range(len(history)-1):
            # append differences to values list
            values.append(history[n+1] - history[n])
        # differences will store all previous values
        differences.append(values)
        # next iteration will calculate differences for the values just calculated until all of them are 0
        history = values
        # reset values
        values = []
    # add first row to the all extrapolated values
    differences.insert(0, first_row)
    # so now row from the top will be last
    differences.reverse()
    diff = 0
    # calculate difference row by row to the last (top) row
    for step in differences:
        diff = step[0] - diff
    sum_extrapolated += diff

print(sum_extrapolated)
