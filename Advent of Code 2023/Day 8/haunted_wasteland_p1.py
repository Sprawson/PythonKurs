"""This format defines each node of the network individually. For example:

RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
Starting with AAA, you need to look up the next element based on the next left/right instruction in your input. In this example, start with AAA and go right (R) by choosing the right element of AAA, CCC. Then, L means to choose the left element of CCC, ZZZ. By following the left/right instructions, you reach ZZZ in 2 steps.

Of course, you might not find ZZZ right away. If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: RL really means RLRLRLRLRLRLRLRL... and so on. For example, here is a situation that takes 6 steps to reach ZZZ:

LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?

"""
with open("input1.txt", 'r') as file:
    instructions = file.readline().strip()
    nodes = file.read().strip().split("\n")

nodes_dict = {}
# create nodes dict
for node in nodes:
    nodes_dict.update({node[0:3]: [node[7:10], node[12:15]]})

# instructions to binary:
instructions = instructions.replace('R', '1')
instructions = instructions.replace('L', '0')

steps = 0
next_move = "AAA"
while next_move != 'ZZZ':
    for direction in instructions:
        next_move = nodes_dict[next_move][int(direction)]
        steps += 1
        if next_move == 'ZZZ':
            break

print(steps)
print(next_move)
