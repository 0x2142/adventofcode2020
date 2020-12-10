import re
data = [x.strip() for x in open('./04-input.txt')]

validcount = 0
validdata = 0
reqfields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def checkPassport(passportinfo):
    # Part 1 - check if passport has all required fields
    if all(field in passportinfo for field in reqfields):
        return True

def validateData(passportinfo):
    # Part 2 - validate data meets requirements
    byr = re.match('.*byr\:(19[2-9][0-9]|200[0-2]).*', passportinfo)
    iyr = re.match('.*iyr\:20[1-2][0-9].*', passportinfo)
    eyr = re.match('.*eyr\:20[2-3][0-9].*', passportinfo)
    hgt = re.match('.*hgt\:(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in).*', passportinfo)
    hcl = re.match('.*hcl\:#(\w|\d){6}.*', passportinfo)
    ecl = re.match('.*ecl\:(amb|blu|brn|gry|grn|hzl|oth).*', passportinfo)
    pid = re.match('.*pid\:\d{9}.*', passportinfo)
    validationList = [byr, iyr, eyr, hgt, hcl, ecl, pid]
    if all(field for field in validationList):
        return True


passportinfo = ""

for line in data:
    if line == "":
        if checkPassport(passportinfo):
            validcount += 1
            if validateData(passportinfo):
                validdata += 1
        passportinfo = ""
    passportinfo += " " + line

print(f'Valid Passports: {validcount}, Valid Data: {validdata}')

#134 is too low