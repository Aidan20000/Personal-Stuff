frac = input("Enter a fraction (ex. 17/24)\n")
frac = frac.split("/")
newNums = []
for num in frac:
    newNums.append(int(num))

saved = 1
lowestNum = min(newNums)
x = int(lowestNum / 2)

while x > 1:
    if newNums[0] % x == 0 and newNums[1] % x == 0:
        saved = x
        break # Common Multiple Found
    x -= 1

x = lowestNum
if newNums[0] % x == 0 and newNums[1] % x == 0:
    saved = x

newNums[0] = newNums[0] / saved
newNums[1] = newNums[1] / saved

print(f"{str(int(newNums[0]))}/{str(int(newNums[1]))}")
