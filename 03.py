data = [x.strip() for x in open('./03-input.txt')]

def checkTrees(right, down):
    tree = 0
    position = 0
    down_init = down
    down = 1
    for line in data:
        if down != 1:
            down -= 1
            continue
        landscape = line * 100
        if landscape[position] == '#':
            tree += 1
        position += right
        down = down_init
    return tree


p1tree = checkTrees(3, 1)
print('~'*30)
print(f'Problem #1 - Number of trees: {p1tree}')
print('~'*30)
# Check each additional slope
p2s1tree = checkTrees(1, 1)
print(f'Problem #2, Slope #1 - Number of trees: {p2s1tree}')
p2s2tree = checkTrees(3, 1)
print(f'Problem #2, Slope #2 - Number of trees: {p2s2tree}')
p2s3tree = checkTrees(5, 1)
print(f'Problem #2, Slope #3 - Number of trees: {p2s3tree}')
p2s4tree = checkTrees(7, 1)
print(f'Problem #2, Slope #4 - Number of trees: {p2s4tree}')
p2s5tree = checkTrees(1, 2)
print(f'Problem #2, Slope #5 - Number of trees: {p2s5tree}')
print('~'*30)
# Multiply all together
totaltree = p2s1tree * p2s2tree * p2s3tree * p2s4tree * p2s5tree
print(f'Total Trees for Problem #2: {totaltree}')