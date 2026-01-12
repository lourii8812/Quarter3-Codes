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
maxsteps = 0
nameW = " "
listv = []
for i in range(len(steps)):
    totalsum = 0
    totalsum = sum(steps[i])
    listv.append(totalsum)
    print(f"Total steps of {names[i]}: {totalsum}")
    if totalsum > maxsteps:
        nameW = names[i]
diff = max(listv) - min(listv)
print(f"The person with the highest number of steps is: {nameW} !!!")
print(f"The difference between highest and lowest values is: {diff} steps.")
