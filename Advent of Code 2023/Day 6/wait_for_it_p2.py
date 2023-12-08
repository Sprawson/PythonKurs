"""--- Part Two ---
As the race is about to start, you realize the piece of paper with race times and record distances you got earlier actually just has very bad kerning. There's really only one race - ignore the spaces between the numbers on each line.

So, the example from before:

Time:      7  15   30
Distance:  9  40  200
...now instead means this:

Time:      71530
Distance:  940200
Now, you have to figure out how many ways there are to win this single race. In this example, the race lasts for 71530 milliseconds and the record distance you need to beat is 940200 millimeters. You could hold the button anywhere from 14 to 71516 milliseconds and beat the record, a total of 71503 ways!

How many ways can you beat the record in this one much longer race?"""

f = open("input2.txt", 'r')
input_file = f.read()

race_time = int(input_file.split("\n")[0].split(":")[1].replace(" ", ""))
race_distance_record = int(input_file.split("\n")[1].split(":")[1].replace(" ", ""))

ways_to_win = 0
ways_to_win_multiplied = 1
for t in range(1, int(race_time) - 1):
    race_distance = (int(race_time) - t) * t
    if race_distance > int(race_distance_record):
        ways_to_win = ways_to_win + 1
print(ways_to_win)
