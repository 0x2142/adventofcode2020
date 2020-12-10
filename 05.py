data = [x.strip() for x in open('./05-input.txt')]

def findRow(ticket):
    min = 0
    max = 128
    for step in ticket[:7]:
        half = (max - min) / 2
        if step == "F":
            max -= half
        if step == "B":
            min += half 
    row = max - 1
    return row

def findColumn(ticket):
    min = 0
    max = 8
    for step in ticket[3:]:
        half = (max - min) / 2
        if step == "L":
            max -= half
        if step == "R":
            min += half 
    column = max - 1
    return column

def findHighestSeatID():
    seat_ids = []
    for ticket in data:
        row = findRow(ticket)
        column = findColumn(ticket)
        seat = (row * 8) + column
        seat_ids.append(seat)

    highest_seat_id = 0
    for seat in seat_ids:
        if seat > highest_seat_id:
            highest_seat_id = seat

    print(f"Highest Seat ID is: {highest_seat_id}")

def findMissingSeat():
    line = []
    for i in range(8):
        line.append("")
    planeGrid = []
    for i in range(128):
        planeGrid.append(list(line))
    for ticket in data:
        row = findRow(ticket)
        column = findColumn(ticket)
        planeGrid[int(row)][int(column)] = 'X'
    rownum = 0
    print("Printing plane layout:")
    for each in planeGrid: 
        print(f'{rownum}: {each}')
        rownum +=1
    

findHighestSeatID()
findMissingSeat()
