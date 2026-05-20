frac = input("Enter a fraction (ex. 17/24)\n")
frac = frac.split("/")
newNums = []
for num in frac:
    newNums.append(int(num))

saved = 1
lowestNum = min(newNums)
currNum = int(lowestNum / 2)

while currNum > 1:
    if newNums[0] % currNum == 0 and newNums[1] % currNum == 0:
        saved = currNum
        break # Common Multiple Found
    currNum -= 1

currNum = lowestNum
if newNums[0] % currNum == 0 and newNums[1] % currNum == 0:
    saved = currNum

newNums[0] = newNums[0] / saved
newNums[1] = newNums[1] / saved

print(f"{str(int(newNums[0]))}/{str(int(newNums[1]))}")
