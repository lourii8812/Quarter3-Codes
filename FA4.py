names = ["Me", "Lia", "Jake"]

steps =[
[4500, 5200, 4800, 5000, 5300],
[4000, 4100, 3900, 4200, 4600],
[6000, 5800, 5900, 6100, 6200]
]

print(f"{'Name':<6} | Day1  | Day2  | Day3  | Day4  | Day5")
print("_" * 45)

for name, stepz in zip(names, steps):
    print(
        f"{name:<6} | "
        f"{stepz[0]:<5} | {stepz[1]:<5} | {stepz[2]:<5} | "
        f"{stepz[3]:<5} | {stepz[4]:<5}"
    )
dictm = {}
for i in range(len(steps)):
    totalsum = 0
    for j in range(len(steps[i])):
        sum1 = steps[0+i][0+j]
        totalsum = totalsum + sum1
    dictm[names[i]] = totalsum
print(dictm)
maxdict = max(dictm, key = dictm.get)
print(f"The person with the highest amount of steps is {maxdict} with {dictm[maxdict]} steps.")
