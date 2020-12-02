data = [int(x.strip()) for x in open('./01-input.txt')]

# Problem 1
for num1 in data:
    for num2 in data:
        if num1 + num2 == 2020:
                print(num1*num2)

#Problem 2
for num1 in data:
    for num2 in data:
        for num3 in data:
            if num1 + num2 + num3 == 2020:
                print(num1*num2*num3)


