import random

# M x N matrix

# Random scenarios generation:

M = random.randint(3, 7)
N = random.randint(3, 7)

random_matrix = []

for i in range(N):
    line = []
    for j in range(M):
        if random.randint(0, 1) == 1:
            line.append(True)
        else:
            line.append(False)
    random_matrix.append(line)

print(M)
print(N)
for item in random_matrix:
    print(item)

# False = Wall
# True = Tile


def minimum_steps(matrix, start, end):
    pass


matrix = [
    [False, False, False, False],
    [True, True, False, True],
    [False, False, False, False],
    [False, False, False, False]
]

matrix_size = (4, 4)

start = (3, 0)
end = (0, 0)

expected_outcome = 7

current_position = start

problem_not_solved = True

total_steps = 0
while problem_not_solved:
    if current_position == end:
        print(total_steps)
        problem_not_solved = False
