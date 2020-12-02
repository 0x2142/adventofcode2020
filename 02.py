data = [x.strip() for x in open('./02-input.txt')]

firstcount = 0
secondcount = 0
for line in data:
    linedata = line.split(" ")
    minlen = linedata[0].split("-")[0]
    maxlen = linedata[0].split("-")[1]
    matchletter = linedata[1][0]
    passwd = linedata[2]
    lettercount = 0
    # Count matches for problem 1
    for letter in passwd:
        if letter == matchletter:
            lettercount += 1
    if lettercount >= int(minlen) and lettercount <= int(maxlen):
        firstcount += 1
    # Count matches for problem 2 
    minlen = int(minlen) - 1
    maxlen = int(maxlen) - 1
    if passwd[int(minlen)] == matchletter or passwd[int(maxlen)] == matchletter:
        if passwd[int(minlen)] == matchletter and passwd[int(maxlen)] == matchletter:
            continue
        else:
            secondcount += 1
print('problem 1 total matches: %s' % firstcount)
print('problem 2 total matches: %s' % secondcount)



